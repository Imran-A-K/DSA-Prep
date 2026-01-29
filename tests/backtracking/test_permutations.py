from tests._loader import load_func

permute = load_func("permute")


def normalize(result):
    """
    Normalize permutations for order-insensitive comparison.
    Converts List[List[int]] → Set[Tuple[int]].
    """
    return set(tuple(p) for p in result)


# ---------- Basic examples ----------
def test_example_1():
    nums = [1, 2, 3]
    result = permute(nums)

    expected = {
        (1, 2, 3),
        (1, 3, 2),
        (2, 1, 3),
        (2, 3, 1),
        (3, 1, 2),
        (3, 2, 1),
    }

    assert normalize(result) == expected


def test_example_2():
    nums = [0, 1]
    result = permute(nums)

    expected = {
        (0, 1),
        (1, 0),
    }

    assert normalize(result) == expected


def test_single_element():
    assert normalize(permute([1])) == {(1,)}


# ---------- Edge cases ----------
def test_empty_array():
    # LeetCode defines this as returning [[]]
    assert normalize(permute([])) == {()}


def test_two_elements():
    assert normalize(permute([1, 2])) == {(1, 2), (2, 1)}


# ---------- Correctness properties ----------
def test_permutation_length():
    nums = [1, 2, 3, 4]
    result = permute(nums)
    assert len(result) == 24  # 4! = 24


def test_each_permutation_uses_all_elements():
    nums = [1, 2, 3]
    result = permute(nums)
    for p in result:
        assert sorted(p) == sorted(nums)


def test_no_duplicates():
    nums = [1, 2, 3]
    result = permute(nums)
    assert len(result) == len(normalize(result))


# ---------- Input immutability ----------
def test_input_not_modified():
    nums = [1, 2, 3]
    original = nums[:]
    permute(nums)
    assert nums == original


# ---------- Negative numbers ----------
def test_with_negative_numbers():
    nums = [-1, 0, 1]
    expected = {
        (-1, 0, 1),
        (-1, 1, 0),
        (0, -1, 1),
        (0, 1, -1),
        (1, -1, 0),
        (1, 0, -1),
    }

    assert normalize(permute(nums)) == expected