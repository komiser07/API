from requests import Response
from utils.checking import Checking

from utils.api import GoogleMapsApi


class TestCreatePlace:

    def test_create_new_place(self):
        print("\nметод POST")
        result_post: Response = GoogleMapsApi.create_new_place()
        Checking.check_status_code(result_post, 200)

        print("\nметод GET POST")
        result_get: Response = GoogleMapsApi.get_new_place(result_post.json()["place_id"])
        Checking.check_status_code(result_get, 200)

        print("\nметод PUT")
        result_put: Response = GoogleMapsApi.put_new_place(result_post.json()["place_id"])
        Checking.check_status_code(result_put, 200)

        check_response_put = result_put.json()
        msg = check_response_put.get('msg')

        print("\nметод GET PUT")
        result_get: Response = GoogleMapsApi.get_new_place(result_post.json()["place_id"])
        Checking.check_status_code(result_get, 200)

        print("\nметод DELETE")
        result_delete: Response = GoogleMapsApi.delete_new_place(result_post.json()["place_id"])
        Checking.check_status_code(result_delete, 200)

        print("\nметод GET DELETE")
        result_get: Response = GoogleMapsApi.get_new_place(result_post.json()["place_id"])
        Checking.check_status_code(result_get, 404)

