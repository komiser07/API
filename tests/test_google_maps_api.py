from requests import Response

from utils.api import GoogleMapsApi

class TestCreatePlace:

    def test_create_new_place(self):

        print("метод POST")
        result_post: Response = GoogleMapsApi.create_new_place()

        print("метод GET")
        result_get: Response = GoogleMapsApi.get_new_place(result_post.json()["place_id"])

        # проверка, что запрос GET прошёл успешно
        assert result_get.status_code == 200
        print(f"Статус код {result_get.status_code}")