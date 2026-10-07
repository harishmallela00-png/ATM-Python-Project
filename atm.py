# ATM Withdrawal and Customer Details System

customer_name = input("Enter customer name: ")
account_number = input("Enter account number: ")
pin = input("Set your 4-digit PIN: ")

balance = 10000.0

print("\n===== ATM SYSTEM =====")

entered_pin = input("Enter your PIN: ")

if entered_pin == pin:
    print("\nLogin successful!")
    
    while True:
        print("\n----- ATM MENU -----")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Customer Details")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print(f"\nAvailable Balance: ₹{balance:.2f}")

        elif choice == "2":
            amount = float(input("Enter withdrawal amount: "))

            if amount <= 0:
                print("Enter a valid amount.")
            elif amount > balance:
                print("Insufficient balance.")
            else:
                balance -= amount
                print(f"Withdrawal successful!")
                print(f"Amount withdrawn: ₹{amount:.2f}")
                print(f"Remaining balance: ₹{balance:.2f}")

        elif choice == "3":
            amount = float(input("Enter deposit amount: "))

            if amount <= 0:
                print("Enter a valid amount.")
            else:
                balance += amount
                print(f"Deposit successful!")
                print(f"Amount deposited: ₹{amount:.2f}")
                print(f"New balance: ₹{balance:.2f}")

        elif choice == "4":
            print("\n----- CUSTOMER DETAILS -----")
            print("Customer Name:", customer_name)
            print("Account Number:", account_number)
            print(f"Balance: ₹{balance:.2f}")

        elif choice == "5":
            print("\nThank you for using the ATM.")
            break

        else:
            print("Invalid choice. Please try again.")

else:
    print("\nIncorrect PIN.")
    print("Access denied.")
