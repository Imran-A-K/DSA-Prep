from tests._loader import load_func

is_monotonic = load_func("is_monotonic")


# ---------- Basic examples ----------
def test_increasing_with_duplicates():
    assert is_monotonic([1, 2, 2, 3]) is True

def test_decreasing_with_duplicates():
    assert is_monotonic([6, 5, 4, 4]) is True

def test_not_monotonic():
    assert is_monotonic([1, 3, 2]) is False


# ---------- Edge cases ----------
def test_single_element():
    assert is_monotonic([5]) is True

def test_all_equal():
    assert is_monotonic([2, 2, 2, 2]) is True

def test_two_elements_increasing():
    assert is_monotonic([1, 2]) is True

def test_two_elements_decreasing():
    assert is_monotonic([2, 1]) is True

def test_empty_erray():
    assert is_monotonic([]) is True


# ---------- Negative numbers ----------
def test_negative_increasing():
    assert is_monotonic([-5, -3, -3, -1]) is True

def test_negative_decreasing():
    assert is_monotonic([-1, -3, -5]) is True

def test_negative_not_monotonic():
    assert is_monotonic([-5, -1, -3]) is False


# ---------- Mixed signs ----------
def test_mixed_sign_increasing():
    assert is_monotonic([-3, -1, 0, 2, 4]) is True

def test_mixed_sign_decreasing():
    assert is_monotonic([4, 2, 0, -1, -3]) is True

def test_mixed_sign_not_monotonic():
    assert is_monotonic([-1, 2, -3]) is False


# ---------- Tricky transitions ----------
def test_flat_then_increase():
    assert is_monotonic([3, 3, 3, 4]) is True

def test_flat_then_decrease():
    assert is_monotonic([3, 3, 2, 2]) is True

def test_increase_then_flat_then_decrease():
    assert is_monotonic([1, 2, 2, 1]) is False

