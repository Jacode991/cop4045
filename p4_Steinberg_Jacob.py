# p4_Steinberg_Jacob.py
# Jacob Steinberg
# z23812823
# COP 4045 - Python Programming
# Homework 3 - Problem 4

def ed_read(filename: str, from_pos: int = 0,
            to_pos: int = -1) -> str:
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    if from_pos < 0 or from_pos > len(text):
        raise IndexError("Invalid starting position")

    if to_pos == -1:
        to_pos = len(text)

    if to_pos > len(text):
        raise IndexError("Ending position exceeds file length")

    if to_pos < from_pos:
        raise ValueError("Ending position is before starting position")

    return text[from_pos:to_pos]


def ed_find(filename: str, search_str: str) -> list[int]:
    if search_str == "":
        raise ValueError("Search string cannot be empty")

    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    positions = []
    start = 0

    while True:
        index = text.find(search_str, start)

        if index == -1:
            break

        positions.append(index)
        start = index + 1

    return positions


def ed_replace(filename: str, search_str: str,
               replace_with: str, occurrence: int = -1) -> int:
    if search_str == "":
        raise ValueError("Search string cannot be empty")

    if occurrence < -1:
        raise ValueError("Invalid occurrence number")

    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    if occurrence == -1:
        count = text.count(search_str)
        new_text = text.replace(search_str, replace_with)

    else:
        count = 0
        start = 0
        position = -1

        for i in range(occurrence + 1):
            position = text.find(search_str, start)

            if position == -1:
                return 0

            start = position + len(search_str)

        new_text = (text[:position] + replace_with +
                    text[position + len(search_str):])
        count = 1

    if count > 0:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(new_text)

    return count

filename = "file1.txt"

print(ed_append(filename, "0123456789"))
print(ed_append(filename, "0123456789"))

print(ed_read(filename))


import os


def testif(condition: bool, message: str) -> None:
    """Print PASS if a test succeeds, or FAIL if it does not."""
    if condition:
        print("PASS:", message)
    else:
        print("FAIL:", message)


def test_ed_find() -> None:
    """Test finding strings inside a text file."""
    filename = "test_find.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write("01234567890123456789")

    result = ed_find(filename, "345")
    testif(result == [3, 13], "Find multiple matches")

    result = ed_find(filename, "356")
    testif(result == [], "Find missing text")

    result = ed_find(filename, "012")
    testif(result == [0, 10], "Find text at the beginning")

    with open(filename, "w", encoding="utf-8") as file:
        file.write("banana")

    result = ed_find(filename, "ana")
    testif(result == [1, 3], "Find overlapping matches")

    os.remove(filename)


def test_ed_replace() -> None:
    """Test replacing strings inside a text file."""
    filename = "test_replace.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write("cat dog cat")

    result = ed_replace(filename, "cat", "bird")
    text = ed_read(filename)
    testif(result == 2 and text == "bird dog bird",
           "Replace all matches")
    with open(filename, "w", encoding="utf-8") as file:
        file.write("cat dog cat")

    result = ed_replace(filename, "cat", "bird", 1)
    text = ed_read(filename)
    testif(result == 1 and text == "cat dog bird",
           "Replace second match")
    result = ed_replace(filename, "cat", "bird", 5)
    text = ed_read(filename)
    testif(result == 0 and text == "cat dog bird",
           "Leave file unchanged if occurrence is missing")
  
    result = ed_replace(filename, "fish", "bird")
    testif(result == 0, "Replace missing text")

    os.remove(filename)


def main() -> None:
    """Demonstrate the text editor functions and run tests."""
    print("Jacob Steinberg")
    print("FAU Student ID: z23812823")
    print("COP 4045 - Python Programming")
    print("Homework 4 - Problem 4")
    print()

    filename = "p4_demo.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write("")

    print("Testing ed_append:")
    print(ed_append(filename, "0123456789"))
    print(ed_append(filename, "0123456789"))

    print("\nTesting ed_read:")
    print(ed_read(filename, 3, 9))
    print(ed_read(filename, 3))

    print("\nTesting ed_find:")
    print(ed_find(filename, "345"))
    print(ed_find(filename, "356"))

    print("\nTesting ed_replace:")
    print(ed_replace(filename, "345", "ABCDE", 1))
    print(ed_read(filename))

    with open(filename, "w", encoding="utf-8") as file:
        file.write("01234567890123456789")

    print(ed_replace(filename, "345", "ABCDE"))
    print(ed_read(filename))

    print("\nRunning unit tests:")
    test_ed_find()
    test_ed_replace()

    print("\nProgram finished.")


if __name__ == "__main__":
    main()

