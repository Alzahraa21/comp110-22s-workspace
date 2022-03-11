"""Dictionaries."""
__author__ = "730358329"


def invert(dict_input: dict[str, str]) -> dict[str, str]:
    """Function inverts the string key and value of a dictionary input."""
    invert_dict: dict[str, str] = {}
    for key in dict_input:
        if dict_input[key] in invert_dict:
            raise KeyError("Error")
        else:
            invert_dict[dict_input[key]] = key
    return invert_dict


def favorite_color(input: dict[str, str]) -> str:
    """Function counts the presence of a certain color in dictionary input and returns the most cited color."""
    result: str = ""
    max: int = 0
    counting_dict: dict[str, int] = {}
    for key in input:
        if input[key] in counting_dict:
            counting_dict[input[key]] = counting_dict[input[key]] + 1
        else:
            counting_dict[input[key]] = 1
    for key in counting_dict:
        if counting_dict[key] > max:
            max = counting_dict[key]
            result = key
    return result 


def count(input: list[str]) -> dict[str, int]:
    """Function counts the frequency of items in a list."""
    result_dict: dict[str, int] = {}
    for i in input:
        if i in result_dict:
            result_dict[i] = result_dict[i] + 1
        else:
            result_dict[i] = 1
    return result_dict
