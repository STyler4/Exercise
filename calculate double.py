def calculate_double(amount):
    double = amount * 2
    return double


# Main routine
question = int(input("How much: "))
answer = calculate_double(question)
print(f"Double {question} is: {calculate_double(question)}")
