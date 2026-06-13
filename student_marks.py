name = input("Enter Student Name: ")
marks = int(input("Enter Marks: "))

print("\n----- Report Card -----")
print("Student:", name)
print("Marks:", marks)

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: F")