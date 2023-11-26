import pytest
@pytest.mark.wizard
class TestHomework:
    @pytest.mark.parametrize("first_name, last_name", [("John", "Smith"), ("Harry", "Potter"), ("Ron", "Weasley")])
    def test_fail_if_john_smith(self, age, first_name, last_name):
        print(f"Hello {first_name} {last_name}! Your age is {age}")
        if first_name == "John" and last_name == "Smith":
            pytest.xfail("XFAIL: Test is expected to fail for John Smith.")