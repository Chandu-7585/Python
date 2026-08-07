def calculator():
    while True:
        print("\n ----- Calculator Menu -----")
        print("1. Addition\n2. Substraction\n3. Exit")
        choice = input("Select an option (1-3): ")

        if choice == '3':
            print("Goodbye!")
            break

        if choice in ('1','2'):
            n1 = float(input("Enter first Number: "))
            n2 = float(input("Enter second Number: "))

            if choice == '1':
                print(f"Result: {n1 + n2}")
            elif choice == '2':
                print(f"Result: {n1 - n2}")
        else:
            print("Invalid option!!!")

calculator()

