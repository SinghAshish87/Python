# balance = 2000.00

# # Predefined recharge plans
# recharge_plans = {
#     1: {"name": "Daily Data Pack - 1.5GB/day", "price": 199},
#     2: {"name": "Monthly Unlimited Pack", "price": 499},
#     3: {"name": "3-Months Combo Pack", "price": 999},
#     4: {"name": "Yearly Super Saver Pack", "price": 1799}
# }

# print("Welcome to the Mobile Recharge System")
# print("Your wallet balance is ₹", balance)

# while True:
#     print("\nMenu:")
#     print("1. Recharge")
#     print("2. Add Money")
#     print("3. Check Balance")
#     print("4. Exit")

#     try:
#         choice = int(input("Enter your choice: "))
#     except ValueError:
#         print("Invalid input! Please enter a number between 1 and 4.")
#         continue

#     if choice == 1:
#         print("\nAvailable Recharge Plans:")
#         for plan_id, plan in recharge_plans.items():
#             print(f"{plan_id}. {plan['name']} - ₹{plan['price']}")

#         try:
#             selected_plan = int(input("Select a plan number: "))
#             if selected_plan in recharge_plans:
#                 plan_price = recharge_plans[selected_plan]["price"]
#                 plan_name = recharge_plans[selected_plan]["name"]
#                 if plan_price <= balance:
#                     balance -= plan_price
#                     print(f"Recharge successful: {plan_name}")
#                     print("Thank you for using our service.")
#                     print("Your new balance is ₹", balance)
#                 else:
#                     print("Insufficient balance for this plan.")
#             else:
#                 print("Invalid plan selection.")
#         except ValueError:
#             print("Please enter a valid plan number.")
    
#     elif choice == 2:
#         try:
#             add_money = float(input("Enter the amount to add: "))
#             if add_money <= 0:
#                 print("Amount must be greater than zero.")
#             else:
#                 balance += add_money
#                 print("Money added successfully.")
#                 print("Your new balance is ₹", balance)
#                 print("Thank you for using our service.")
#         except ValueError:
#             print("Invalid amount entered.")
    
#     elif choice == 3:
#         print("Your current balance is ₹", balance)
#         print("Thank you for using our service.")

#     elif choice == 4:
#         print("Thank you for using the Mobile Recharge System.")
#         break

#     else:
#         print("Invalid choice. Please enter a number between 1 and 4.")


balance = 5000.00
print("welcome to the mobile recharge")
print("select your plan from below options")

while True:
    print("\nMenu:")
    print("1. Recharge")
    print("2. Add Money")
    print("3. Check Balance")
    print("4. Exit")

    try:
        choice = int(input("Enter any one form above  :(1,4): "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 to 4")
        continue

    if choice == 1:
        mobile_number = input("Enter the mobile number to recharge: ")
        if not mobile_number.isdigit() or len(mobile_number) != 10:
            print("Invalid mobile number. Please enter a 10-digit number.")
            continue

        print("Available recharge plans")
        print("1: ₹199 - 1GB data unlimited calls and 100 messages")
        print("2: ₹249 - 1.5GB data and unlimited calls and 100 messages")
        print("3: ₹299 - 2GB data unlimited calls and 100 messages for 1 month")
        print("4: ₹799 - 1.5GB data and unlimited calls and 100 messages for 3 month")
        print("5: ₹3999 -  2.5Gb data and untimate call and 100 messages for 1 year")
        print("6: Exit")

        try:
            selected_plan = int(input("Select any plan from above: "))
            if selected_plan < 1 or selected_plan > 6:
                print("Retue to The main menue ")
                continue

            plan_prices = {1: 199, 2: 249, 3: 299, 4: 799, 5:3999}
            if selected_plan == 5:
                continue

            if selected_plan not in plan_prices:
                print("Invalid plan selection. Please select a valid option.")
                continue
            plan_cost = plan_prices[selected_plan]

            if balance >= plan_cost:
                balance -= plan_cost
                if selected_plan == 1:
                    print("Recharge successful for mobile number:", mobile_number)
                    print("₹{} has been deducted.".format(plan_cost))
           
                    print("Your plan is activated.")
                    print("You have selected 1GB data unlimited calls and 100 messages plan one month")
                elif selected_plan == 2:
                    print("You have selected 1.5GB data and unlimited calls and 100 messages one month")
                elif selected_plan == 3:
                    print("You have selected 2GB data unlimited calls and 100 messages plan one month")
                elif selected_plan == 4:
                    print("You have selected 1.5GB data and unlimited calls and 100 messages fpor 3 month")
                elif selected_plan == 5:
                    print("You have selected 2.5GB data and unlimited calls and 100 messages for 1 year")
                    print("Recharge successful for mobile number:", mobile_number)
                    print("Thank you for using our service.")
                    print("Your new balance is ₹", balance)
                elif choice == 6:
                     print("Exiting the Mobile Recharge System.")
                     print("Thank you for using the Mobile Recharge System.")
                     break
            else:
                print("Insufficient balance. Please recharge your account.")

                print("Your plan is activated.")
                print("₹{} has been deducted.".format(plan_cost))
                print("Remaining balance: ₹", balance)
                
        
            #  else:
            #         print("Insufficient balance. Please add money to recharge.")

        except ValueError:
            print("Please enter a valid plan number.")

    elif choice == 2:
        try:
            amount = float(input("Enter the amount to add: "))
            if amount <= 0:
                print("Amount must be greater than zero.")
            else:
                balance += amount
                print("Money added successfully.")
                print("Your new balance is ₹", balance)
                print("Thank you for using our service.")
        except ValueError:
            print("Invalid amount entered.")

    elif choice == 3:
        print("Your current balance is ₹", balance)
        print("Thank you for using our service.")
        if balance < 0:
            print("Your balance is low. Please recharge.")
        else:
            print("Your balance is sufficient.")

    elif choice == 4:
        print("Exiting the Mobile Recharge System.")
        print("Thank you for using the Mobile Recharge System.")
        break

    elif choice == 5:  # Optional: this is redundant since 4 is for exit
        print("Exiting the Mobile Recharge System.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")






# 

