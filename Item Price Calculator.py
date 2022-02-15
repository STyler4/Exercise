Price = float(input("Please entre price: $"))
Item = (input("Please entre Item number:\n E.g. 1 food, or electrical etc. "))
if Price > 10:
    if Item == "food":
        Price *= 0.60
    elif Item == "electrical":
        Price *= 0.70
    else:
        Price *= 0.80
print(f"The price for your {Item} item will be ${Price:,.2f} ")
