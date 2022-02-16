number_to_be_averaged = int(input("How many number to be average: "))
counter = 1
total = 0
while counter != number_to_be_averaged + 1:
    number = int(input(f"Enter number {counter} : "))
    total += number
    counter += 1
print(f"Total is {total}")
print(f"Average is {total / number_to_be_averaged}")
print(f"Average rounded to 2dp is {round(total / number_to_be_averaged,2)}")
