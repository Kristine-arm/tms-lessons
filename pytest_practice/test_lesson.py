# from datetime import datetime
#
# import pytest
# import requests
#
# import random
# from dataclasses import dataclass
# import pytest
#
#
# @pytest.fixture
# def meaning_of_life():
#     return 42
#
# @pytest.fixture
# def fixture_with_yield():
#     print("\nBefore test")
#
#     yield
#
# @pytest.fixture
# def fixture_teardown():
#     yield
#     print("\nAfter test")
#
#
# @dataclass
# class User:
#     name: str
#     last_name: str
#     age: int
#
#
# @pytest.fixture
# def user():
#     some_user = User("Vasya", "Pupkin", age=random.randrange(0, 100))
#
#     yield some_user
#
#
# @pytest.fixture
# def delete_user():
#     yield
#     print("Delete user")
#
#
# @pytest.fixture(scope="class")
# def class_setup():
#     print("This is class setup")
#
#
# @pytest.fixture(autouse=True)
# def auto_fixture():
#     print("Before")
#     yield
#     print("After")
#
#
# @pytest.fixture(scope="session", autouse=True)
# def big_fixture():
#     pass
#
# class TestFirstClass:
#     def test_with_fixture(self, meaning_of_life):
#         assert meaning_of_life == 42
#
#     def test_with_yield(self, fixture_with_yield):
#         print("\nThis is test")
#
#     def test_with_teardown(self, fixture_teardown):
#         print("\nThis is test")
#
#     def test_with_user(self, user, delete_user):
#         # Arrange
#         user.age = 50
#         # Act
#         # Assert
#         assert user.age == 50
#         ...
#
#     def test_with_class_fixture(self, class_setup):
#         print("This is test")
#
#     def test_bare_function(self):
#         print("This is test")
#
#     # ==========================================================================
#
#     def test_first(self):
#         print("\nThis is my test")
#
#     def test_failing_test(self):
#         response = requests.get("https://www.google.com/")
#         status_code_actual = response.status_code
#         status_code_expected = 404
#
#         assert status_code_actual == status_code_expected
#
#     def test_failing_test(self):
#         response = requests.get("https://www.google.com/")
#         status_code_actual = response.status_code
#         status_code_expected = 404
#
#         assert status_code_actual == status_code_expected
#
#     @pytest.mark.skip
#     def test_failing_test_skipped(self):
#         response = requests.get("https://www.google.com/")
#         status_code_actual = response.status_code
#         status_code_expected = 404
#
#         assert status_code_actual == status_code_expected
#
#     @pytest.mark.skipif(
#         int(datetime.now().timestamp()) % 2 == 0, reason="Timestamp is even"
#     )
#     def test_failing_test_skipped_condition(self):
#         response = requests.get("https://www.google.com/")
#         status_code_actual = response.status_code
#         status_code_expected = 404
#
#         assert status_code_actual == status_code_expected
#
#     @pytest.mark.xfail
#     def test_failing_test_xfail(self):
#         response = requests.get("https://www.google.com/")
#         status_code_actual = response.status_code
#         status_code_expected = 404
#
#         assert status_code_actual == status_code_expected
#
#     def test_failing_test_xfail_inside(self):
#         response = requests.get("https://www.google.com/")
#         status_code_actual = response.status_code
#
#         if status_code_actual == 200:
#             pytest.xfail("We hate 200")
#
#         status_code_expected = 404
#
#         assert status_code_actual == status_code_expected
#
#     @pytest.mark.tms
#     def test_custom_mark(self):
#         pass
#
#     def test_google_status(self, class_setup):
#         print("1")
#         response = requests.get("https://www.google.com/")
#
#         assert response.ok
#
#     def test_google_request(self, class_setup):
#         print("2")
#         response = requests.get("https://www.google.com/search?q=badger")
#
#         assert response.ok
#
#     @pytest.mark.parametrize("name", ["Petya", "Vasya"])
#     def test_with_one_param(self, name):
#         print(f"Hello, {name}!")
#
#     @pytest.mark.parametrize("name", ["Petya", "Vasya"])
#     @pytest.mark.parametrize("patronymic", ["111", "222"])
#     @pytest.mark.parametrize("last_name", ["Pupkin", "Sidorov"])
#     def test_with_two_param(self, name, last_name, patronymic):
#         print(f"Hello, {name} {last_name}!")
#
#     @pytest.mark.parametrize("money", [2, 100, 250])
#     def test_real(self, money):
#         if money < 100:
#             print("Not enought")
#         elif money == 100:
#             print("Just fine!")
#         elif money > 100:
#             print("Too much")
