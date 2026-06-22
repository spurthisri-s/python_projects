while True:

    try:

        print("\n===== Safe Calculator =====")

        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))

        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = input("Choose Operation: ")

        if choice == "1":
            print("Result =", num1 + num2)

        elif choice == "2":
            print("Result =", num1 - num2)

        elif choice == "3":
            print("Result =", num1 * num2)

        elif choice == "4":
            print("Result =", num1 / num2)

        else:
            print("Invalid Choice")

        break

    except ZeroDivisionError:
        print("Division by zero is not allowed!")

    except ValueError:
        print("Please enter valid numbers!")