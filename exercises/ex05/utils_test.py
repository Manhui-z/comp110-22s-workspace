"""Exercie 05 of unit tests."""

__author__ = "730442764"

from utils import only_evens, sub, concat


def test_utils_empty() -> None:
    """If all entry list are empty list, then the results should be empty list."""
    xs: list[int] = []
    a_list: list[int] = []
    start: int = 1
    end: int = -1
    ys: list[int] = []
    zs: list[int] = []

    assert only_evens(xs) == []
    assert sub(a_list, start, end) == []
    assert concat(ys, zs) == []


def test_utils_many_items() -> None:
    """Test whether the function work as I expected."""
    xs: list[int] = [1, 2, 3, 4]
    a_list: list[int] = [10, 20, 30, 40, 50]
    start: int = 1
    end: int = 4
    ys: list[int] = [1, 2, 3, 4]
    zs: list[int] = [5, 6, 7, 8]

    assert only_evens(xs) == [2, 4]
    assert sub(a_list, start, end) == [20, 30, 40]
    assert concat(ys, zs) == [1, 2, 3, 4, 5, 6, 7, 8]


def test_utils_many_items_again() -> None:
    """Test functions with more variation in integers in the list."""
    xs: list[int] = [45, 22, 30, 67, 50]
    a_list: list[int] = [149, 42, 236, 110, 58, 372, 445]
    start: int = -1
    end: int = 5
    ys: list[int] = [18, 526, 33, 747]
    zs: list[int] = [55, 614, 97, 8]

    assert only_evens(xs) == [22, 30, 50]
    assert sub(a_list, start, end) == [149, 42, 236, 110, 58]
    assert concat(ys, zs) == [18, 526, 33, 747, 55, 614, 97, 8]