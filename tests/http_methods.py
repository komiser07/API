# импортируем библиотеку request
import request

# создаём класс
class HttpMethods:
    # Заголовки для HTTP запросов и куки
    headers = {'Content-Type': 'application/json'}
    cookie = ""

    # создаём статический метод GET
    @staticmethod
    def get(url):
        result = request.get(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return result.json()

    # создаём статический метод POST
    @staticmethod
    def post(url, body):
        result = request.post(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return result.json()

    # создаём статический метод PUT
    @staticmethod
    def put(url, body):
        result = request.put(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return result.json()

    # создаём статический метод DELETE
    @staticmethod
    def delete(url, body):
        result = request.delete(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return result.json()