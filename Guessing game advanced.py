import random
number = random.randint(1, 101)
# print(number)
count = 1
mode = ""
while mode != "H" and mode != "E":
    mode = input("Enter 'H' for Hard mode or 'E' for Easy: "). upper()
    if mode == "H":
        num_guesses = 4
    elif mode == "E":
        num_guesses = 10
    else:
        print("That was not an option")
guess = int(input("Guess the number: "))

while guess != number and count < num_guesses:
    count += 1
    if guess > number:
        guess = int(input("Lower. Try again: "))
    else:
        guess = int(input("Higher. Try again: "))
if guess == number:
    print(f"You got it in {count} guesses")
else:
    print(f"You used up your {count} guesses")
