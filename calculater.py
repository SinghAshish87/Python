

# with list and user input
# and even without list and user input

# list= [1,3,4,56,233,56,78,90,45,27,39,29,12,34,56,78,90]

# while True:
#     try:
#         # Ask user for the number they want to check
#         number = int(input("Enter a number from the list: "))
#         if number not in list:
#             print("that number is not in the list .Try again")
#             continue 
#         if number % 2 == 0:
#             print(f"{number} is even")
#         else:
#             print(f"{number} is odd")
#     except ValueError:
#             print("Please enter a valid integer.")
 
#     # Ask user if they want to continue
#     choice = input("Do you want to check another number? (yes/no): ").lower()
#     if choice != 'yes':
#         print("Exiting the program. Goodbye!")
#         break




my_list = [1, 3, 4, 56, 233, 56, 78, 90, 45, 27, 39, 29, 12, 34, 56, 78, 90]

while True:
    try:
        action = input("\nWhat do you want to do? (check/calculate): ").lower()

        if action == 'calculate':
            # Choose number from list or enter new
            source = input("Use a number from the list or add your own? (list/add): ").lower()

            if source == 'add':
                number1 = int(input("Enter your first number: "))
            elif source == 'list':
                number1 = int(input("Enter a number from the list: "))
                if number1 not in my_list:
                    print("That number is not in the list.")
                    continue
            else:
                print("Invalid option. Try again.")
                continue

            # Get the second number and the operation
            number2 = int(input("Enter the second number: "))
            operation = input("Enter operation (+, -, *, /): ")

            # Perform the calculation
            if operation == '+':
                result = number1 + number2
            elif operation == '-':
                result = number1 - number2
            elif operation == '*':
                result = number1 * number2
            elif operation == '/':
                if number2 == 0:
                    print("Cannot divide by zero.")
                    continue
                result = number1 / number2
            else:
                print("Invalid operation.")
                continue

            print(f"Result: {number1} {operation} {number2} = {result}")

        elif action == 'check':
            # Check even or odd
            choice = input("Use existing number or add your own? (list/add): ").lower()

            if choice == 'add':
                new_number = int(input("Enter the number you want to check: "))
                my_list.append(new_number)
                number = new_number
            elif choice == 'list':
                number = int(input("Enter a number from the list: "))
                if number not in my_list:
                    print("That number is not in the list.")
                    continue
            else:
                print("Invalid choice.")
                continue

            if number % 2 == 0:
                print(f"{number} is even")
            else:
                print(f"{number} is odd")

        else:
            print("Invalid action. Type 'check' or 'calculate'.")
            continue

    except ValueError:
        print("Please enter a valid number.")

    again = input("\nDo you want to continue? (yes/no): ").lower()
    if again != 'yes':
        print("Exiting the program. Goodbye!")
        break
