Patient = int(input("What is the patient's age: "))
if Patient < 12:
    weight = int(input("Enter weight: "))
    dose = weight * 10
else:
    dose = 1000
print(f"Recommend {dose}mg paracetamol")
