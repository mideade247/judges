from src.court_data.validation import (
    validate_case_record,
    find_duplicate_cases,
)


def test_valid_case_record():
    record = {
        "case_id": "CASE-001",
        "case_title": "Example Case",
        "decision_date": "2026-01-15",
    }

    result = validate_case_record(record)

    assert result["valid"] is True
    assert result["errors"] == []


def test_missing_case_title():
    record = {
        "case_id": "CASE-001",
        "case_title": "",
        "decision_date": "2026-01-15",
    }

    result = validate_case_record(record)

    assert result["valid"] is False
    assert "Missing required field: case_title" in result["errors"]


def test_invalid_date():
    record = {
        "case_id": "CASE-001",
        "case_title": "Example Case",
        "decision_date": "15/01/2026",
    }

    result = validate_case_record(record)

    assert result["valid"] is False


def test_duplicate_case_ids():
    records = [
        {"case_id": "CASE-001"},
        {"case_id": "CASE-002"},
        {"case_id": "CASE-001"},
    ]

    duplicates = find_duplicate_cases(records)

    assert duplicates == ["CASE-001"]


def test_no_duplicates():
    records = [
        {"case_id": "CASE-001"},
        {"case_id": "CASE-002"},
    ]

    assert find_duplicate_cases(records) == []
