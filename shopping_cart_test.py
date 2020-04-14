# shopping_cart_test.py

import pytest

#from shopping_cart import to_usd, find_product, calculate_tax, calculate_total_price
from shopping_cart import tax_rate, to_usd

## TODO:

def test_tax_rate():
    assert(tax_rate) == 0.0875

# test to_usd
def test_to_usd():
    result = to_usd(13673.239020)
    assert result == "$13,673.24"

# test find_product

# test calculate_tax

# test calculate_total_price