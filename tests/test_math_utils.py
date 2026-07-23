from math_utils import is_palindrome


def test_is_palindrome_returns_true_for_simple_palindrome():
    assert is_palindrome("racecar") is True


def test_is_palindrome_ignores_case_and_spaces():
    assert is_palindrome("Never Odd Or Even") is True


def test_is_palindrome_returns_false_for_non_palindrome():
    assert is_palindrome("hello") is False


def test_is_palindrome_returns_true_for_empty_string():
    assert is_palindrome("") is True
