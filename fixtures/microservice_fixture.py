import pytest


@pytest.fixture(scope='function')
def token():
    token = {
        'TOKEN': 'wmitwnik',
    }

    return token
