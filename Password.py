correct_password = "pineapple"
attempt = input("What is your password: ")
while attempt != correct_password:
    attempt = input("Password incorrect, try again: ")
print("Access granted")

