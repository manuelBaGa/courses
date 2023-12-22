import pytest


#  Fixture example is now in conftest.py file
#  @pytestDemo.fixture()
#  def setup():
#    print("I will be executing first")
#    yield
#    print("I will be executing last")

@pytest.mark.usefixtures("setup")
class TestExample:
    def test_fixtureDemo(self):
        print("I will execute steps in fixtureDemo method")

    def test_fixtureDemo1(self):
        print("I will execute steps in fixtureDemo method")

    def test_fixtureDemo2(self):
        print("I will execute steps in fixtureDemo method")

    def test_fixtureDemo3(self):
        print("I will execute steps in fixtureDemo method")