# p1_Steinberg_Jacob.py
# Jacob Steinberg
# z23812823
# COP 4045 - Python Programming
# Homework 3 - Problem 1

from __future__ import annotations

from collections.abc import Sequence
from numbers import Real
from types import NotImplementedType

class NVector:
    def __init__(self, *values: Real | Sequence[Real] | NVector) -> None:
      if len(values) == 1:
        try:
            self.elements: list[Real] = list(values[0])
        except TypeError as error:
            raise TypeError("One argument must be a sequence") from error
      elif len(values) >= 2:
          self.elements = list(values)
      else:
          raise TypeError("NVector requires at least one argument")
      for value in self.elements:
          if isinstance(value, bool) or not isinstance(value, Real):
              raise TypeError("Vector elements must be real numbers")

    def __len__(self) -> int:
        return len(self.elements)

    def __getitem__(self, index: int) -> Real:
        return self.elements[index]

    def __setitem__(self, index: int, value: Real) -> None:
        if isinstance(value, bool) or not isinstance(value, Real):
            raise TypeError("Vector elements must be real numbers")
        self.elements[index] = value

    def __str__(self) -> str:
        return str(self.elements)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, NVector) and self.elements == other.elements

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    def __add__(self, other: NVector | Real) -> NVector | NotImplementedType:
        if isinstance(other, NVector):
            if len(self) != len(other):
                raise ValueError("Vector dimensions must match")
            return NVector([a + b for a, b in zip(self.elements, other.elements)])
        if isinstance(other, Real) and not isinstance(other, bool):
            return NVector([a + other for a in self.elements])
        return self.__add__(other)

    def __radd__(self, other: Real) -> NVector | NotImplementedType:
        return self.__add__(other)

    def __mul__(self, other: NVector | Real) -> Real | NotImplementedType:
        if isinstance(other, NVector):
            if len(self) != len(other):
                raise ValueError("Vector dimensions must match")
            return sum(a * b for a, b in zip(self.elements, other.elements))
        if isinstance(other, Real) and not isinstance(other, bool):
            return sum(a * other for a in self.elements)
        return NotImplemented

    def __rmul__(self, other: Real) -> Real | NotImplementedType:
        return self.__mul__(other)

    @classmethod
    def zeros(cls, n: int) -> NVector:
        if isinstance(n, bool) or not isinstance(n, int):
            raise TypeError("Dimension must be an integer")
        if n < 0:
            raise ValueError("Dimension cannot be negative")
        return cls([0] * n)


def testif(condition: bool, passed: str, failed: str) -> None:
    """Print a pass/fail message based on a Boolean test condition."""
    print("PASS:", passed) if condition else print("FAIL:", failed)


def main() -> None:
    """Ask for the student's ID, then test the required vector methods."""
    student_id = input("Enter your FAU student ID: ").strip()
    print("FAU Student ID:", student_id or "NOT ENTERED")
    print("NVector tests\n" + "-" * 34)

    values = [3, 0, 1, -1]
    v = NVector(values)
    testif(v == NVector(3, 0, 1, -1), "constructors work", "constructors failed")
    testif(v == NVector((3, 0, 1, -1)), "tuple works", "tuple failed")
    values[0] = 99
    testif(v[0] == 3, "constructor copies list", "list was shared")
    testif(NVector(v) == v, "vector copy works", "vector copy failed")

    testif(len(v) == 4, "len works", "len failed")
    testif(v[1] == 0 and v[-2] == 1, "getitem works", "getitem failed")
    v[2] = 5
    v[-1] = 7
    testif(v[2] == 5 and v[3] == 7, "setitem works", "setitem failed")

    testif(str(v) == "[3, 0, 5, 7]", "str works", "str failed")
    testif(v == NVector([3, 0, 5, 7]), "eq works", "eq failed")
    testif(v != NVector([3, 0, 5, 8]), "ne works", "ne failed")
    testif(v != [3, 0, 5, 7], "different types compare", "type comparison failed")

    a = NVector([3, 0, 1, -1])
    b = NVector([1, 2, 3, 4])
    testif(a + b == NVector([4, 2, 4, 3]), "vector add works", "vector add failed")
    testif(a + 10 == NVector([13, 10, 11, 9]), "number add works", "number add failed")
    testif(10 + a == NVector([13, 10, 11, 9]), "radd works", "radd failed")

    testif(a * b == 2, "dot product works", "dot product failed")
    testif(a * 10 == 30, "scalar mul works", "scalar mul failed")
    testif(10 * a == 30, "rmul works", "rmul failed")

    testif(NVector.zeros(4) == NVector([0, 0, 0, 0]), "zeros works", "zeros failed")

    try:
        v[20] = 5
        testif(False, "", "invalid index did not raise IndexError")
    except IndexError:
        testif(True, "IndexError works", "")

    try:
        a + NVector([1, 2])
        testif(False, "", "different dimensions did not raise ValueError")
    except ValueError:
        testif(True, "ValueError works", "")


if __name__ == "__main__":
    main()
        
