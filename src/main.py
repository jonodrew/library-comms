from src.message import filter_data, create_message, send_message
from src.read import get_details


def main(filepath: str) -> None:
    list_of_dict = get_details(filepath)
    filtered_data = filter_data(list_of_dict)
    for row in filtered_data:
        message = create_message(row)
        number = row["Student_phone_number"]
        send_message(message, number)
