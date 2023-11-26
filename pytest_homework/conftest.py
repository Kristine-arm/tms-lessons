import pytest
import random

@pytest.fixture(scope='function')
def age():
    random_age = random.randint(0, 100)
    print(f"Random age is {random_age}")
    yield random_age
    print("Deleting random age... Done")