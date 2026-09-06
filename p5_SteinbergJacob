import string


def caesar_cipher(text, shift):
    result = ""
    alphabet_lower = string.ascii_lowercase
    alphabet_upper = string.ascii_uppercase

    for ch in text:
        if ch in alphabet_lower:
            index = alphabet_lower.index(ch)
            new_index = (index + shift) % 26
            result += alphabet_lower[new_index]

        elif ch in alphabet_upper:
            index = alphabet_upper.index(ch)
            new_index = (index + shift) % 26
            result += alphabet_upper[new_index]

        else:
            result += ch

    return result


def caesar_decipher(cyphertext, shift):
    return caesar_cipher(cyphertext, -shift)


def letter_frequency(text):
    frequencies = {}

    for letter in string.ascii_lowercase:
        frequencies[letter] = 0

    for ch in text:
        ch = ch.lower()

        if ch in string.ascii_lowercase:
            frequencies[ch] += 1

    return frequencies


def main():
    while True:
        print()
        print("Caesar Cipher Menu")
        print("1. Encrypt a message")
        print("2. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            message = input("Enter a message: ")
            shift = int(input("Enter shift value: "))

            ciphered = caesar_cipher(message, shift)
            deciphered = caesar_decipher(ciphered, shift)
            frequencies = letter_frequency(message)

            print()
            print("Ciphered text:")
            print(ciphered)

            print()
            print("Letter frequencies:")

            for letter in frequencies:
                print(letter, ":", frequencies[letter])

            print()
            print("Deciphered text:")
            print(deciphered)

        elif choice == "2":
            print("Program ended.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
