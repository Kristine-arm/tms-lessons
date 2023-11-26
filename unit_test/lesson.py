import unittest
from unittest.mock import Mock, MagicMock, patch
import requests
from some_function import add_two_numbers, Life

def my_print(text, visible=True):
    if visible:
        print(text)

def mocked_get(*args, **kwargs):
    return 42


class TestAddTwoNumbers(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        my_print("Creating...")

    @classmethod
    def tearDownClass(cls):
        my_print("Deleting...")

    def setUp(self):
        my_print("Connecting...")

    def tearDown(self):
        my_print("Closing... Done")

    def test_add_simple_numbers(self):
        result = add_two_numbers(2, 2)

        self.assertEqual(result, 4)

    def test_check_bool(self):
        my_print("Test #2")
        result = add_two_numbers(2, 2, return_bool=True)

        self.assertTrue(result)

    def test_exception(self):
        my_print("Test #3")
        with self.assertRaises(TypeError):
            add_two_numbers(2, "a")

    @unittest.skip("This raises an exception! Not cool!")
    def test_skip_test(self):
        raise Exception("!!!!!!!")

    @unittest.skipif(
        # int(datetime.now().timestamp()) % 2 == 0,
        "Skipped because timestamp is even",
    )
    def test_skip_if_test(self):
        raise Exception("!!!!!!!")

    @unittest.expectedFailure
    def test_xfail(self):
        result = add_two_numbers(2, 3)
        self.assertEqual(result, 4)

    # ==========================================================================

    def test_mock_1(self):
        mock = Mock(return_value=4)

        self.assertEqual(add_two_numbers(2, 2), mock())

    def test_mock_2(self):
        mock = Life()
        mock.meaning_of_life = MagicMock(return_value=42)

        self.assertEqual(mock.meaning_of_life(), 42)

    @patch("requests.get", side_effect=mocked_get)
    def test_mock_3(self, mock):
        response = requests.get("https://www.google.com/")

        self.assertEqual(response, 42)