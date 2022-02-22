import random
number = random.randint(1,101)
guess = int(input("Guess the number: "))
# print(number)


while guess > number:
    guess = int(input("Lower. Try again: "))
while guess < number:
    guess = int(input("Higher. Try again: "))
print("You got it")
