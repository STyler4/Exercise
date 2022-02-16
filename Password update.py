count = 0
correct_password = "pineapple"
attempt = input("What is your password: ")
while count < 3 and attempt != correct_password:
    attempt = input("Password incorrect, try again: ")
    count += 1
if attempt == correct_password:
    print("Access granted")
else:
    print("Too many attempts")


