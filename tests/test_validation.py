import pytest

from src.court_data.validation import (
    find_duplicate_cases,
    validate_case_record,
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


@pytest.mark.parametrize("field", ["case_id", "case_title", "decision_date"])
@pytest.mark.parametrize("value", [None, "", "   ", 0, False, [], {}])
def test_required_fields_reject_invalid_values(field, value):
    record = {
        "case_id": "CASE-001",
        "case_title": "Synthetic Case",
        "decision_date": "2024-02-29",
    }
    record[field] = value
    result = validate_case_record(record)
    assert result["valid"] is False
    assert any(field in error for error in result["errors"])


@pytest.mark.parametrize(
    "value",
    [
        "2023-02-29",
        "2026-04-31",
        "2026-1-1",
        "20260101",
        "2026-W01-1",
        "2026-01-01T00:00:00",
        " 2026-01-01",
    ],
)
def test_rejects_invalid_or_noncanonical_dates(value):
    result = validate_case_record(
        {
            "case_id": "CASE-001",
            "case_title": "Synthetic Case",
            "decision_date": value,
        }
    )
    assert result == {
        "valid": False,
        "errors": ["decision_date must use YYYY-MM-DD format"],
    }


def test_accepts_leap_day_without_mutating_input():
    record = {
        "case_id": "CASE-001",
        "case_title": "Synthetic Case",
        "decision_date": "2024-02-29",
    }
    original = record.copy()
    assert validate_case_record(record) == {"valid": True, "errors": []}
    assert record == original


def test_reports_all_missing_fields():
    result = validate_case_record({})
    assert result["valid"] is False
    assert len(result["errors"]) == 3


def test_duplicate_detection_ignores_invalid_identifiers():
    records = (
        {"case_id": value}
        for value in [
            None,
            None,
            [],
            {},
            "",
            " ",
            1,
            "CASE-001",
            "CASE-001",
            "CASE-001",
        ]
    )
    assert find_duplicate_cases(records) == ["CASE-001", "CASE-001"]
