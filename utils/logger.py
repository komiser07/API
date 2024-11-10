import datetime
import os

from requests import Response


class Logger:
    # создаём файл в который будут сохраняться логи, со временем их создания
    file_name = f'logs/log_' + str(datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')) + ".log"

    @classmethod
    def write_log_to_file(cls, data: str):
        with open(cls.file_name, 'a', encoding='utf=8') as logger_file:
            logger_file.write(data)

    # создаём метод, который добавляет в log файл строки для запросов
    @classmethod
    def add_request(cls, url: str, method: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')

        data_to_add = f'\n-----\n'
        data_to_add += f'Test: {test_name}\n'
        data_to_add += f'Time: {str(datetime.datetime.now())}\n'
        data_to_add += f'Request method: {method}\n'
        data_to_add += f'Request URL: {url}\n'
        data_to_add += '\n'

        cls.write_log_to_file(data_to_add)

    # создаём метод, который добавляет в log файл строки после ответа от сервера.
    @classmethod
    def add_response(cls, result: Response):
        headers_as_dict = dict(result.headers)
        cookies_as_dict = dict(result.cookies)

        data_to_add = f'Response code: {result.status_code}\n'
        data_to_add += f'Response test:\n{result.text}\n'
        data_to_add += f'Response headers:\n{headers_as_dict}\n'
        data_to_add += f'Response cookies:\n{cookies_as_dict}\n'
        data_to_add += f'\n-----\n'

        cls.write_log_to_file(data_to_add)

        return cls.file_name
