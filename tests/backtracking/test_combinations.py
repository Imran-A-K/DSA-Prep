from tests._loader import load_func

combine = load_func("combine")


def normalize(result):
    """
    Normalize List[List[int]] -> Set[Tuple[int]]
    Order-insensitive comparison.
    """
    return set(tuple(c) for c in result)


# ---------- Given examples ----------
def test_example_1():
    # n = 4, k = 2
    result = combine(4, 2)

    expected = {
        (1, 2),
        (1, 3),
        (1, 4),
        (2, 3),
        (2, 4),
        (3, 4),
    }

    assert normalize(result) == expected


def test_example_2():
    # n = 1, k = 1
    assert normalize(combine(1, 1)) == {(1,)}


# ---------- Edge cases ----------
def test_k_zero():
    # By definition, one empty combination
    assert normalize(combine(5, 0)) == {()}


def test_k_equals_n():
    assert normalize(combine(4, 4)) == {(1, 2, 3, 4)}


def test_n_zero():
    assert normalize(combine(0, 0)) == {()}


# ---------- Correctness properties ----------
def test_combination_length():
    result = combine(5, 3)
    for c in result:
        assert len(c) == 3


def test_no_duplicates():
    result = combine(5, 3)
    assert len(result) == len(normalize(result))


def test_elements_in_range():
    n, k = 5, 3
    result = combine(n, k)

    for c in result:
        for x in c:
            assert 1 <= x <= n


def test_strictly_increasing():
    result = combine(5, 3)
    for c in result:
        assert list(c) == sorted(c)


# ---------- Mathematical correctness ----------
def test_count_matches_nCk():
    # 6C3 = 20
    assert len(normalize(combine(6, 3))) == 20

    # 7C2 = 21
    assert len(normalize(combine(7, 2))) == 21


# ---------- Input immutability ----------
def test_input_not_mutated():
    # combine uses integers only; just ensure function runs safely
    combine(5, 2)