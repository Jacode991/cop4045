# p5_Steinberg_Jacob.py
# Jacob Steinberg
# z23812823
# COP 4045 - Python Programming
# Problem 5 - Recursion


import math
import turtle


def testif(condition: bool, description: str) -> None:
    if condition:
        print("PASS:", description)
    else:
        print("FAIL:", description)


def leaf_point(x: float, y: float, length: float, width: float,
               bend: float, height: float, side: int) -> tuple[float, float]:
    center_x = x + bend * height * height
    edge_x = side * width * math.sin(math.pi * height)
    return center_x + edge_x, y + length * height


def draw_veins(level: int, start: float, end: float, x: float,
               y: float, length: float, width: float, bend: float) -> None:
    if level == 0:
        return

    middle = (start + end) / 2
    center = leaf_point(x, y, length, width, bend, middle, 0)

    edge_height = min(middle + 0.05, 1.0)
    for side in (-1, 1):
        edge = leaf_point(x, y, length, width, bend, edge_height, side)
        turtle.penup()
        turtle.goto(center)
        turtle.pendown()
        turtle.goto(edge)

    draw_veins(level - 1, start, middle, x, y, length, width, bend)
    draw_veins(level - 1, middle, end, x, y, length, width, bend)


def draw_leaf(level: int, stem: float, x: float, bend: float) -> None:
    if level < 1 or stem <= 0:
        raise ValueError("Level and stem length must be positive")

    y = -130.0
    blade_length = 225.0
    width = 85.0
    steps = 40

    turtle.hideturtle()
    turtle.speed(0)
    turtle.pencolor("darkgreen")

    turtle.penup()
    turtle.goto(x, y - stem)
    turtle.setheading(90)
    turtle.pendown()
    turtle.pensize(4)
    turtle.goto(x, y)

    turtle.pensize(2)
    turtle.fillcolor("lightgreen")
    turtle.begin_fill()
    for i in range(steps + 1):
        point = leaf_point(x, y, blade_length, width, bend, i / steps, 1)
        turtle.goto(point)
    for i in range(steps, -1, -1):
        point = leaf_point(x, y, blade_length, width, bend, i / steps, -1)
        turtle.goto(point)
    turtle.end_fill()

    turtle.pensize(3)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for i in range(1, steps + 1):
              return digits[n]
    return strB(n // base, base) + digits[n % base]

def strB(n: int, base: int = 10) -> str:
    """Convert a nonnegative integer to a different base using recursion."""
    if n < 0 or base < 2 or base > 26:
        raise ValueError("Invalid number or base")

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if n < base:
        return digits[n]

    return strB(n // base, base) + digits[n % base]

def test_strB() -> None:
    """Run four tests for the recursive base conversion."""
    testif(strB(31, 2) == "11111", "Convert to base 2")
    testif(strB(255, 16) == "FF", "Convert to base 16")
    testif(strB(81, 3) == "10000", "Convert to base 3")
    testif(strB(26, 26) == "10", "Convert to base 26")

def Cnk_m(n: int, k: int,
          memo: dict[tuple[int, int], int] | None = None) -> int:
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
    testif(Cnk_m(5, 2) == 10, "5 choose 2")
    testif(Cnk_m(8, 3) == 56, "8 choose 3")
    testif(Cnk_m(10, 5) == 252, "10 choose 5")
    testif(Cnk_m(12, 0) == 1, "12 choose 0")


def run_Cnk(n: int = 30, k: int = 15) -> None:
    print(f"Cnk_m({n}, {k}) = {Cnk_m(n, k)}")

def make_pairs(seq1: list, seq2: list,
               pairs: list[tuple] | None = None,
               index: int = 0) -> list[tuple]:
    if pairs is None:
        pairs = []

    if index >= len(seq1) or index >= len(seq2):
        return pairs

    pairs.append((seq1[index], seq2[index]))
    return make_pairs(seq1, seq2, pairs, index + 1)


def test_make_pairs() -> None:
    testif(make_pairs([1, 2], [3, 4]) == [(1, 3), (2, 4)],
           "Lists of equal length")
    testif(make_pairs([1], [3, 4]) == [(1, 3)],
           "First list is shorter")
    testif(make_pairs([1, 2], [3]) == [(1, 3)],
           "Second list is shorter")
    testif(make_pairs([], [1, 2]) == [], "First list is empty")
    testif(make_pairs([1, 2], []) == [], "Second list is empty")


def main() -> None:
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
