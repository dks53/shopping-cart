# Darshil Shah - Shopping Cart Project

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

