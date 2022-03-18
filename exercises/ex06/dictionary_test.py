"""Exercie 06 of unit tests."""

__author__ = "730442764"

from dictionary import invert, favorite_color, count


def test_dictionary_empty() -> None:
    """If all imput are empty, then all results should be empty."""
    a: dict[str, str] = {}
    b: dict[str, str] = {}
    c: list[str] = []

    assert invert(a) == {}
    assert favorite_color(b) == ""
    assert count(c) == {}


def test_dictionary_many_items() -> None:
    """Test whether the function work as I expected."""
    a: dict[str, str] = {"apple": "cat", "banana": "dog"}
    b: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    c: list[str] = ["a", "b", "c", "a"]

    assert invert(a) == {"cat": "apple", "dog": "banana"}
    assert favorite_color(b) == "blue"
    assert count(c) == {'a': 2, 'b': 1, 'c': 1}


def test_dictionary_many_items_again() -> None:
    """Test functions with more variation in inputs."""
    a: dict[str, str] = {"one": "first", "two": "second", "three": "third", "four": "fourth"}
    b: dict[str, str] = {"Zhu": "Green", "Hu": "White", "Zhang": "Blue", "Xie": "Green"}
    c: list[str] = ["one", "one", "six", "five", "two", "one", "six"]

    assert invert(a) == {"first": "one", "second": "two", "third": "three", "fourth": "four"}
    assert favorite_color(b) == "Green"
    assert count(c) == {'one': 3, 'six': 2, 'five': 1, 'two': 1}