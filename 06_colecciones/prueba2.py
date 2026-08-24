# CASHIER ALGORITHM
import locale

try:
    locale.setlocale(locale.LC_ALL, "es_CO.utf8")
except locale.Error:
    locale.setlocale(locale.LC_ALL, "")

print("Welcome to the mini market Fuck Society!")
# variables
quantity: int = 0
price: float = 0
total_price: float = 0

quantity = int(input("Please input the quantity of product to buy: "))
price = float(input("please input the price per unit in COP: "))

while quantity <= 0:
    quantity = int(
        input("you should register at least one product to buy, try again: ")
    )
else:
    print("pretty well quantity")

while price <= 0:
    price = float(input("the price or value of product must be greater than zero: "))
else:
    print("pretty well price")

print(f"total price of purchase is: {locale.currency(quantity*price,grouping=True)}")
