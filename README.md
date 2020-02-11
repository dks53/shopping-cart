# Darshil Shah - Shopping Cart Project

This document walks you (the user) through this shopping cart project. It will help you setup your environment to run the code successfully. If you have any questions, you can reach out to project lead dks53@georgetown.edu

## What does this code do?

Asks the user to input one or more product identifiers, then looks up the prices for each, then prints an itemized customer receipt including the total amount owed.

When the clerk inputs a product identifier, the program validates it, displaying a helpful message like "Please input product identifier, or 'DONE' if there are no more items" if there are no products matching the given identifier.

At any time the clerk is able to indicate there are no more shopping cart items by inputting the word 'DONE'

After the clerk indicates there are no more items, the program prints a custom receipt on the screen. The receipt includes:

1) Name of the grocery store
2) Store phone number and website URL
3) The date and time of the beginning of the checkout process
4) The name and price of each shopping cart item, price being formatted as US dollars and cents (e.g. $3.50, etc.)
5) The total cost of all shopping cart items (i.e. the "subtotal"), formatted as US dollars and cents (e.g. $19.47), calculated as the sum of their prices
6) The amount of tax owed (e.g. $1.70), calculated by multiplying the total cost by a New York City sales tax rate of 8.75% (for the purposes of this project, groceries are not exempt from sales tax)
7) The total amount owed, formatted as US dollars and cents (e.g. $21.17), calculated by adding together the amount of tax owed plus the total cost of all shopping cart items
8) A friendly message thanking the customer and/or encouraging the customer to shop again

## Setup
Use GitHub Desktop software or the command-line to download or "clone" the repository onto your computer. Choose a familiar download location like the Desktop.

After cloning the repo, navigate there from the command-line: 

```sh
cd ~/Desktop/shopping-cart
```
## Environment setup

Create and activate a new Anaconda virtual environment:

```sh
conda create -n shopping-env python=3.7 # (first time only)
conda activate shopping-env
```

From within the virtual environment, demonstrate your ability to run the Python script from the command-line:

```sh
python shopping_cart.py
```

## Configuring Sales Tax Rates

If you'd like to share your code with stores in other locations as well, but different municipalities use different sales tax rates, you can now configure the tax via the ".env" file. 

Click on the .env file and set the tax to your state/munucipality's tax rate and save the file before running the program.

## Writing Receipts to File

In addition to displaying a receipt at the end of the checkout process, the program writes the receipt information into a new ".txt" file saved in the "receipts" directory inside the project repository. The clerk's printer-connected computer should be able to actually print a paper receipt from the information contained in this file.

Once you run the code, navigate to the "receipts" directory inside the project repository and find the receipt for the code that you just ran. All receipts will remain in that folder.

All receipts are saved in the following format:
receipts/year-month-day-hour-minute-second-microsecond.txt