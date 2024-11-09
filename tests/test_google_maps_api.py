from requests import Response

from utils.api import GoogleMapsApi


class TestCreatePlace:

    def test_create_new_place(self):
        print("\nметод POST")
        result_post: Response = GoogleMapsApi.create_new_place()

        print("\nметод GET POST")
        result_get: Response = GoogleMapsApi.get_new_place(result_post.json()["place_id"])

        # проверка, что запрос GET прошёл успешно
        assert result_get.status_code == 200, " Ошибка, локация с таким place_id отсутствует"
        print(f"Статус код {result_get.status_code}, запрос прошёл успешно")

        print("\nметод PUT")
        result_put: Response = GoogleMapsApi.put_new_place(result_post.json()["place_id"])

        check_response_put = result_put.json()
        msg = check_response_put.get('msg')
        print(msg)

        print("\nметод GET PUT")
        result_get: Response = GoogleMapsApi.get_new_place(result_post.json()["place_id"])

        # проверка, что при не существующем (существующем) place_id выводится нужное сообщение
        assert msg == "Update address operation failed, looks like the data doesn't exists"
        # assert msg == "Address successfully updated"
        print("Поле MSG корректно")
