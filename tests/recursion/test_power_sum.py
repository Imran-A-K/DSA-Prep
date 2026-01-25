from tests._loader import load_func

power_sum = load_func("power_sum")


# ---------- Given examples ----------
def test_example_1():
    # [2,3,[4,1,2]] = 2 + 3 + (4+1+2)^2 = 5 + 7^2 = 54
    assert power_sum([2, 3, [4, 1, 2]]) == 54

def test_example_2():
    # [1,2,[7,[3,4],2]]
    # = 1 + 2 + ( 7 + (3+4)^3 + 2 )^2
    # = 3 + ( 7 + 343 + 2 )^2
    # = 3 + 352^2 = 3 + 123904 = 123907
    assert power_sum([1, 2, [7, [3, 4], 2]]) == 123907


# ---------- Base cases ----------
def test_single_integer():
    assert power_sum([5]) == 5

def test_flat_array_multiple_ints():
    assert power_sum([1, 2, 3, 4]) == 10

def test_single_nested_array_level_2():
    # [ [1,2,3] ] -> (1+2+3)^2 = 6^2 = 36
    assert power_sum([[1, 2, 3]]) == 36


# ---------- Multiple nested arrays at same depth ----------
def test_two_nested_arrays_same_level():
    # [1, [2], [3]] = 1 + (2)^2 + (3)^2 = 1 + 4 + 9 = 14
    assert power_sum([1, [2], [3]]) == 14

def test_nested_and_ints_mixed():
    # [2, [1,1], 3] = 2 + (1+1)^2 + 3 = 2 + 4 + 3 = 9
    assert power_sum([2, [1, 1], 3]) == 9


# ---------- Deeper nesting correctness ----------
def test_depth_3_simple():
    # [[ [1] ]] : depth(outer)=1, middle=2, inner=3
    # inner: (1)^3 = 1
    # middle: (1)^2 = 1
    # outer: 1
    assert power_sum([[[1]]]) == 1

def test_depth_3_nontrivial():
    # [1, [2, [3]]]
    # = 1 + ( 2 + (3)^3 )^2
    # = 1 + ( 2 + 27 )^2
    # = 1 + 29^2 = 842
    assert power_sum([1, [2, [3]]]) == 842

def test_depth_4_small():
    # [ [ [ [2] ] ] ] -> ( ( (2^4)^3 )^2 )? No: apply definition consistently:
    # innermost list at depth 4: (2)^4 = 16
    # depth 3 list: (16)^3 = 4096
    # depth 2 list: (4096)^2 = 16777216
    # outer depth 1: 16777216
    assert power_sum([[[[2]]]]) == 16777216


# ---------- Zeros / negatives ----------
def test_with_zero():
    # [0, [0]] = 0 + (0)^2 = 0
    assert power_sum([0, [0]]) == 0

def test_with_negative_numbers():
    # [-1, [2, -3]] = -1 + (2 + -3)^2 = -1 + (-1)^2 = 0
    assert power_sum([-1, [2, -3]]) == 0

def test_negative_inside_deeper():
    # [1, [2, [-1, 1]]]
    # = 1 + ( 2 + (-1+1)^3 )^2
    # = 1 + ( 2 + 0 )^2
    # = 5
    assert power_sum([1, [2, [-1, 1]]]) == 5


# ---------- Property sanity checks ----------
def test_equivalent_flat_no_nesting():
    # If no nested lists exist, power_sum should be regular sum
    arr = [10, -5, 2, 3]
    assert power_sum(arr) == sum(arr)

def test_nested_never_empty_assumption_smoke():
    # Just a smoke test with minimal non-empty nesting
    assert power_sum([1, [2]]) == 1 + (2**2)