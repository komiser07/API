# импортируем библиотеку request
import requests


class HttpMethods:
    headers = {'Content-Type': 'application/json'}
    cookie = ""

    # создаём статический метод GET
    @staticmethod
    def get(url):
        result = requests.get(
            url,
            headers=HttpMethods.headers,
            cookies=HttpMethods.cookie
        )
        return result

    # создаём статический метод POST
    @staticmethod
    def post(url, body):
        result = requests.post(
            url,
            json=body,
            headers=HttpMethods.headers,
            cookies=HttpMethods.cookie
        )
        return result

    # создаём статический метод PUT
    @staticmethod
    def put(url, body):
        result = requests.put(
            url,
            json=body,
            headers=HttpMethods.headers,
            cookies=HttpMethods.cookie
        )
        return result

    # создаём статический метод DELETE
    @staticmethod
    def delete(url, body):
        result = requests.delete(
            url,
            json=body,
            headers=HttpMethods.headers,
            cookies=HttpMethods.cookie
        )
        return result
