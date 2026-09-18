# Jacob Steinberg
# COP 4045
# Homework 2 - Problem 2
# Comprehensions

def main():
    print("Jacob Steinberg")
    print("COP 4045 - Homework 2 - Problem 2")
    print()

    #Part A
    print("Part A")

    answer_a = [(a, b, c, d)
                for a in range(1, 11)
                for b in range(1, 11)
                for c in range(1, 11)
                for d in range(1, 11)
                if len({a, b, c, d}) == 4
                and a ** 2 + b ** 2 == c ** 2 + d ** 2]

    print(answer_a)
    print()

    #Part B
    print("Part B")

    words = ["One", "SEVEN", "three", "two", "Ten"]

    answer_b = [(word.lower(), len(word))
                for word in words
                if len(word) < 5]

    print(answer_b)
    print()

    #Part C
    print("Part C")

    names = ["Christopher Ashton Kutcher",
              "Elizabeth Stamatina fey"]

    answer_c = [name.split()[0] + " "
                + name.split()[1][0] + ". "
                + name.split()[2]
                for name in names]

    print(answer_c)
    print()

    #Part D
    print("Part D")

    lst1 = ["Spam", "Trams", "Elbows", "Tops", "Astral"]
    lst2 = ["Bowels", "Sample", "Altars", "Stop", "Course", "Smart"]

    answer_d = [(w1, w2)
                for w1 in lst1
                for w2 in lst2
                if sorted(w1.lower()) == sorted(w2.lower())]

    print(answer_d)
    print()

    #Part E
    print("Part E")

    s = ["one", "two", "three"]

    answer_e = {word: len(word) for word in s}

    print(answer_e)
    print()

    #Part F
    print("Part F")

    text = "Hello World"

    answer_f = {i: c
                for i, c in enumerate(text)
                if c.lower() in "aeiou"}

    print(answer_f)

if __name__ == "__main__":
    main()
  
