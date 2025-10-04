
import datetime

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