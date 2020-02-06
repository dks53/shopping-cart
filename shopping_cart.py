# shopping_cart.py

#from pprint import pprint
import operator
import pandas
from datetime import datetime

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

#print(products)

print("")
print("WELCOME TO THE GEORGETOWN GROCERY STORE")
print("")

# user INPUT of data
prod_list = []
# prod_list = [1, 8, 6, 16, 6] # temporary list of valid ids for testing purposes

subtotal = 0


while True:
    prod_id = input("Please input product identifier, or 'DONE' if there are no more items: ")
    if prod_id == "DONE":
        print("Here are the products you chose: ", prod_list)
        break
    else:
        prod_id = int(prod_id)
        matching_product = [p for p in products if p["id"] == prod_id]
        prod_list.append(prod_id)
        for prod in matching_product:
            print("+ ", prod["name"], "(", to_usd(prod["price"]), ")")
        price = prod["price"]
        subtotal = subtotal + price


# Look-up products



# computer OUTPUT of results

dateTimeObj = datetime.now() # Returns a datetime object containing the local date and time

print("--------------------------------")
print("GEORGETOWN GROCERY STORE")
print("--------------------------------")

print("Website: www.gugrocery.com")
print("Phone: 202-660-3650")
print("DATE: ", dateTimeObj.year, '/', dateTimeObj.month, '/', dateTimeObj.day)
print("TIME: ", dateTimeObj.hour, ':', dateTimeObj.minute)
print("--------------------------------")

print("PRODUCT DETAILS")

print("--------------------------------")
tax = 0.1
print("SUBTOTAL: $", round(subtotal, 2))

tax_amt = subtotal * tax
print("TAX: $", round(tax_amt, 2))

total_price = subtotal - tax_amt
print("TOTAL PRICE: $", round(total_price, 2))
print("--------------------------------")
print("Thank you for shopping with us!")
print("********************************")



# A grocery store name of your choice
# A grocery store phone number and/or website URL and/or address of choice
# The date and time of the beginning of the checkout process, formatted in a human-friendly way (e.g. 2019-06-06 11:31 AM)
# The name and price of each shopping cart item, price being formatted as US dollars and cents (e.g. $1.50)
# The total cost of all shopping cart items, formatted as US dollars and cents (e.g. $4.50), calculated as the sum of their prices
# The amount of tax owed (e.g. $0.39), calculated by multiplying the total cost by a New York City sales tax rate of 8.75% (for the purposes of this project, groceries are not exempt from sales tax)
# The total amount owed, formatted as US dollars and cents (e.g. $4.89), calculated by adding together the amount of tax owed plus the total cost of all shopping cart items
# A friendly message thanking the customer and/or encouraging the customer to shop again