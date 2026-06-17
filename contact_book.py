contacts = {}

while True:
    print("\n===== Contact Book =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")

        contacts[name] = phone
        print("Contact Added!")

    elif choice == "2":
        print("\nContacts:")
        for name, phone in contacts.items():
            print(name, "-", phone)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")