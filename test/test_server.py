import pytest
import socket
import os


def test_server_connect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 8080))
    print(client)
    assert client
