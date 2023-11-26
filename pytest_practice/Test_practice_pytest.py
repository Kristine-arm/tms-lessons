import pytest
@pytest.fixture
def person():
    return "John"
class TestMyClass:
    def test_my_first_test_no_fixture(self):
        pass

    def test_my_second_test_with_fixture(self, person):
        print(f'{person} loves Mary')

    @pytest.mark.parametrize("lady", ['Sarah', 'Jane', 'Elizabeth'])
    def test_my_third_test_with_parametrize(self, person, lady):
        print(f'{person} loves {lady}')

    @pytest.fixture
    def end_of_story():
    yield
    print('The end')

    @pytest.fixture(scope='class', autouse=True)
    def big_end_of_story():
    yield
    print('End of story')

class TestClass:
    def test_function(self, end_of_story):
        pass

    @pytest.mark.skip
    def test_i_dont_like(self):
        pass

