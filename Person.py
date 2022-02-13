Age = float(input("Enter your age: "))
Weight = float(input("Enter your weight: "))
MIN_AGE = 16
MIN_WEIGHT = 50

if Age < MIN_AGE or Weight < MIN_WEIGHT:
    print("You can't give blood")

else:
    print("You can give blood")
