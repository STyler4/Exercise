Mark = (int(input("Please enter mark: ")))
if Mark >= 90:
    print(f"{Mark} is grade A")
elif Mark >= 70:
    print(f"{Mark} is grade B")
elif Mark >= 50:
    print(f"{Mark} is grade C")
else:
    print(f"{Mark} is a fail")
