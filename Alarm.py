Day = int(input("What day is it?\n1 Mon, 2 Tue.... 7 Sun: "))

if Day < 6 and Day > 0:
    print("Alarm rings at 7")
elif Day == 6:
    print("Alarm rings at 7")
elif Day == 7:
    print("Alarm ring at 9")
else:
    print("That was not a number between 1 and 7")
