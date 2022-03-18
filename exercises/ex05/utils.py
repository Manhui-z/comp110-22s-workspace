"""Exercie 05 of funtion skeletons."""

__author__ = "730442764"


def only_evens(xs: list[int]) -> list[int]:
    """Return a list containing only even inputs."""
    evenlist: list[int] = list()
    i: int = 0
    while i < len(xs):
        if xs[i] % 2 == 0:
            evenlist.append(xs[i])
        i += 1
    return evenlist


def sub(a_list: list[int], start: int, end: int) -> list[int]:
    """Return a list from my start to the end(exclude)."""
    sublist: list[int] = list()
    i = start

    while i < end and end < len(a_list):
        if i > 0:
            sublist.append(a_list[i])
        elif i <= 0 and end < len(a_list):
            i = 0
            sublist.append(a_list[0])
        i += 1
    while i < len(a_list) and end >= len(a_list):
        if i > 0:
            sublist.append(a_list[i])
        elif i <= 0 and end < len(a_list):
            i = 0
            sublist.append(a_list[0])
        i += 1
    if len(a_list) == 0 and start > len(a_list) and end <= len(a_list):
        sublist = list()

    return sublist


def concat(ys: list[int], zs: list[int]) -> list[int]:
    """Return a list that contains all elements of two list."""
    concat_one: list[int] = list()
    concat_two: list[int] = list()
    i: int = 0
    a: int = 0
    while i < len(ys):
        concat_one.append(ys[i])
        i += 1
    concat_two = concat_one
    while a < len(zs):
        concat_two.append(zs[a])
        a += 1
    return concat_two


    
