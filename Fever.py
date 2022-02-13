Age = float(input("Enter your age: "))
Temperature = float(input("Enter your temperature: "))

if Age < 2 and Temperature >= 38:
    print("Call a doctor")
elif Temperature > 39.5:
    print("High fever")

else:
    print("You're fine")
