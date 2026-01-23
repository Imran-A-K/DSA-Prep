from tests._loader import load_func

sorted_squares = load_func("sorted_squares")

def test_example_1():
    assert sorted_squares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]

def test_example_2():
    assert sorted_squares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]

def test_all_negative():
    assert sorted_squares([-5, -4, -3]) == [9, 16, 25]

def test_single():
    assert sorted_squares([0]) == [0]