from tests._loader import load_func

combination_sum = load_func("combination_sum")


def normalize(result):
    """
    Normalize List[List[int]] -> Set[Tuple[int]]
    - Sort each combination
    - Convert to tuple
    - Convert outer to set for order-insensitive comparison
    """
    return set(tuple(sorted(c)) for c in result)


def assert_valid_combos(candidates, target, result):
    cand_set = set(candidates)
    for combo in result:
        assert sum(combo) == target
        for x in combo:
            assert x in cand_set


# ---------- Given examples ----------
def test_example_1():
    candidates = [2, 3, 6, 7]
    target = 7
    result = combination_sum(candidates, target)

    expected = {
        (7,),
        (2, 2, 3),
    }

    assert normalize(result) == expected
    assert_valid_combos(candidates, target, result)


def test_example_2():
    candidates = [2, 3, 5]
    target = 8
    result = combination_sum(candidates, target)

    expected = {
        (2, 2, 2, 2),
        (2, 3, 3),
        (3, 5),
    }

    assert normalize(result) == expected
    assert_valid_combos(candidates, target, result)


def test_example_3():
    candidates = [2]
    target = 1
    result = combination_sum(candidates, target)

    assert normalize(result) == set()
    assert_valid_combos(candidates, target, result)


# ---------- Edge cases ----------
def test_target_zero():
    # By common convention: one way to make 0 is choose nothing
    candidates = [1, 2, 3]
    result = combination_sum(candidates, 0)
    assert normalize(result) == {()}

def test_single_candidate_exact():
    candidates = [7]
    target = 7
    result = combination_sum(candidates, target)
    assert normalize(result) == {(7,)}

def test_single_candidate_multiple():
    candidates = [3]
    target = 9
    result = combination_sum(candidates, target)
    assert normalize(result) == {(3, 3, 3)}


# ---------- Correctness properties ----------
def test_no_duplicates_in_output():
    candidates = [2, 3, 5]
    target = 8
    result = combination_sum(candidates, target)
    assert len(result) == len(normalize(result))


def test_combos_use_only_candidates_and_hit_target():
    candidates = [2, 3, 6, 7]
    target = 7
    result = combination_sum(candidates, target)
    assert_valid_combos(candidates, target, result)


def test_input_not_modified():
    candidates = [2, 3, 6, 7]
    original = candidates[:]
    combination_sum(candidates, 7)
    assert candidates == original


# ---------- Additional validation ----------
def test_larger_target_small_candidates():
    candidates = [2, 3]
    target = 10
    result = combination_sum(candidates, target)

    # Ways:
    # 2*5
    # 2*2 + 3*2 (4 + 6)
    # 2*1 + 3*? -> 2 + 8 not possible with 3s
    expected = {
        (2, 2, 2, 2, 2),
        (2, 2, 3, 3),
    }

    assert normalize(result) == expected
    assert_valid_combos(candidates, target, result)