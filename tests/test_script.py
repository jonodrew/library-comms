from src.read import get_details


def test_get_details():
    details = get_details(filepath="tests/test_data.csv")
    assert {"Student_name": "Harry", "Student_ID": "ABC123", "Student_phone_number": "07777777777"} in details