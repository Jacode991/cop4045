# p5_Steinberg_Jacob.py
# Jacob Steinberg
# z23812823
# COP 4045 - Python Programming
# Problem 5 - Recursion


        return digits[n]
    return strB(n // base, base) + digits[n % base]


def test_strB() -> None:
    """Run four tests for the recursive base conversion."""
    testif(strB(31, 2) == "11111", "Convert to base 2")
    testif(strB(255, 16) == "FF", "Convert to base 16")
    testif(strB(81, 3) == "10000", "Convert to base 3")
    testif(strB(26, 26) == "10", "Convert to base 26")


# Part C: Recursive binomial coefficient with memoization

def Cnk_m(n: int, k: int,
          memo: dict[tuple[int, int], int] | None = None) -> int:
    """Return n choose k using recursion and a dictionary cache.

    Preconditions: 0 <= k <= n. The memo dictionary saves earlier results.
    """
    if n < 0 or k < 0 or k > n:
        raise ValueError("Require 0 <= k <= n")

    if memo is None:
        memo = {}

    if k == 0 or k == n:
        return 1

    key = (n, k)
    if key not in memo:
        memo[key] = (Cnk_m(n - 1, k - 1, memo) +
                     Cnk_m(n - 1, k, memo))

    return memo[key]


def test_Cnk_m() -> None:
    """Run four tests for the memoized binomial coefficient."""
    testif(Cnk_m(5, 2) == 10, "5 choose 2")
    testif(Cnk_m(8, 3) == 56, "8 choose 3")
    testif(Cnk_m(10, 5) == 252, "10 choose 5")
    testif(Cnk_m(12, 0) == 1, "12 choose 0")


def run_Cnk(n: int = 30, k: int = 15) -> None:
    """Display an example result from the memoized Cnk_m function."""
    print(f"Cnk_m({n}, {k}) = {Cnk_m(n, k)}")


# Part D: Make matching pairs using recursion and an accumulator

def make_pairs(seq1: list, seq2: list,
               pairs: list[tuple] | None = None,
               index: int = 0) -> list[tuple]:
    """Pair matching indexes, stopping at the shorter list.

    The pairs list is an accumulator passed into each recursive call.
    """
    if pairs is None:
        pairs = []

    if index >= len(seq1) or index >= len(seq2):
        return pairs

    pairs.append((seq1[index], seq2[index]))
    return make_pairs(seq1, seq2, pairs, index + 1)


def test_make_pairs() -> None:
    """Run five tests, including cases with empty lists."""
    testif(make_pairs([1, 2], [3, 4]) == [(1, 3), (2, 4)],
           "Lists of equal length")
    testif(make_pairs([1], [3, 4]) == [(1, 3)],
           "First list is shorter")
    testif(make_pairs([1, 2], [3]) == [(1, 3)],
           "Second list is shorter")
    testif(make_pairs([], [1, 2]) == [], "First list is empty")
    testif(make_pairs([1, 2], []) == [], "Second list is empty")


def main() -> None:
    """Run the required tests and display both recursive leaf drawings."""
    print("Jacob Steinberg")
    print("FAU Student ID: z23812823")
    print("COP 4045 - Problem 5")

    print("\nTesting strB:")
    test_strB()
    print("Example: strB(2026, 16) =", strB(2026, 16))

    print("\nTesting Cnk_m:")
    test_Cnk_m()
    run_Cnk(30, 15)

    print("\nTesting make_pairs:")
    test_make_pairs()
    print("Example:", make_pairs([10, 20, 30], ["a", "b"]))

    print("\nOpening the turtle window with both leaves...")
    screen = turtle.Screen()
    screen.setup(900, 620)
    screen.title("Problem 5 - Straight and Curved Recursive Leaves")
    screen.tracer(0)

    draw_leaf_straight(6, 120)
    draw_leaf_curved(6, 120)

    turtle.pencolor("black")
    turtle.goto(-225, -280)
    turtle.write("Straight leaf (6, 120)", align="center",
                 font=("Arial", 12, "normal"))
    turtle.goto(215, -280)
    turtle.write("Curved leaf (6, 120)", align="center",
                 font=("Arial", 12, "normal"))

    screen.update()
    print("Take screenshots of the leaves and your console output.")
    turtle.done()


if __name__ == "__main__":
    main()

