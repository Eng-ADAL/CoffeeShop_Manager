# CoffeeShop - Unit Test
# Agile - 4

"""
test_utils.py – Unit tests for CoffeeShop Manager CLI utils.
Covers functions in source/utils.py such as valid_price().
"""

from source.utils import valid_price

# utils.py valid price test

def test_valid_price_with_number():
    assert valid_price("1.99") is True

def test_valid_price_with_zero():
    assert valid_price("0") is True

def test_invalid_price_with_text():
    assert valid_price("banana") is False

def test_invalid_price_with_negative():
    assert valid_price("-5.0") is False
