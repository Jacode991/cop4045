import unittest
from p5_yourname import caesar_cipher, caesar_decipher, letter_frequency


class TestCaesarCipher(unittest.TestCase):

    def test_basic_cipher(self):
        result = caesar_cipher("abc", 3)
        self.assertEqual(result, "def")

    def test_uppercase(self):
        result = caesar_cipher("ABC", 2)
        self.assertEqual(result, "CDE")

    def test_wraparound(self):
        result = caesar_cipher("xyz", 3)
        self.assertEqual(result, "abc")

    def test_spaces_and_symbols(self):
        result = caesar_cipher("Hello World!", 1)
        self.assertEqual(result, "Ifmmp Xpsme!")

    def test_decipher(self):
        result = caesar_decipher("Ifmmp", 1)
        self.assertEqual(result, "Hello")

    def test_cipher_and_decipher(self):
        original = "Python Programming"
        encrypted = caesar_cipher(original, 5)
        decrypted = caesar_decipher(encrypted, 5)

        self.assertEqual(decrypted, original)

    def test_letter_frequency(self):
        result = letter_frequency("Hello")

        self.assertEqual(result["h"], 1)
        self.assertEqual(result["e"], 1)
        self.assertEqual(result["l"], 2)
        self.assertEqual(result["o"], 1)

    def test_frequency_ignores_case(self):
        result = letter_frequency("AaA")

        self.assertEqual(result["a"], 3)

    def test_frequency_ignores_symbols(self):
        result = letter_frequency("A1! b2?")

        self.assertEqual(result["a"], 1)
        self.assertEqual(result["b"], 1)


if __name__ == "__main__":
    unittest.main()
