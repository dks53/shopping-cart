# shopping_cart_test.py

import pytest

#from shopping_cart import tax_rate, to_usd, find_product, calculate_tax, calculate_total_price
from shopping_cart import tax_rate, to_usd, find_product

# test tax_rate
def test_tax_rate(): 
    assert(tax_rate) == 0.1
    
    '''
    Imports the tax_rate set in the shopping_cart.py file and checks to see if it matches.
    If the tax_rate is changed in the shopping_cart.py file, it must be changed in this test_tax_rate function too.
    The tax rate by default is set to 10% (0.1)
    '''

# test to_usd
def test_to_usd():
    result = to_usd(13673.239020)
    assert result == "$13,673.24"
    
    '''
    Tests the to_usd function for formatting - displays the $ sign, rounds to and displays 2 decimals and inserts thousands separator.
    '''

# test find_product
def test_find_product():
    products = [
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] 
    # test to see if the product matches 
    matching_product = find_product("1", products)
    assert matching_product["name"] == "Chocolate Sandwich Cookies"
    
    # test to see if the price matches
    matching_product = find_product("6", products)
    assert matching_product["price"] == 21.99

    # test to confirm that both product and price match
    matching_product = find_product("19", products)
    assert matching_product["name"] == "Gluten Free Quinoa Three Cheese & Mushroom Blend"
    assert matching_product["price"] == 3.99

    # TODO: What to do if it doesn't match?
    # HAVE REMOVED PRODUCT NUMBER 3 FROM THE LIST TO TEST THE ERROR.
    # IndexError?

    '''
    Tests the product finding and matching function. Ensures that the product ID selected by the customer matches an existing product
    in the database/list. If the product exists, it will pass and allow the user to continue. If the product doesn't exist it will 
    display an error.
    '''

# test calculate_tax

# test calculate_total_price