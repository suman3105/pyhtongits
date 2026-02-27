
user_id = "101"
password = "abc123"
balance = 5000

uid = input("Enter ID: ")
pwd = input("Enter Password: ")

if uid == user_id and pwd == password:
    print("\nLogin Successful!")

    while True:
        print("\n---- MENU ----")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Your Balance:", balance)

        elif choice == "2":
            amt = int(input("Enter amount to deposit: "))
            balance += amt
            print("Deposit Successful!")
            print("Updated Balance:", balance)

        elif choice == "3":
            amt = int(input("Enter amount to withdraw: "))
            if amt <= balance:
                balance -= amt
                print("Withdraw Successful!")
                print("Updated Balance:", balance)
            else:
                print("Insufficient Balance!")

        elif choice == "4":
            print("Thank you! Exiting...")
            break

        else:
            print("Invalid Choice!")

else:
    print("Invalid ID or Password!")
