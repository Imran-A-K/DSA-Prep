from tests._loader import load_func

permute_unique = load_func("permute_unique")


def normalize(perms):
    """Order-insensitive comparison: List[List[int]] -> Set[Tuple[int]]"""
    return set(tuple(p) for p in perms)


def assert_all_perms_use_same_multiset(nums, perms):
    target = sorted(nums)
    for p in perms:
        assert sorted(p) == target


# ---------- Core examples ----------
def test_example_1():
    nums = [1, 1, 2]
    result = permute_unique(nums)

    expected = {
        (1, 1, 2),
        (1, 2, 1),
        (2, 1, 1),
    }

    assert normalize(result) == expected
    assert_all_perms_use_same_multiset(nums, result)


def test_example_2():
    nums = [1, 2, 3]
    result = permute_unique(nums)

    # Should match standard permutations count: 3! = 6
    assert len(normalize(result)) == 6
    assert_all_perms_use_same_multiset(nums, result)


# ---------- Edge cases ----------
def test_empty():
    # LeetCode convention: [[]]
    assert normalize(permute_unique([])) == {()}

def test_single():
    assert normalize(permute_unique([7])) == {(7,)}

def test_all_duplicates():
    nums = [2, 2, 2]
    result = permute_unique(nums)
    assert normalize(result) == {(2, 2, 2)}
    assert len(result) == 1


# ---------- Correctness properties ----------
def test_duplicate_handling_count():
    # [1,1,2,2] has 4!/(2!*2!) = 6 unique permutations
    nums = [1, 1, 2, 2]
    result = permute_unique(nums)
    assert len(normalize(result)) == 6
    assert_all_perms_use_same_multiset(nums, result)

def test_no_duplicates_in_output():
    nums = [1, 1, 2]
    result = permute_unique(nums)
    assert len(result) == len(normalize(result))  # no duplicates returned


# ---------- Negative values + duplicates ----------
def test_negative_and_zero_duplicates():
    nums = [-1, 0, -1]
    result = permute_unique(nums)

    expected = {
        (-1, -1, 0),
        (-1, 0, -1),
        (0, -1, -1),
    }

    assert normalize(result) == expected
    assert_all_perms_use_same_multiset(nums, result)


# ---------- Input immutability ----------
def test_input_not_modified():
    nums = [1, 1, 2]
    original = nums[:]
    permute_unique(nums)
    assert nums == original