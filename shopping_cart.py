# shopping_cart.py

import operator
import pandas
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

def to_usd(my_price):
    return f"${my_price:,.2f}" #> $12,000.71
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Source: https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/datatypes/numbers.md#formatting-as-currency
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}

] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

print("")
print("WELCOME TO THE GEORGETOWN GROCERY STORE")
print("")

# user INPUT of data

selected_products = []

while True:
    prod_id = input("Please input product identifier, or 'DONE' if there are no more items: ")
    if prod_id == "DONE":
        break
    else:
        prod_id = int(prod_id)
        matching_products = [p for p in products if p["id"] == prod_id]
        
        try:
            matching_product = matching_products[0]
            print("+ ", matching_product["name"], "(", to_usd(matching_product["price"]), ")")
            selected_products.append(matching_product)
        except IndexError:
            print("Product doesn't exist! Please select another product.")

# computer OUTPUT of results

dateTimeObj = datetime.now() # Returns a datetime object containing the local date and time
subtotal = 0 

print("--------------------------------")
print("GEORGETOWN GROCERY STORE")
print("--------------------------------")

print("Website: www.gugrocery.com")
print("Phone: 202-660-3650")
print("DATE: ", dateTimeObj.year, '/', dateTimeObj.month, '/', dateTimeObj.day)
print("TIME: ", dateTimeObj.hour, ':', dateTimeObj.minute)
print("--------------------------------")

print("PRODUCT DETAILS:")

for prod in selected_products:
    print("+ ", prod["name"], "(", to_usd(prod["price"]), ")")
    price = prod["price"]
    subtotal = subtotal + price

print("--------------------------------")
print("SUBTOTAL:", to_usd(subtotal))

tax = os.getenv("state_tax")
tax = float(tax)
tax_amt = subtotal * tax
print("TAX (", tax * 100, "%): ", to_usd(tax_amt))

total_price = subtotal + tax_amt
print("TOTAL PRICE:", to_usd(total_price))
print("--------------------------------")
print("Thank you for shopping with us!")
print("We hope to see you again soon!")
print("********************************")
