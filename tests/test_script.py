from unittest.mock import patch
from twilio.rest import Client
from pytest import fixture
from freezegun import freeze_time

from src.read import get_details
from src.message import create_message, filter_date, send_message


@fixture
def single_user():
    return {"Student_name": "Harry", "Student_ID": "ABC123", "Student_phone_number": "07777777777", "Due_date": "01/10/2025"}

def test_get_details(single_user):
    details = get_details(filepath="tests/test_data.csv")
    assert single_user in details

@freeze_time("2025-10-04")
def test_create_message_when_overdue(single_user):
    assert create_message(single_user) == "Hello, Harry! You're overdue!"

@freeze_time("2025-09-30")
def test_create_message_when_due(single_user):
    assert create_message(single_user) == "Hello, Harry! You're due tomorrow!"

@freeze_time("2025-10-04")
def test_filter_date():
    test_details = get_details(filepath="tests/test_data.csv")
    filtered_details = filter_date(test_details)
    assert len(filtered_details) == 2

def test_send_message():
    with patch("src.message.create_client") as mock_twilio_client:
        send_message("Hello, Harry!", "07777777777")
    assert mock_twilio_client.return_value.messages.create.called
