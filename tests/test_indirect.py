import pytest


@pytest.fixture(scope='function')
def x(request):
    return request.param * 3


@pytest.fixture(scope='function')
def y(request):
    return request.param * 2


def test_indirect(x, y):
    assert x == 'aaa'
    assert y == 'b'
