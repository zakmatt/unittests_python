def pytest_addoption(parser):
    parser.addoption(
        "--all",
        action="store_true",
        help="run all combinations"
    )


def pytest_generate_tests(metafunc):
    if 'param1' in metafunc.fixturenames:
        if metafunc.config.getoption('all'):
            end = 5
        else:
            end = 2
        metafunc.parametrize("param1", range(end))

    # database examples
    if 'db' in metafunc.fixturenames:
        metafunc.parametrize('db', ['d1', 'd2'], indirect=True)

    if 'x' and 'y' in metafunc.fixturenames:
        metafunc.parametrize('x, y', [('a', 'b')], indirect=['x'])
