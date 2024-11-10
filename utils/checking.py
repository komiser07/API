import json

from requests import Response


class Checking:

    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print(f"Статус код = {response.status_code}, запрос прошёл успешно")
        else:
            print(f"Ошибка, статус код = {response.status_code}")

    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("Все поля присутствуют")


