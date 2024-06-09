import os
from server.Functions.QuarantineLocalFile import QuarantineLocalFile
import pytest
@pytest.mark.parametrize("path, file", [
    ("/Users/daniilvilchinskiy/Desktop/Programming/Courses/PT-START/INT-3/INT-3/test/test.txt", "/Users/daniilvilchinskiy/Desktop/Programming/Courses/PT-START/INT-3/INT-3/test/folder")
])
def test_QuarantineLocalFile(path, file):
    my_file = open("text_replace_file.txt", "w+")
    my_file.close()
    assert QuarantineLocalFile(path, file) == True
    os.remove("folder/text_replace_file.txt")