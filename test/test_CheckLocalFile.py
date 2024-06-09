import pytest
from server.Functions.CheckLocalFile import CheckLocalFile


@pytest.mark.parametrize("file_path, signature, result", [
    ("test.txt", "print(i)", [2, 4])
])
def test_CheckLocalFile(file_path, signature, result):
    assert CheckLocalFile(file_path, signature) == result
