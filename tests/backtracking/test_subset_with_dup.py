from tests._loader import load_func

subsets_with_dup = load_func("subset_with_dup")


def normalize(result):
    """
    Normalize List[List[int]] -> Set[Tuple[int]]
    - Sort each subset
    - Convert to tuple
    - Use set to remove ordering effects
    """
    return set(tuple(sorted(s)) for s in result)


def assert_no_duplicates(result):
    norm = normalize(result)
    assert len(result) == len(norm)


# ---------- Given examples ----------
def test_example_1():
    nums = [1, 2, 2]
    result = subsets_with_dup(nums)

    expected = {
        (),
        (1,),
        (2,),
        (1, 2),
        (2, 2),
        (1, 2, 2),
    }

    assert normalize(result) == expected
    assert_no_duplicates(result)


def test_example_2():
    nums = [0]
    result = subsets_with_dup(nums)
    assert normalize(result) == {(), (0,)}
    assert_no_duplicates(result)


# ---------- Edge cases ----------
def test_empty():
    assert normalize(subsets_with_dup([])) == {()}

def test_all_duplicates():
    nums = [2, 2, 2]
    result = subsets_with_dup(nums)

    expected = {
        (),
        (2,),
        (2, 2),
        (2, 2, 2),
    }

    assert normalize(result) == expected
    assert_no_duplicates(result)


def test_two_duplicates():
    nums = [1, 1]
    result = subsets_with_dup(nums)

    expected = {
        (),
        (1,),
        (1, 1),
    }

    assert normalize(result) == expected
    assert_no_duplicates(result)


# ---------- Correctness properties ----------
def test_contains_only_elements_from_input():
    nums = [1, 2, 2]
    result = subsets_with_dup(nums)
    allowed = set(nums)

    for subset in result:
        assert set(subset).issubset(allowed)

def test_expected_count_for_multiset():
    # nums = [1,1,2,2]
    # unique subsets count = (count(1)+1) * (count(2)+1) = 3 * 3 = 9
    nums = [1, 1, 2, 2]
    result = subsets_with_dup(nums)
    assert len(normalize(result)) == 9
    assert_no_duplicates(result)


# ---------- Negative numbers + duplicates ----------
def test_negative_duplicates():
    nums = [-1, -1, 0]
    result = subsets_with_dup(nums)

    expected = {
        (),
        (-1,),
        (-1, -1),
        (0,),
        (-1, 0),
        (-1, -1, 0),
    }

    assert normalize(result) == expected
    assert_no_duplicates(result)


# ---------- Input immutability ----------
def test_input_not_modified():
    nums = [1, 2, 2]
    original = nums[:]
    subsets_with_dup(nums)
    assert nums == original