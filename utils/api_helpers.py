from requests import Session, Response
import curlify
import logging


def to_curl(request, compressed=False, verify=True):
    try:
        return curlify.to_curl(request, compressed=compressed, verify=verify)
    except UnicodeDecodeError:
        request.body = str(request.body)
        return curlify.to_curl(request, compressed=compressed, verify=verify)


def request_counter():
    global REQUEST_COUNT
    REQUEST_COUNT += 1
    return REQUEST_COUNT


class ApiSession(Session):
    """Сессия с base_url, логами запросов в файлы allure-report и консоль"""

    def __init__(self, console_log, **kwargs):
        custom_session_headers = kwargs.pop('headers', {})

        self.base_url = kwargs.pop('base_url')

        self.console_log = console_log
        super().__init__(**kwargs)
        self.headers.update(custom_session_headers)

    def request(self, method, url, **kwargs) -> Response:
        """Сессия с base_url и логами request/response для allure-report и вывода в консоль"""
        url = f'{self.base_url}{url}'
        headers = kwargs.pop('headers', {})
        headers.update(self.headers)

        response = super().request(method, url, headers=headers, **kwargs)

        request_counter()

        if self.console_log:
            curl = to_curl(response.request)
            if response.status_code in [200, 201, 204]:
                logging.info(f'{response.status_code} {response.reason} {curl}')
            else:
                logging.warning(f'{response.status_code} {response.reason} {curl}')

        return response


class ResponseValidator:

    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code

    def validate_json(self, schema):
        if isinstance(self.response_json, list):
            assert schema.model_validate(self.response_json[0])
        else:
            assert schema.model_validate(self.response_json)
        return self

    def validate_status_code(self, status_code):
        assert self.response_status == status_code, \
            f'Ожидался код {status_code}, пришел {self.response_status}'
        return self
