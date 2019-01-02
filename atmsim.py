'''This creates a simple bank ATM simulation'''

# Print welcome message
def welcome():
    print("Hello! Welcome to Python Bank!")

# User login
def memLogin():
    uLog = input("Please enter your member number: ")
    uPass = input("Please enter your password: ")
    returnList = [uLog, uPass]
    return returnList

# User verify
def memData(x):
    uMemNum = x[0]
    uPassword = x[1]
    memNum = 12345678
    password = 5335000
    if int(uMemNum) == int(memNum) and int(uPassword) == int(password):
        return True
    elif int(uMemNum) != int(memNum) or int(uPassword) != int(password):
        print("Error! Please contact the system administrator.")

# Main navigation screen
def memScreen():
    print("To check your balance press 1")
    print("To make a deposit press 2")
    print("To make a withdrawal press 3")
    print("To logout press 4")
    uInput = input("Enter your selection: ")
    uInput = int(uInput)
    if uInput <= 0 or uInput > 4:
        print("Error! Invalid selection. Please choose again.")
    elif uInput == 1:
        processOptions(1)
    elif uInput == 2:
        processOptions(2)
    elif uInput == 3:
        processOptions(3)
    elif uInput == 4:
        processOptions(4)

# Process user choice from navigation screen
def processOptions(x):
    if x == 1: # Check Balance
        print(accountBalance)
        memScreen()
    elif x == 2: # Make a Deposit
        makeDeposit()
        memScreen()
    elif x == 3: # Make a Withdrawal
        makeWithdrawal()
        memScreen()
    elif x == 4: # Logout
        print("Goodbye!")
    else: print("Oops")

# Make a deposit
def makeDeposit():
    depositAmount = input("Enter the amount to deposit: ")
    depositAmount = float(depositAmount)
    global accountBalance 
    accountBalance = accountBalance + depositAmount
    print(accountBalance)

# Make a withdrawal
def makeWithdrawal():
    withdrawalAmount = input("Enter the amount to withdraw: ")
    withdrawalAmount = float(withdrawalAmount)
    global accountBalance 
    accountBalance = accountBalance - withdrawalAmount
    print(accountBalance)

# Main()
def main():
    welcome()
    uLoginList = memLogin()
    memData(uLoginList)
    loginSuccess = memData(uLoginList)
    if loginSuccess == True:
        memScreen()
    
# Execute main() and initialize global variable
accountBalance = float(1000.00)
main()