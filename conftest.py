import pytest
from utils.constants import Servers

pytest_plugins = [
    'fixtures.microservice_fixture',
    'fixtures.fixtures_session'
]


def pytest_addoption(parser):
    """Pytest command settings parameters.

    Example:
        pytest --server=stage

    """
    parser.addoption(
        '--server',
        help='Тестовый сервер',
        choices=[
            Servers.STAGE,
            Servers.PREPROD,
            Servers.PROD,
        ],
        default='dev',
    )
    parser.addoption(
        '--console-log',
        help='Логирование request, 0=Выключено, 1=включено',
        default=1,
    )


@pytest.fixture(scope='session')
def console_log(request):
    return bool(int(request.config.getoption('--console-log')))
