# shopping_cart.py

import operator
import pandas
from datetime import datetime
import os
from dotenv import load_dotenv
import csv
load_dotenv()

# defining variables used
tax_rate = 0.1 # constant, default value
selected_prod_ids = [] # list holds all the product IDs entered by the user (created using append)
subtotal = 0 # ensures that the subtotal calculation begins at 0 for each customer.

# defining functions
def to_usd(my_price):
    return f"${my_price:,.2f}" #> $12,000.71
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Source: https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/datatypes/numbers.md#formatting-as-currency
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """

def find_product(one_prod_id, all_products):
    matching_products = [p for p in all_products if str(p["id"]) == one_prod_id]
    matching_product = matching_products[0]
    return matching_product
    """
    Checks if the product requested by the customer exists in the database (products list)
    Param 1: "one_prod_id" which holds the unique product identifier that is entered by the user
    Param 2: "all_products" which holds the entire list of products
    Returns: "matching_product" with all the key/value paris corresponding to the selected product ID
    Example: matching_product = {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50}
    """

def calculate_tax(pretax_subtotal):
    tax_amt = pretax_subtotal * tax_rate
    return tax_amt
    """
    Calculated the amount of tax to be paid on a particular purchase/transaction
    Param: pretax_subtotal (float) like 68.52
    Example: calculate_tax(68.52)
    Returns: 5.9955
    """

def calculate_total_price(pretax_subtotal,tax_charged):
    total_price = pretax_subtotal + tax_charged
    return total_price
    """
    Calculated the total price to be paid on a particular purchase/transaction
    Param 1: pretax_subtotal (float) like 68.52
    Param 2: tax_charged (float) like 5.9955
    Example: calculate_tax(68.52,5.9955)
    Returns: 74.5155
    """

# TODO: define a function to refactor timestamp-formatting logic


## Product dictionary based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017
#products = [
#    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
#    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
#    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
#    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
#    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
#    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
#    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
#    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
#    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
#    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
#    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
#    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
#    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
#    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
#    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
#    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
#    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
#    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
#    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
#    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
#] 
#
### user INPUT of data
#
#print("")
#print("WELCOME TO THE GEORGETOWN GROCERY STORE")
#print("")
#
#while True:
#    prod_id = input("Please input product identifier, or 'DONE' if there are no more items: ")
#    if prod_id == "DONE":
#        break
#    else:
#        selected_prod_ids.append(prod_id)
#        matching_product = find_product(prod_id, products)
#        print("+ ", matching_product["name"], "(", to_usd(matching_product["price"]), ")")
#
## computer OUTPUT of results
#
#dateTimeObj = datetime.now() # Returns a datetime object containing the local date and time
#
#print("--------------------------------")
#print("GEORGETOWN GROCERY STORE")
#print("--------------------------------")
#
#print("Website: www.gugrocery.com")
#print("Phone: 202-660-3650")
#print("DATE: ", dateTimeObj.year, '/', dateTimeObj.month, '/', dateTimeObj.day)
#print("TIME: ", dateTimeObj.hour, ':', dateTimeObj.minute)
#print("--------------------------------")
#
#print("PRODUCT DETAILS:")
#
## loop to print products and prices on the receipt
#for prod_id in selected_prod_ids:
#
#    matching_product = find_product(prod_id, products)
#    print("+ ", matching_product["name"], "(", to_usd(matching_product["price"]), ")")
#    
#    price = matching_product["price"]
#    subtotal = subtotal + price
#
#    tax_amt = calculate_tax(subtotal)
#        
#    total_price = calculate_total_price(subtotal,tax_amt)
#    
#print("--------------------------------")
#print("SUBTOTAL:", to_usd(subtotal))
#print("TAX (", tax_rate * 100, "%): ", to_usd(tax_amt))
#print("TOTAL PRICE:", to_usd(total_price))
#print("--------------------------------")
#print("Thank you for shopping with us!")
#print("We hope to see you again soon!")
#print("********************************")
#print("")