
# balance = 2000.0  

# print("Welcome to Simple Pay")
# print(f"You have Balance thts is: ₹{balance:.2f}")
# print("choose any one option from below")

# while True:
#     print("\n1. Pay")
#     print("2. Add Money")
#     print("3. Check Balance")
#     print("4. Exit")

#     choice = input("Choose any one from above (1-4): ")
     

#     if choice == "1":
#         name = input("Pay to: ").strip()
#         try:
#             amount = float(input(" You have choosen 1 option Amount: enter the Amount ₹:"))
#             if amount <= 0:
#                 print("Enter a (positive)currect amount.")
#             elif amount > balance:
#                 print("Not enough balance.")
#             else:
#                 balance -= amount
#                 print(f" Paid ₹{amount:.2f} to {name}.")
#                 print(f" Remaining balance: ₹{balance:.2f}")
#         except ValueError:
#             print("Enter a valid number.")

#     elif choice == "2":
#         try:
#             amount = float(input(" You have choosen 2 option, Added amount: ₹"))
#             if amount <= 0:
#                 print("Enter a (positive)currect amount.")
#             else:
#                 balance += amount
#                 print(f" ₹{amount:.2f} added.")
#         except ValueError:
#             print(" Enter a valid number.")

#     elif choice == "3":
#         print(f" You have choosen 3 option , Balance: ₹{balance:.2f}")

#     elif choice == "4":
#         print(" You have choosen 4 option Exit :  Goodbye! see u soon")
#         break

#     else:
#         print("Invalid choice.")
        
        
        
        
        
# new  updated way  and  in this we can check the  transaction  history      
      


from datetime import datetime

balance = 2000.0
transactions = []


def generate_upi_qr(name, upi_id, amount, filename="upi_qr.png"):
    upi_url = f"upi://pay?pa={upi_id}&pn={name}&am={amount}&cu=INR"

    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(upi_url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"QR Code generated and saved as '{filename}'")
    img.show()  



print("Welcome to Simple Pay")
print(f"Your current balance is: ₹{balance:.2f}")

while True:
    print("\nPlease choose an option:")
    print("1. Pay")
    print("2. Add Money")
    print("3. Check Balance")
    print("4. Exit")
    print("5. Transaction History")
    print("6. Generate QR to Receive Payment")


    choice = input("Enter choice (1-6): ")

    if choice == "1":
        name = input("Pay to: ").strip()
        try:
            amount = float(input("Enter amount to pay ₹: "))
            if amount <= 0:
                print("Please enter a valid positive amount.")
            elif amount > balance:
                print("Insufficient balance.")
            else:
                balance -= amount
                transactions.append(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Paid ₹{amount:.2f} to {name}")
                print(f"Paid ₹{amount:.2f} to {name}. Remaining balance: ₹{balance:.2f}")
        except ValueError:
            print("Invalid input. Please enter a number.")

    elif choice == "2":
        try:
            amount = float(input("Enter amount to add ₹: "))
            if amount <= 0:
                print("Please enter a valid positive amount.")
            else:
                balance += amount
                transactions.append(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Added ₹{amount:.2f}")
                print(f"₹{amount:.2f} added successfully. New balance: ₹{balance:.2f}")
        except ValueError:
            print("Invalid input. Please enter a number.")

    elif choice == "3":
        print(f"Your current balance is: ₹{balance:.2f}")

    elif choice == "4":
        print("Exiting Simple Pay. Goodbye!")
        break

    elif choice == "5":
        if transactions:
            print("\n--- Transaction History ---")
            for t in transactions:
                print(t)
        else:
            print("No transactions yet.")

    elif choice == "6":
        upi_id = input("Enter your UPI ID (e.g., ashish@bank): ").strip()
        name = input("Enter your name: ").strip()
        try:
            amount = float(input("Enter amount to receive ₹: "))
            if amount <= 0:
                print("Enter a valid positive amount.")
            else:
                filename = f"{upi_id}_qr.png"
                generate_upi_qr(name, upi_id, amount, filename)
        except ValueError:
            print("Invalid amount entered.")

    else:
        print("Invalid choice. Please select between 1 and 6.")
        
      
        
           