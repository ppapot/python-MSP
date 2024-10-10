import unittest
from palyndrome import ispalyndrome

class TestIsPalyndrome(unittest.TestCase):

    def test_empty_string(self):
        self.assertTrue(ispalyndrome(''))
    pass

    def test_single_character_string(self):
        self.assertTrue(ispalyndrome('a'))

    def test_even_length_palindrome(self):
        self.assertTrue(ispalyndrome("abba"))

    def test_odd_length_palindrome(self):
        self.assertTrue(ispalyndrome("racecar"))

    def test_mixed_case_palindrome(self):
        self.assertTrue(ispalyndrome("RaceCar"))


    def test_ispalyndrome_with_spaces(self):
        self.assertTrue(ispalyndrome("A man a plan a canal Panama"))

    def test_ispalyndrome_with_punctuation(self):
        self.assertTrue(ispalyndrome("A man, a plan, a canal, Panama!"))


    def test_ispalyndrome_with_spaces_not_a_palindrome(self):
        self.assertFalse(ispalyndrome("this is not a palindrome"))

    def test_mixed_case_non_palindrome(self):
        self.assertFalse(ispalyndrome('OpenAI'))
        
    def test_non_palindrome_string(self):
        self.assertFalse(ispalyndrome("hello"))

if __name__ == '__main__':
    unittest.main()
