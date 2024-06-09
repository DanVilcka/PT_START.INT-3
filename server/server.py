"""
Подключаем логирование
Для сервера оно обязательно!
"""
import logging
logging.basicConfig(level=logging.DEBUG, filename="../logs/server.log", filemode="w", format="%(asctime)s %(levelname)s %(message)s")


"""
Начало основного кода сервера
"""
# импорт библиотек и функций
import json
import select
import socket


from Functions import CheckLocalFile, QuarantineLocalFile

logging.info("Объявляем переменные")
SERVER_ADDRESS = ('localhost', 8080)
print("")
MAX_CONNECTIONS = int(input("Введите максимальное количество одновременных соединений: "))
INPUTS = list()
OUTPUTS = list()



def get_non_blocking_server_socket():

    logging.warning("Создаем сокет, который работает без блокирования основного потока")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setblocking(0)

    logging.info("Биндим сервер на нужный адрес и порт")
    server.bind(SERVER_ADDRESS)

    logging.info("Установка максимального количество подключений")
    server.listen(MAX_CONNECTIONS)

    return server


def handle_readables(readables, server):

    logging.warning("Обрабатываем события на вход")
    for resource in readables:
        if resource is server:
            connection, client_address = resource.accept()
            logging.info("Новое соединение " + str(client_address))
            connection.setblocking(0)
            INPUTS.append(connection)
        else:
            logging.info("Обрабатываем не!серверный сокет")
            data = []
            try:
                logging.warning("Получаем данные из буфера и парсим их")
                res = str(resource.recv(1024), 'utf-8')
                lines = res.splitlines()
                json_data = lines[-1]
                data = parse(json_data)
            except ConnectionResetError:
                pass

            if data:
                result = []
                logging.warning("Запуск функции " + data[0])
                if data[0] == 'CheckLocalFile':
                    for key in data[1]:
                        try:
                            res = CheckLocalFile.CheckLocalFile(key, data[1][key])
                            if isinstance(res, list):
                                for item in res:
                                    result.append(f"Значение найдено в строке: {item[0]}, Количество символов от начала строки: {item[1]}.\n")
                            else:
                                result.append(str(res))
                        except Exception as e:
                            print(e)
                            result = 'Error'
                else:
                    for key in data[1]:
                        try:
                            result = QuarantineLocalFile.QuarantineLocalFile(key, data[1][key])
                        except Exception as e:
                            print(e)
                            result = 'Error'
                if isinstance(result, list):
                    for data in result:
                        resource.send(bytes(str(data), 'utf-8'))
                else:
                    resource.send(bytes(str(result), 'utf-8'))

                if resource not in OUTPUTS:
                    OUTPUTS.append(resource)
            else:
                logging.warning("Закрываем сокет из-за отсутствия входных данных")
                clear_resource(resource)

def parse(req):
    data = json.loads(req)
    command = data['command']
    params = data['params']

    return [command, params]

def clear_resource(resource):
    if resource in OUTPUTS:
        OUTPUTS.remove(resource)
    if resource in INPUTS:
        INPUTS.remove(resource)
    resource.close()

    logging.warning("Очистка ресурсов!")


def handle_writables(writables):
    logging.warning("Отправление данных при освобождении помяти от подключения")
    for resource in writables:
        try:
            logging.warning("Отправка сообщения об окончании соединения")
            resource.send(bytes('\nThis is answer for your request!\nConnection closed!', encoding='UTF-8'))
        except OSError:
            clear_resource(resource)


if __name__ == '__main__':
    logging.warning("Создаем серверный сокет без блокирования основного потока в ожидании подключения")
    server_socket = get_non_blocking_server_socket()
    INPUTS.append(server_socket)

    print("Сервер запущен для остановки Ctrl+C")
    logging.info("server is running, please, press ctrl+c to stop")
    try:
        while INPUTS:
            readables, writables, exceptional = select.select(INPUTS, OUTPUTS, INPUTS)
            handle_readables(readables, server_socket)
            handle_writables(writables)
    except KeyboardInterrupt:
        clear_resource(server_socket)
        print("Сервер остановлен!")
        logging.info("Server stopped! Thank you for using!")