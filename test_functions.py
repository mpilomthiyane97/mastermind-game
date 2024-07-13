import unittest
from unittest.mock import patch
import mastermind
from io import StringIO
import sys
sys.stdout = StringIO()


class TestFunction(unittest.TestCase):

    """test if it is a list and the length of that list"""
    def test_code(self):
        self.assertEqual(len(mastermind.create_code()), 4)
        self.assertIsInstance(mastermind.create_code(), list)
        self.assertNotIn(mastermind.create_code()[0], [0, 9])
        self.assertNotIn(mastermind.create_code()[1], [0, 9])
        self.assertNotIn(mastermind.create_code()[2], [0, 9])
        self.assertNotIn(mastermind.create_code()[3], [0, 9])

    """test if answer is correct digits and correct digits in correct position """
    @patch("sys.stdin", StringIO("3246\n3264\n1578\n6423"))
    def test_turns(self):

        code = [3, 2, 4, 6]
        self.assertEqual(mastermind.take_turn(code,"3246"),4)
        self.assertEqual(mastermind.take_turn(code,"3264"),2)
        self.assertEqual(mastermind.take_turn(code,"1578"),0)
        self.assertEqual(mastermind.take_turn(code,"6423"),0)


    """test if the length of the answer is correct"""
    @patch("sys.stdin", StringIO("123\n12345\n1234\n"))
    def test_user_input(self):
        self.assertEqual(mastermind.user_input(), "1234")


    """test if answer is correct"""
    def test_check_correctness(self):
        self.assertFalse(mastermind.check_correctness(3,5))
        self.assertTrue(mastermind.check_correctness(4,5))

   

if __name__ == "__main__":
    unittest.main()




