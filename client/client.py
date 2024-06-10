import socket
import json

address_to_server = ('localhost', 8080)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address_to_server)


# data_qu = json.decoder.JSONDecoder().decode('''
# {
#     "command": "QuarantineLocalFile",
#     "params": {
#         "/Users/daniilvilchinskiy/Desktop/Programming/Courses/PT-START/INT-3/INT-3/test/test.txt": "/Users/daniilvilchinskiy/Desktop/Programming/Courses/PT-START/INT-3/INT-3/test/folder"
#     }
# }''')
#
# data_ch = json.decoder.JSONDecoder().decode('''
#     {
#         "command": "CheckLocalFile",
#         "params": {
#             "/Users/daniilvilchinskiy/Desktop/Programming/Courses/PT-START/INT-3/INT-3/test/test.txt": "test.txt"
#         }
#     }
# ''')

def str_split(string):
    try:
        bytes_array = bytes(map(int, string.split()))
    except:
        bytes_array = string.encode('utf-8')
    return bytes_array.decode('utf-8')


name = input('Введите имя функции: ')
param = input('Введите первый параметр: ')
value = input('Введите значение: ')
json_conf = json.decoder.JSONDecoder().decode('''
    {{
        "command": "{}",
        "params": {{ 
            "{}": "{}" 
        }}
    }}
'''.format(name, param, str_split(value)))
client.sendall(bytes(json.dumps(json_conf), encoding='UTF-8'))

data_qu = client.recv(1024).decode('UTF-8')
print(str(data_qu))
