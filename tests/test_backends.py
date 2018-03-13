import pytest


class DB1(object):
    """database object one"""


class DB2(object):
    """alternative database object"""


@pytest.fixture
def db(request):
    '''returns instalce of a database'''
    if request.param == 'd1':
        return DB1()
    elif request.param == 'd2':
        return DB2()
    else:
        raise ValueError('Invalid internal test config')


def test_db_initialized(db):
    if db.__class__.__name__ == 'DB2':
        pytest.fail('Deliberately failing for demo purposes')
