score = 0

print("===== Python Quiz =====")

answer = input("1. What keyword is used to define a function in Python? ")

if answer.lower() == "def":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("2. Which data type stores multiple values? ")

if answer.lower() == "list":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("3. What does HTML stand for? ")

if "hypertext" in answer.lower():
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("\nFinal Score:", score, "/ 3")