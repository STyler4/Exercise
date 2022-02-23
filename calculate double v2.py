def calculate_double(amount):
    double = amount * 2
    return double


def calculate_half(amount):
    half = amount / 2
    return half


def calculate_ten_more(amount):
    ten_more = amount + 10
    return ten_more
    

# Main routine
question = int(input("How much: "))
answer1 = calculate_double(question)
answer2 = calculate_half(question)
answer3 = calculate_ten_more(question)
print(f"Double {question} is: {answer1}")
print(f"Half {question} is: {answer2}")
print(f"Adding ten to {question} is: {answer3}")
