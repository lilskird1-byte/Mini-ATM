# Creating a an ATM account dictionary
account= {
    "name" :"Stanbic ATM",
    "balance": 1000,
    "pin": "1234",
    "account type": "business account",
}
print("Welcome To Stanbic ATM")
print()
name= input("Enter Your Name :")
print(f"Hello! Dear {name}.")
print()
# Creating PIN for account access
correct_pin= 1234
attempt=0
while attempt<3:
    pin=int(input("Enter account PIN:"))
    if pin==correct_pin:
        print("Acccess Granted")#PIN entered correctly
        break
    else:
        attempt+=1
        print("Invalid PIN")#PIN wrong
    if attempt ==3:
        print("Process Locked!")#Attempts finished so process locked
        quit()
#List of Menu for customer service
while True:
    print("=========ATM MENU==========")
    print("1.Check Balance:")
    print("2.Deposit Money:")
    print("3.Withdraw Money:")
    print("4.Exit")
    print()
    option=(1,2,3,4) # Variable to help customer navigate through the ATM.
    option=int(input("Enter your choice :"))
    if option==1:
        print(f"Account balance:${account["balance"]}")

    elif option==2:
        print("Deposit Money:")#Section where customer enters deposit amount
        amount=int(input("Enter deposit amount :"))
        account["balance"]+=amount
        print("Deposit Successful!")
        print(f"Your new balance is ${account['balance']}")
        print()

    elif option==3:
        print("Withdraw Money:")#Section for money withdrawal
        withdrawal=0
        while withdrawal<=account["balance"]:
            withdrawal=int(input("Enter withdrawal amount: "))
            if withdrawal<=account["balance"]:
                account["balance"]-=withdrawal
                print("Withdrawal Successful!")
                print(f"Your new balance is ${account['balance']}")
                print()
                break
            else:
                print("Insufficient Funds!")#Withdrawal amount has exceeded account balance
                print()
    else:
        option==4 #Program ends with Exit menu
        print("Thanks for Banking with Us")
        quit()
            
   
    












































