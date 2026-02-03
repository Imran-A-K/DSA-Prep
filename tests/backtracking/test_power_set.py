from tests._loader import load_func

subsets = load_func("power_set")


def normalize(result):
    """
    Normalize List[List[int]] -> Set[Tuple[int]]
    - Sort each subset
    - Convert to tuple so it can go into a set
    """
    return set(tuple(sorted(s)) for s in result)


# ---------- Basic examples ----------
def test_example_1():
    nums = [1, 2, 3]
    result = subsets(nums)

    expected = {
        (),        # []
        (1,),
        (2,),
        (3,),
        (1, 2),
        (1, 3),
        (2, 3),
        (1, 2, 3),
    }

    assert normalize(result) == expected


def test_example_2():
    nums = [0]
    result = subsets(nums)
    assert normalize(result) == {(), (0,)}


# ---------- Edge cases ----------
def test_empty():
    # By definition, subsets([]) = [[]]
    assert normalize(subsets([])) == {()}

def test_two_elements():
    nums = [5, 6]
    expected = {(), (5,), (6,), (5, 6)}
    assert normalize(subsets(nums)) == expected


# ---------- Correctness properties ----------
def test_count_is_power_of_two():
    nums = [1, 2, 3, 4]
    result = subsets(nums)
    assert len(normalize(result)) == 16  # 2^4

def test_no_duplicates_in_output():
    nums = [1, 2, 3]
    result = subsets(nums)
    norm = normalize(result)
    assert len(result) == len(norm)

def test_every_subset_is_valid():
    nums = [2, 4, 6]
    result = subsets(nums)
    nums_set = set(nums)

    for s in result:
        # every element in subset must come from nums
        assert set(s).issubset(nums_set)


# ---------- Input immutability ----------
def test_input_not_modified():
    nums = [1, 2, 3]
    original = nums[:]
    subsets(nums)
    assert nums == original


# ---------- Negative numbers ----------
def test_negative_numbers():
    nums = [-1, 0, 1]
    result = subsets(nums)

    expected = {
        (),
        (-1,),
        (0,),
        (1,),
        (-1, 0),
        (-1, 1),
        (0, 1),
        (-1, 0, 1),
    }

    assert normalize(result) == expected