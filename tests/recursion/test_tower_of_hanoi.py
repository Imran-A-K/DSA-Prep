import io
import sys
from tests._loader import load_func

toh = load_func("toh")


def capture_output(func, *args):
    """
    Utility to capture stdout while running a function.
    """
    captured = io.StringIO()
    old_stdout = sys.stdout
    sys.stdout = captured
    try:
        result = func(*args)
    finally:
        sys.stdout = old_stdout
    return captured.getvalue(), result


# ---------- Basic correctness ----------
def test_n_1():
    output, moves = capture_output(toh, 1, 1, 3, 2)
    assert moves == 1
    assert output.strip() == "move disk 1 from rod 1 to rod 3"


def test_n_2():
    output, moves = capture_output(toh, 2, 1, 3, 2)
    lines = output.strip().splitlines()

    assert moves == 3
    assert len(lines) == 3
    assert lines[0] == "move disk 1 from rod 1 to rod 2"
    assert lines[1] == "move disk 2 from rod 1 to rod 3"
    assert lines[2] == "move disk 1 from rod 2 to rod 3"


def test_n_3():
    output, moves = capture_output(toh, 3, 1, 3, 2)
    lines = output.strip().splitlines()

    expected = [
        "move disk 1 from rod 1 to rod 3",
        "move disk 2 from rod 1 to rod 2",
        "move disk 1 from rod 3 to rod 2",
        "move disk 3 from rod 1 to rod 3",
        "move disk 1 from rod 2 to rod 1",
        "move disk 2 from rod 2 to rod 3",
        "move disk 1 from rod 1 to rod 3",
    ]

    assert moves == 7
    assert lines == expected


# ---------- Mathematical invariant ----------
def test_move_count_formula():
    for n in range(1, 6):
        _, moves = capture_output(toh, n, 1, 3, 2)
        assert moves == (1 << n) - 1  # 2^n - 1


# ---------- Output format ----------
def test_output_format():
    output, _ = capture_output(toh, 3, 1, 3, 2)
    for line in output.strip().splitlines():
        assert line.startswith("move disk ")
        assert " from rod " in line
        assert " to rod " in line


# ---------- Larger n smoke test ----------
def test_n_5_smoke():
    output, moves = capture_output(toh, 5, 1, 3, 2)
    assert moves == 31
    assert len(output.strip().splitlines()) == 31