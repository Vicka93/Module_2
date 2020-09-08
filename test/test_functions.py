"""
Author:Viktoriia Denys
Program:camper_age_input_py
The program will have will prompt for the age of one infant (age 1-5 years) who is attending camp
and convert the age in months to years via a function call then print the result.

"""

import unittest
from main import camper_age_input


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(72, camper_age_input.convert_to_months(6))


if __name__ == '__main__':
    unittest.main()
