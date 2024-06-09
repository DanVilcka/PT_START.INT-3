import pytest
import socket
import os


# def is_palindrome(palindrome):
#     palindrome = palindrome.lower()
#     palindrome = palindrome.replace(' ', '')
#     palindrome = ''.join(char for char in palindrome if char.isalnum())
#     if str(palindrome) == str(palindrome)[::-1]:
#         return True
#     else:
#         return False
#
#
# @pytest.mark.parametrize("maybe_palindrome, expected_result", [
#     ("", True),
#     ("a", True),
#     ("Bob", True),
#     ("Never odd or even", True),
#     ("Do geese see God?", True),
#     ("abc", False),
#     ("abab", False),
# ])
# def test_is_palindrome(maybe_palindrome, expected_result):
#     assert is_palindrome(maybe_palindrome) == expected_result
#

def test_server_connect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 8080))
    print(client)
    assert client
