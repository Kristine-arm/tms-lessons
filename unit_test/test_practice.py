import unittest
from practice_home import divide_two_numbers
import requests
from unittest.mock import patch
class TestDivideTwoNumbers(unittest.TestCase):
    def test_smoke(self):
        result = divide_two_numbers(2,2)
        self.assertEqual(result, 1)

    def test_zero_division_error(self):
        with self.assertRaises(ZeroDivisionError):
            divide_two_numbers(2, 0)

    @unittest.skip('can not calculate')
    def test_skip_test(self):
        result = divide_two_numbers(6, 3)
        self.assertEqual(result, 3)
    @unittest.expectedFailure
    def test_expected_failure(self):
        result = divide_two_numbers(8, 3)
        self.assertEqual(result, 4)

    def mocked_get(*args, **kwargs):
        return "you know python"
    @patch('requests.get', side_effect= mocked_get)
    def test_mock(self, mock):
        link = 'https://teachmeskills.pl/'
        response = requests.get(link)
        self.assertEqual(response,"you know python" )

