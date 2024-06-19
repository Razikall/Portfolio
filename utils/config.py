class Service:
    """Домены сервисов на различных окружениях."""
    def __init__(self, server: str):

        self.microservice = {
            'stage': 'http://stage.microservice.test.ru',
            'preprod': 'http://preprod.microservice.test.ru',
            'prod': 'http://microservice.test.ru',
        }[server]
