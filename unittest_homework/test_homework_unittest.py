import unittest
from unittest.mock import patch
import requests
from homework_unittest import join_words
from datetime import datetime
def my_print (text, visible=True):
    if visible:
        print(text)
class TestJoinWords(unittest.TestCase):

#перед тестами должен быть сетап, который print("A test suite begins")
    def setUpClass(cls):
        print("A test suite begins")

#- после тестов должен быть тир даун, который print("A test suite ends")
    @classmethod
    def tearDownClass(cls):
        print("A test suite ends")

#перед тестом должен запускаться сетап, который print("A test beings")
    @classmethod
    def setUpClass(cls):
        my_print("A test beings")

#после теста должен быть тир даун, который print("A test ends")
    @classmethod
    def tearDownClass(cls):
        my_print("A test ends")

#должен быть один скипнутый тест
    @unittest.skip("This test is skipped")
    def test_skipped_test(self):
    result = join_words("skipped", "test")
    self.assertEqual(result, "skipped-test")

#должен быть один тест, который expectedFailure
    @unittest.expectedFailure
    def test_expected_failure(self):
        result = join_words("expected", "failure")
        self.assertEqual(result, "expected-failure-wrong-result")

#должен быть тест, где замоканный запрос "https://www.google.com/search?q=badger" возвращает "badger-racoon"
    @patch("requests.get", side_effect=mocked_get)
    def test_mocked_request(self, mock):
    response = requests.get("https://www.google.com/search?q=badger")
    self.assertEqual(response, 42)

#должен быть один тест, который скипается если сегодня понедельник, среда или пятница
    @unittest.skipIf(
        datetime.now().weekday() in [0, 2, 4],
        "Skip test on Monday, Wednesday, or Friday"
    )
    def test_skip_on_specific_weekdays(self):
    # my text here
        pass

#тест, который делает настоящий запрос в гугл, получает настоящий ответ, но статус мы подменяем на 404
    def test_real_request_with_status_404(self):
    with patch('requests.get') as mocked_request:
        mocked_request.return_value.status_code = 404
        response = requests.get("https://www.google.com")
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()