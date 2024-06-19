import allure
import resources.microservice.apples as apple_json
from xml.dom.minidom import parseString
from utils.api_helpers import ResponseValidator


def get_xml(microservice, token, source_id, source):
    with allure.step("Запрос тестового xml"):
        result = microservice.get(url=f'/test/get/{source_id}/xml', headers=token)
        assert result.status_code == 200
        root = parseString(result.content)
        assert root.getElementsByTagName("channel")[0].childNodes[0].firstChild.nodeValue == source
        assert root.getElementsByTagName("title").length > 70


def get_apples(microservice):
    with allure.step("Валидация json-схемы"):
        result = microservice.get(url=f"/apples")
        response = ResponseValidator(result)
        response.validate_status_code(200).validate_json(apple_json.DataApples)
