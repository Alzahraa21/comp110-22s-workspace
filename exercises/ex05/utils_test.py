"""Exercise five test."""
__author__ = "730358329"

from exercises.ex05.utils import only_evens, sub, concat 


def test_only_evens_sinlge_odd_int() -> None:
    """Tests a list with single odd integer."""
    list_of_ints: list[int] = [3]
    assert only_evens(list_of_ints) == []


def test_only_evens_one_odd_rest_even() -> None:
    """Tests a list with one odd and the rest even."""
    list_of_ints: list[int] = [2, 5, 4, 6, 8]
    assert only_evens(list_of_ints) == [2, 4, 6, 8]


def test_only_evens_mix() -> None:
    """Test a list with a mix of odd and even."""
    list_of_ints: list[int] = [1, 2, 4, 7, 8, 10, 11, 15, 13, 6, 12]
    assert only_evens(list_of_ints) == [2, 4, 8, 10, 6, 12]


def test_sub_start_index_less_than_zero() -> None:
    """The starting index is less than zero."""
    list_of_ints: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert sub(list_of_ints, -2, 5)


def test_sub_end_index_more_than_len() -> None:
    """The end index is more than length of list."""
    list_of_ints: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    assert sub(list_of_ints, 1, 11) == [2, 3, 4, 5, 6, 7, 8]


def test_sub_empty_list() -> None:
    """The start index is more than the length of list."""
    list_of_ints: list[int] = [1, 2, 4, 6, 7, 11, 12]
    assert sub(list_of_ints, 14, 9) == []


def test_concat_empty_second_list() -> None:
    """Add an empty list to the first list."""
    list_one: list[int] = [1, 2, 4, 6, 6, 9]
    list_two: list[int] = []
    assert concat(list_one, list_two) == [1, 2, 4, 6, 6, 9]


def test_concat_normal() -> None:
    """Add two lists together."""
    list_one: list[int] = [1, 6, 8, 9]
    list_two: list[int] = [2, 5, 6, 7]
    assert concat(list_one, list_two) == [1, 6, 8, 9, 2, 5, 6, 7]


def test_concat_empty_first_list() -> None:
    """Add a normal list to an empty list."""
    list_one: list[int] = []
    list_two: list[int] = [2, 5, 6, 7]
    assert concat(list_one, list_two) == [2, 5, 6, 7]
