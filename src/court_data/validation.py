from collections.abc import Iterable, Mapping
from datetime import date
from typing import TypedDict


class ValidationResult(TypedDict):
    valid: bool
    errors: list[str]


def validate_case_record(record: Mapping[str, object]) -> ValidationResult:
    errors: list[str] = []
    for field in ("case_id", "case_title", "decision_date"):
        value = record.get(field)
        if value is None or (isinstance(value, str) and not value.strip()):
            errors.append(f"Missing required field: {field}")
        elif not isinstance(value, str):
            errors.append(f"{field} must be a string")

    date_value = record.get("decision_date")
    if isinstance(date_value, str) and date_value.strip():
        try:
            parsed = date.fromisoformat(date_value)
            if parsed.isoformat() != date_value:
                raise ValueError
        except ValueError:
            errors.append("decision_date must use YYYY-MM-DD format")

    return {"valid": not errors, "errors": errors}


def find_duplicate_cases(records: Iterable[Mapping[str, object]]) -> list[str]:
    seen: set[str] = set()
    duplicates: list[str] = []
    for record in records:
        case_id = record.get("case_id")
        if not isinstance(case_id, str) or not case_id.strip():
            continue
        if case_id in seen:
            duplicates.append(case_id)
        else:
            seen.add(case_id)
    return duplicates
