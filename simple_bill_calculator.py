# This program calculates the total cost of items
price = float(input("Enter the price of one item: "))
quantity = int(input("How many items do you want? "))

total = price * quantity

print(f"you bought {quantity} items at ${price:.2f} each = ${total:.2f}")
