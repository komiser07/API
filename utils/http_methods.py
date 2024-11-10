# импортируем библиотеку request
import requests

from utils.logger import Logger


class HttpMethods:
    headers = {'Content-Type': 'application/json'}
    cookie = ""

    # создаём статический метод GET
    @staticmethod
    def get(url):
        Logger.add_request(url, method='GET')
        result = requests.get(
            url,
            headers=HttpMethods.headers,
            cookies=HttpMethods.cookie
        )
        Logger.add_response(result)
        return result

    # создаём статический метод POST
    @staticmethod
    def post(url, body):
        Logger.add_request(url, method='POST')
        result = requests.post(
            url,
            json=body,
            headers=HttpMethods.headers,
            cookies=HttpMethods.cookie
        )
        Logger.add_response(result)
        return result

    # создаём статический метод PUT
    @staticmethod
    def put(url, body):
        Logger.add_request(url, method='PUT')
        result = requests.put(
            url,
            json=body,
            headers=HttpMethods.headers,
            cookies=HttpMethods.cookie
        )
        Logger.add_response(result)
        return result

    # создаём статический метод DELETE
    @staticmethod
    def delete(url, body):
        Logger.add_request(url, method='DELETE')
        result = requests.delete(
            url,
            json=body,
            headers=HttpMethods.headers,
            cookies=HttpMethods.cookie
        )
        Logger.add_response(result)
        return result
