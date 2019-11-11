acountbal = 50000
choice = input("Please enter 'b' to check balance, 'w' to withdraw or 'd' to deposit: ")
while choice != 'q':
    if choice.lower() in ('w','b','d'):
        if choice.lower() == 'b':
            print("Your balance is: %d" % acountbal)
            print("Anything else?")
            choice = input("Enter b for balance, w to withdraw, d to deposit or q to quit: ")
            print(choice.lower())
        elif choice.lower() == 'w':
            try:
                withdraw = float(input("Enter amount to withdraw: "))
                if withdraw <= acountbal:
                    print("here is your: %.2f" % withdraw)
                    acountbal = acountbal - withdraw
                    print("Anything else?")
                    choice = input("Enter b for balance, w to withdraw, d to deposit or q to quit: ")
                else:
                    print("You have insufficient funds: %.2f" % acountbal)
            except:
                print("Enter amount in digits")
        else:
            try:
                deposit = int(input("Enter amount to deposit: "))    
                if deposit <= acountbal:
                    print("Here is your deposited amount: %d" % deposit)
                    acountbal = acountbal + deposit
                    print("Anything else?")
                    choice = input("Enter b for balance, w to withdraw, d to deposit or q to quit: ")
                elif deposit > acountbal:
                    print("Here is your deposited amount: %d" % deposit)
                    acountbal = acountbal + deposit
                    print("Anything else?")
                    choice = input("Enter b for balance, w to withdraw, d to deposit or q to quit: ")
                    #choice = 'q'
                else:
                    print("You have insufficient funds: %.2f" % acountbal)
            except:
                print("Enter amount in digits") 
    else:
        print("Wrong choice!")
        choice = input("Please enter 'b' to check balance, 'w' to withdraw or 'd' to deposit: ")