import pytest
import time
import requests
from flask import Response

def is_palindrome(s):
    return s == s[::-1]

@pytest.mark.skip
def test_always_passes():
    resp = requests.get("https://www.google.com")
    response = Response(resp.content, resp.status_code)
    assert True

@pytest.mark.skip
def test_always_reversed():
    assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]

@pytest.mark.skip
def test_sometimes_passes():
    assert False

@pytest.mark.parametrize("maybe_palindrome, expected_result", [
    ("", True),
    ("a", True),
    ("Bob", False),
    ("Never odd or even", False),
    ("Do geese see God?", False),
    ("abc", False),
    ("abab", False),
])
def test_is_palindrome(maybe_palindrome, expected_result):
    assert is_palindrome(maybe_palindrome) == expected_result