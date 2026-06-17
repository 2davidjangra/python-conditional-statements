pin = int(input("Enter PIN: "))
balance = 10000

if pin == 1234:
    amount = float(input("Enter Withdrawal Amount: "))
    
    if amount <= balance:
        print("Withdrawal Successful")
        print("Remaining Balance =", balance - amount)
    else:
        print("Insufficient Balance")
else:
    print("Invalid PIN")
