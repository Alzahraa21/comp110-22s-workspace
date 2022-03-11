"""Testing."""
__author__ = "730358329"


from exercises.ex06.dictionary import invert, count, favorite_color
import pytest


def test_list_normal() -> None: 
    """Test a normal dictionary with no repeats."""
    input: dict[str, str] = {'a': 'x', 'b': 'y', 'c': 'z'}
    assert invert(input) == {'x': 'a', 'y': 'b', 'z': 'c'}


def test_list_repeat() -> None:
    """Tests an edge case with repeats that lead to error."""
    with pytest.raises(KeyError): 
        input: dict[str, str] = {'x': 'a', 'y': 'a', 'z': 'b', 'w': 'c'}
        invert(input)


def test_empty_dict() -> None:
    """Tests an empty dictionary."""
    input: dict[str, str] = {}
    assert invert(input) == {}


def test_colors_single() -> None:
    """Each person has different favorite colors."""
    input: dict[str, str] = {'sarah': 'yellow', 'ashley': 'pink', 'james': 'red'}
    assert favorite_color(input) == ("yellow")


def test_colors() -> None:
    """One color has the highest count."""
    input: dict[str, str] = {'sarah': 'pink', 'ashley': 'pink', 'james': 'red'}
    assert favorite_color(input) == ("pink")


def test_colors_more() -> None:
    """One color has the highest count."""
    input: dict[str, str] = {'sarah': 'pink', 'ashley': 'pink', 'james': 'red', 'lily': 'green', 'ahmed': 'red'}
    assert favorite_color(input) == ("pink")


def test_count_list_() -> None:
    """Each letter in list is present once."""
    input: list[str] = ["a", "b", "c", "d"]
    assert count(input) == {'a': 1, 'b': 1, 'c': 1, 'd': 1}


def test_count_list_with_repeat_() -> None:
    """Letters are present in different frequencies."""
    input: list[str] = ["a", "b", "c", "d", "a", "b", "a"]
    assert count(input) == {'a': 3, 'b': 2, 'c': 1, 'd': 1}


def test_count_list_empty_() -> None:
    """Input is an empty list."""
    input: list[str] = []
    assert count(input) == {}
