cart = {}
total = 0.0

print("🛒 Welcome to Simple Grocery Billing")

while True:
    print("\n1. Add Item")
    print("2. View Cart")
    print("3. Checkout")
    print("4. Exit")

    choice = input("👉 Choose an option (1-4): ")

    if choice == "1":
        item = input("🍎 Enter item name: ").capitalize()
        try:
            price = float(input("💰 Enter item price: ₹"))
            if price <= 0:
                print("⚠️ Enter a valid price.")
            else:
                cart[item] = cart.get(item, 0) + price
                total += price
                print(f"✅ Added {item} - ₹{price:.2f}")
        except ValueError:
            print("⚠️ Enter a valid price.")

    elif choice == "2":
        if not cart:
            print("🛒 Your cart is empty.")
        else:
            print("📋 Your Cart:")
            for item, price in cart.items():
                print(f"• {item}: ₹{price:.2f}")
            print(f"Total: ₹{total:.2f}")

    elif choice == "3":
        if not cart:
            print("🛒 Your cart is empty.")
        else:
            print("🧾 Checkout Summary:")
            for item, price in cart.items():
                print(f"• {item}: ₹{price:.2f}")
            print(f"🧮 Total Amount: ₹{total:.2f}")
            print("✅ Thank you for shopping!")
            cart.clear()
            total = 0.0

    elif choice == "4":
        print("👋 Exiting Grocery Billing. Goodbye!")
        break

    else:
        print("❗ Invalid option. Choose from 1 to 4.")
