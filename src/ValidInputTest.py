from ValidInput import is_valid_zip, is_valid_date
import unittest


class TestSolution(unittest.TestCase):
    def test_true_zip(self):
        self.assertTrue(is_valid_zip("01234"))
        self.assertTrue(is_valid_zip("99999"))
        self.assertTrue(is_valid_zip("123456789"))

    def test_false_zip(self):
        self.assertFalse(is_valid_zip("1234567890"))
        self.assertFalse(is_valid_zip("1234"))
        self.assertFalse(is_valid_zip(12345))
        self.assertFalse(is_valid_zip("ab123"))
        self.assertFalse(is_valid_zip("1234a"))
        self.assertFalse(is_valid_zip("99991234a"))
        self.assertFalse(is_valid_zip(""))

    def test_true_date(self):
        self.assertTrue(is_valid_date("10312017"))
        self.assertTrue(is_valid_date("01011111"))

    def test_false_date(self):
        self.assertFalse(is_valid_date("10322017"))
        self.assertFalse(is_valid_date("1012017"))
        self.assertFalse(is_valid_date("00000000"))
        self.assertFalse(is_valid_date(""))
        self.assertFalse(is_valid_date("abcdefgh"))
        self.assertFalse(is_valid_date("01322017"))


if __name__ == "__main__":
    unittest.main()
