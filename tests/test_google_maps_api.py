from requests import Response
from utils.checking import Checking
from utils.api import GoogleMapsApi


class TestCreatePlace:

    def test_create_new_place(self):
        print("\nметод POST")
        result_post: Response = GoogleMapsApi.create_new_place()
        Checking.check_status_code(result_post, 200)
        Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Checking.check_json_value(result_post, 'status', 'OK')

        print("\nметод GET POST")
        result_get: Response = GoogleMapsApi.get_new_place(result_post.json()["place_id"])
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get,
                                  ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                   'language'])
        Checking.check_json_value(result_get, 'address', '29, side layout, cohen 09')

        print("\nметод PUT")
        result_put: Response = GoogleMapsApi.put_new_place(result_post.json()["place_id"])
        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put, ['msg'])
        Checking.check_json_value(result_put, 'msg', 'Address successfully updated')

        print("\nметод GET PUT")
        result_get: Response = GoogleMapsApi.get_new_place(result_post.json()["place_id"])
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get,
                                  ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                   'language'])
        Checking.check_json_value(result_get, 'address', '44, Volgograd, RU')

        print("\nметод DELETE")
        result_delete: Response = GoogleMapsApi.delete_new_place(result_post.json()["place_id"])
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_token(result_delete, ['status'])
        Checking.check_json_value(result_delete, 'status', 'OK')

        print("\nметод GET DELETE")
        result_get: Response = GoogleMapsApi.get_new_place(result_post.json()["place_id"])
        Checking.check_status_code(result_get, 404)
        Checking.check_json_token(result_get, ['msg'])
        Checking.check_json_search_word_in_value(result_get, 'msg', 'failed')

        print("Тестирование создания, изменения и удаления новой локации прошло успешно")
