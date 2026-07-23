"""Tiny scratch module for testing close-tickets."""


def is_palindrome(s: str) -> bool:
    """Return True if `s` is a palindrome, ignoring case and spaces."""
    normalized = s.lower().replace(" ", "")
    return normalized == normalized[::-1]
