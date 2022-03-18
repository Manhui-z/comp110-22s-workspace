"""Exercie 06 of dictionary functions."""

__author__ = "730442764"


def invert(a: dict[str, str]) -> dict[str, str]:
    """Invert the key and value of the dictionary."""
    result: dict[str, str] = {}
    for key in a:
        a_value: str = a[key]
        if a_value in result:
            raise KeyError
        result[a[key]] = key
    return result


def favorite_color(b: dict[str, str]) -> str:
    """Return the favorite color for each people."""
    color: str = ""
    largest: int = 0
    color_freq: dict[str, int] = {}
    for b_key in b:
        b_value: str = b[b_key]
        if b_value in color_freq:
            color_freq[b_value] += 1
        else:
            color_freq[b_value] = 1
    print(color_freq)

    for color_freq_key in color_freq:
        if largest < color_freq[color_freq_key]:
            largest = color_freq[color_freq_key]
            color = color_freq_key

    return color

            
def count(c: list[str]) -> dict[str, int]:
    """Count the number of times that value appered in the input list."""
    count_freq: dict[str, int] = {}
    for c_key in c:
        if c_key in count_freq:
            count_freq[c_key] += 1
        else:
            count_freq[c_key] = 1
    return count_freq
