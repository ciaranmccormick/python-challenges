from level_0 import (
    add_x_and_y,
    subtract_x_and_y,
    divide_x_by_y,
    multiply_x_and_y,
    remainder_of_x_and_y,
    is_even,
    even_characters,
    fifth_letter, first_and_fifth_letter)


def test_add_x_and_y():
    assert add_x_and_y(1, 2) == 3
    assert add_x_and_y(2, 3) == 5


def test_subtract_x_and_y():
    assert subtract_x_and_y(3, 2) == 1
    assert subtract_x_and_y(2, 3) == -1
    assert subtract_x_and_y(5, 5) == 0


def test_divide_x_by_y():
    assert divide_x_by_y(5, 2) == 2.5
    assert divide_x_by_y(3, 3) == 1
    assert divide_x_by_y(10, 5) == 2


def test_multiply_x_and_y():
    assert multiply_x_and_y(3, 9) == 9
    assert multiply_x_and_y(-1, 5) == -5
    assert multiply_x_and_y(2.5, 3) == 7.5


def test_remainder_of_x_and_y():
    assert remainder_of_x_and_y(5, 2) == 1
    assert remainder_of_x_and_y(6, 3) == 0
    assert remainder_of_x_and_y(5, 3) == 2


def test_is_even():
    assert is_even(4)
    assert not is_even(5)
    assert is_even(6)
    assert not is_even(17)
    assert is_even(0)
    assert is_even(-4)
    assert not is_even(-5)


def test_even_characters():
    assert not even_characters("hello")
    assert even_characters("world!")
    assert even_characters("ciaran")
    assert not even_characters("max")


def test_fifth_letter():
    assert fifth_letter("hello") == "o"
    assert fifth_letter("yes") == "y"
    assert fifth_letter("world!") == "d"


def test_first_and_fifth_letter():
    assert first_and_fifth_letter("hello") == "ho"
    assert first_and_fifth_letter("yes") == "yy"
    assert first_and_fifth_letter("a") == "aa"

