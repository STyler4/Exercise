import random
number = random.randint(1,11)
guess = int(input("Guess the number: "))
# print(number)


while guess != number:
    guess = int(input("Wrong. Try again: "))
print("You got it")
