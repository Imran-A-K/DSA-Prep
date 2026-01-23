from tests._loader import load_func

find_winner = load_func("find_winner")


# --------- Given examples ----------
def test_example_1():
    assert find_winner(5, 2) == 3

def test_example_2():
    assert find_winner(6, 5) == 1


# --------- Edge cases ----------
def test_single_friend():
    assert find_winner(1, 1) == 1

def test_k_equals_1_always_last_is_n():
    # If k=1, you remove current person each time -> winner is n
    for n in [1, 2, 5, 10, 50]:
        assert find_winner(n, 1) == n

def test_k_equals_n_small():
    # Known Josephus results for k=n cases
    # n=2,k=2 -> winner 1
    assert find_winner(2, 2) == 1
    # n=3,k=3 -> winner 2
    assert find_winner(3, 3) == 2
    # n=4,k=4 -> winner 2
    assert find_winner(4, 4) == 2
    # n=5,k=5 -> winner 2
    assert find_winner(5, 5) == 2


# --------- Known Josephus checkpoints (common for validation) ----------
def test_known_values_k2():
    # For k=2, winner is 2*(n - 2^floor(log2 n)) + 1
    assert find_winner(2, 2) == 1
    assert find_winner(3, 2) == 3
    assert find_winner(4, 2) == 1
    assert find_winner(5, 2) == 3
    assert find_winner(7, 2) == 7
    assert find_winner(8, 2) == 1
    assert find_winner(10, 2) == 5


def test_known_values_misc():
    assert find_winner(7, 3) == 4
    assert find_winner(10, 3) == 4
    assert find_winner(10, 4) == 5
    assert find_winner(12, 5) == 1


# --------- Constraint-edge smoke tests ----------
def test_upper_bound_smoke():
    # Should run fast and return a valid index
    ans = find_winner(500, 500)
    assert 1 <= ans <= 500

def test_upper_bound_k1_smoke():
    assert find_winner(500, 1) == 500