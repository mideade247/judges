from datetime import datetime


def validate_case_record(record):
    required_fields = [
        "case_id",
        "case_title",
        "decision_date",
    ]

    errors = []

    for field in required_fields:
        value = record.get(field)

        if value is None or (
            isinstance(value, str) and not value.strip()
        ):
            errors.append(f"Missing required field: {field}")

    date_value = record.get("decision_date")

    if date_value:
        try:
            datetime.strptime(str(date_value), "%Y-%m-%d")
        except ValueError:
            errors.append(
                "decision_date must use YYYY-MM-DD format"
            )

    return {
        "valid": len(errors) == 0,
        "errors": errors,
    }


def find_duplicate_cases(records):
    seen = set()
    duplicates = []

    for record in records:
        case_id = record.get("case_id")

        if case_id in seen:
            duplicates.append(case_id)
        else:
            seen.add(case_id)

    return duplicates
