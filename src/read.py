from csv import DictReader

def get_details(filepath: str) -> list[dict[str, str]]:
    """
    Read from the CSV at filepath and return a list of the details in dictionary format
    :param filepath:
    :return:
    """
    with open(filepath, 'r') as f:
        dict_reader = DictReader(f)
        list_of_dict = list(dict_reader)
    return list_of_dict