import pytest

@pytest.fixture(scope='function')
def fixture_function():
    print('--- function')


@pytest.fixture(scope='class')
def fixture_class():
    print('--- class')


@pytest.fixture(scope='module')
def fixture_module():
    print('--- module')


@pytest.fixture(scope='session')
def fixture_session():
    print('--- session')