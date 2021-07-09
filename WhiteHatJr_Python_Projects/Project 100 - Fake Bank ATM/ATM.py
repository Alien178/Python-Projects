import os

orignalBalance = 50000

def clearScreen():
    os.system("cls")

class ATM:
    global orignalBalance

    def __init__(self, cardnumber, pin):
        self.cardnumber = cardnumber,
        self.pin = pin

    def checkBalance(self):
        print("Your balance is $50,000")

    def withdrawlBalance(self, amount):
        newBalance = orignalBalance - amount
        print("You have withdrawn amount of " + str(amount) + ". Your remaining balance is " + str(newBalance))

def main():
    clearScreen()
    CardNumber = input("Insert your Card Number:\n")
    clearScreen()
    PinNumber  = input("Enter your Pin Number:\n")
    clearScreen()

    newUser =  ATM(CardNumber, PinNumber)

    print("Choose Your Activity ")
    print("--------------------")
    print("1. Balance Enquriy | 2. Withdraw Money")
    print("--------------------------------------")
    activity = int(input("Enter your Choice:\n"))

    if (activity == 1):
        clearScreen()
        newUser.checkBalance()
    elif (activity == 2):
        clearScreen()
        amount = int(input("Enter the Amount:\n"))

        if amount > orignalBalance:
            newUser.checkBalance()
            amount = int(input("Please Enter a Valid Amount:\n"))
            if amount > orignalBalance:
                main()
            else:
                newUser.withdrawlBalance(amount)
        else:
            newUser.withdrawlBalance(amount)

    else:
        print("Enter a Valid Number")
        main()


if __name__ == "__main__":
    clearScreen()
    main()
        