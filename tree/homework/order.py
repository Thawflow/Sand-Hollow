item1 = input("Item: ")
price1 = float(input("Price: "))
count1 = int(input("Count: "))

item2 = input("Item: ")
price2 = float(input("Price: "))
count2 = int(input("Count: "))

total = price1 * count1 + price2 * count2

pay = float(input("Payment: "))
change = pay - total

store = "Thawpaw's Dollar Tree"
print(f"{store:^30}")
print(f"Item: {item1}, {price1:,.2f} x {count1}")
print(f"Item: {item2}, {price2:,.2f} x {count2}")
print(f"Total: {total:,.2f}")
print(f"Payment: {pay:,.2f} yuan")
print(f"Your change: {change:.2f}")

