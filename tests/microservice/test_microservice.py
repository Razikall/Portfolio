import utils.microservice.microservice_helpers as microservice_requests
from pytest import mark
import allure


@allure.parent_suite("Microservice")
@allure.feature("Microservice")
@allure.suite("GET /test/get/{source_id}/xml")
@allure.title("Запрос тестового xml")
@mark.microservice
@mark.parametrize("source_id, source", [(2, "test1"), (3, "test2"), (4, "test3")])
def test_get_xml(microservice, token, source_id, source):
    """ Запрос тестового xml из разных источников """
    microservice_requests.get_xml(microservice, token, source_id, source)


@allure.parent_suite("Microservice")
@allure.feature("Microservice")
@allure.suite("GET test/get/apples")
@allure.title("Запрос яблок")
@mark.microservice
def test_get_apples(microservice):
    """ Валидация статускода и данных при запросе яблок """
    microservice_requests.get_apples(microservice)
