
import datetime

from twilio.rest import Client


def filter_date(all_data: list[dict[str, str]]) -> list[dict[str, str]]:
    """Takes all data on due and overdue items and filters for items due tomorrow or in the past"""
    filtered_data = []
    today = datetime.date.today()
    for row in all_data:
        due_date = datetime.datetime.strptime(row["Due_date"], "%d/%m/%Y").date()
        if due_date < today or due_date == today + datetime.timedelta(days=1):
            filtered_data.append(row)
    return filtered_data

def create_message(user_details: dict[str, str]) -> str:
    """
    Create a message from a user's details. The kind of message that will be created depends on the due date.
    Assumption: this function is only called when the due date is tomorrow or in the past
    :param user_details:
    :return:
    """
    today = datetime.date.today()
    due_date = datetime.datetime.strptime(user_details["Due_date"], "%d/%m/%Y").date()
    if due_date < today:
        return f"Hello, {user_details["Student_name"]}! You're overdue!"
    else:
        return f"Hello, {user_details["Student_name"]}! You're due tomorrow!"

def send_message(message: str, phone_number: str) -> None:
    client = create_client()
    sent_message = client.messages.create(
        to=phone_number,
        from_="07123456789",
        body=message
    )
    return None

    # //
    # base_message = f"Hello {name}"
    # if due_date > today:
    #     message  = base_message + "grrr I'm mad"
    # else:
    #     # do something different
    #
    # return ""

# def overdue_message(user_details: dict[str, str]) -> str:
#     return ""
#
# def reminder_message(user_details: dict[str, str]) -> str:
#     return ""
def create_client() -> Client:
    """
    Create a Twilio client using the tokens from the web interface. They should be kept secret and not published.
    :return:
    """
    pass
