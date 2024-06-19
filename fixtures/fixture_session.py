from utils.api_helpers import ApiSession
from utils.config import Service
import pytest


@pytest.fixture(scope='session')
def microservice(server, console_log) -> ApiSession:
    service_url = Service(server).microservice
    yield from session_or_skip(server, service_url, console_log)


def session_or_skip(server, service_url, console_log=False, **kwargs):
    """Функция пропуска тестов сервисов, для которых не указан service_url."""
    if service_url is None:
        pytest.skip(f'skipped on this platform: {server}')
    else:
        with ApiSession(
                **kwargs,
                base_url=service_url,
                console_log=console_log
        ) as session:
            yield session
