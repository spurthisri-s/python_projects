visitors = set()

while True:
    print("\n===== Visitor Tracker =====")
    print("1. Add Visitor")
    print("2. View Visitors")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter Visitor Name: ")
        visitors.add(name)
        print("Visitor Added!")

    elif choice == "2":
        print("\nUnique Visitors:")
        for visitor in visitors:
            print(visitor)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")