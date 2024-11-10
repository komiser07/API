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

    @staticmethod
    def check_json_value(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(f"Значение поля {field_name} = {check_info}. Верно!")

    @staticmethod
    def check_json_search_word_in_value(response: Response, field_name, search_word):
        check = response.json()
        check_info = check.get(field_name)
        if search_word in check_info:
            print(f"Слово '{search_word}' найдено в поле {field_name}")
        else:
            print(f"Слово '{search_word}' не найдено в поле {field_name}")



