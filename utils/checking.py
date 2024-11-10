from requests import Response


class Checking():

    @staticmethod
    def check_status_code(responce: Response, status_code):
        assert status_code == responce.status_code
        if responce.status_code == status_code:
            print(f"Статус код = {responce.status_code}, запрос прошёл успешно")
        else:
            print(f"Ошибка, статус код = {responce.status_code}")

