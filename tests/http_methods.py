import request

class HttpMethods:
    headers = {'Content-Type': 'application/json'}
    cookie = " "

    @staticmethod
    def get(url):
        result = request.get(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return result.json()

    @staticmethod
    def post(url, body):
        result = request.post(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return result.json()

    @staticmethod
    def put(url, body):
        result = request.put(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return result.json()

    @staticmethod
    def delete(url, body):
        result = request.delete(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return result.json()