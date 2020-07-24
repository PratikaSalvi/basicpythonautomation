import pytest

@pytest.fixture()
def setup():
    print("Once before executing every test case")


def testmethod1(setup):
    print("//this is test method 1")

def testmethod2():
    print("//this is test method 2")