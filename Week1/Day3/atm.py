balance = 10000

while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = int(input("Enter choice: "))

    if choice == 1: 
     print("Check Balance: ",balance)

    elif choice == 2:
     amount = float(input("Enter amount to deposit: "))
     balance = balance + amount
     print("Deposit Successful")
     print("Updated balance: ",balance)

    elif choice == 3:
     amount = float(input("Enter amount to withdraw: "))
     if amount <= balance:
          balance= balance- amount
          print("Withrawing Successful")
          print("Remaining balance: ",balance)
     else:
      print("Insufficient balance")

    elif choice == 4:
        print("Thank you for using the ATM.")
        break

    else:
        print("Invalid choice")

