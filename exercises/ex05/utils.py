"""EX05."""
__author__ = "730358329"


def only_evens(list_of_ints: list[int]) -> list[int]:
    """Returns a list with only evens."""
    i: int = 0
    new_list: list[int] = []
    while i < len(list_of_ints):
        if list_of_ints[i] % 2 == 0:
            new_list.append(list_of_ints[i])
        i = i + 1
    return new_list


def sub(list_of_ints: list[int], start_index: int, end_index: int) -> list[int]:
    """Returns a list that begins at a specific index and ends at a specific index."""
    sub_list: list[int] = list()
    if start_index < 0:
        start_index = 0
    if end_index > len(list_of_ints):
        end_index = len(list_of_ints)
    if len(list_of_ints) == 0 or start_index > len(list_of_ints) or end_index <= 0:
        sub_list = []
    while start_index < end_index:
        sub_list.append(list_of_ints[start_index])
        start_index = start_index + 1
    return sub_list


def concat(list_one: list[int], list_two: list[int]) -> list[int]:
    """Combines lists."""
    i: int = 0
    while i < len(list_two):
        list_one.append(list_two[i])
        i = i + 1
    return list_one
