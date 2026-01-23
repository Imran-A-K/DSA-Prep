from tests._loader import load_func

kth_grammar = load_func("kth_symbol")


# --------- Provided examples ----------
def test_example_1():
    assert kth_grammar(1, 1) == 0

def test_example_2():
    assert kth_grammar(2, 1) == 0

def test_example_3():
    assert kth_grammar(2, 2) == 1


# --------- Base / small n sanity ----------
def test_row_3_all_k():
    # row 3 = 0110
    assert kth_grammar(3, 1) == 0
    assert kth_grammar(3, 2) == 1
    assert kth_grammar(3, 3) == 1
    assert kth_grammar(3, 4) == 0

def test_row_4_all_k():
    # row 4 = 01101001
    expected = [0, 1, 1, 0, 1, 0, 0, 1]
    for k, val in enumerate(expected, start=1):
        assert kth_grammar(4, k) == val


# --------- Edge cases around boundaries ----------
def test_first_symbol_always_zero():
    for n in range(1, 11):
        assert kth_grammar(n, 1) == 0

def test_last_symbol_pattern():
    # last symbol of row n (k = 2^(n-1)) alternates: n odd -> 0, n even -> 1
    for n in range(1, 11):
        k_last = 1 << (n - 1)
        expected = 0 if (n % 2 == 1) else 1
        assert kth_grammar(n, k_last) == expected


# --------- Parent/child relationship checks ----------
def test_pair_rule_same_parent():
    # In any row n>1, positions (2p-1, 2p) come from parent at p:
    # parent 0 -> (0,1), parent 1 -> (1,0)
    n = 6
    for p in [1, 2, 3, 10, 16]:
        left = kth_grammar(n, 2 * p - 1)
        right = kth_grammar(n, 2 * p)
        assert (left, right) in [(0, 1), (1, 0)]
        assert left != right


# --------- Deeper values (avoid building the whole string) ----------
def test_known_values_deeper():
    # These are consistent known points derived from recursion/parity logic.
    assert kth_grammar(5, 1) == 0
    assert kth_grammar(5, 8) == 1
    assert kth_grammar(6, 16) == 0
    assert kth_grammar(7, 32) == 1


# --------- Max-ish constraints smoke tests ----------
def test_large_n_small_k():
    assert kth_grammar(30, 1) == 0

def test_large_n_last_k():
    k_last = 1 << 29
    # n=30 even -> last symbol should be 1
    assert kth_grammar(30, k_last) == 1