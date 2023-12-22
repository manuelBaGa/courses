# Any pytestDemo file should start with test_
# pytestDemo method names should start with test
#Any code should be wrapped in method only
#Execute project:
# py.test -v -s
import pytest


@pytest.mark.smoke
def test_firstProgram():
    print("Hello")

@pytest.mark.xfail
def test_secondProgram_CreditCard():
    print("Good Morning")

def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])