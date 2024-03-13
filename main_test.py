from main import return_backward_string, get_mode

import unittest
import os

class TestMain(unittest.TestCase):
    def test_return_backword_string(self):
        random_string = "dipoo"
        reversed_random_string = "oopid"
        self.assertEqual(reversed_random_string, return_backward_string(random_string))

    def test_get_mode(self):
        self.assertEqual('dev', get_mode())


if __name__ == '__main__':
    unittest.main()

