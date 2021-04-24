# ***Register***
# - First Name Last Name, Email, Password.
# - Generate account for user

# ***Login***
# - account Number and password

# ***bank operations***
# - Deposit
# - Withdrawal
# - Complain  
# - Logout

#Generate Complaint ID

import random


#system initializing
database = {} #dictionary

def login():
    print('============= Login =============')

    userAccountNumber = int(input('Enter your account Number: \n'))
    password = input('Enter password: \n')

    for accountNumber, userDetails in database.items():
        if(accountNumber == userAccountNumber):
            if(userDetails[3] == password):
                bankOperation(userDetails)
            else:
                print('Incorrect password')
        else:
            print('Invalid Account Number')
            
    print('please login to continue')
    login()
    

def register():
    print('========== Register ==========')

    email = input('Enter a functional email address: \n')
    firstName = input('What is your First Name? \n')
    lastName = input('What is your Last Name? \n')
    password = input('Create your own unique password: \n')
             
    accountNumber = generateAccountNumber()

    database[accountNumber] = [ firstName, lastName, email, password ]

    print('Your account Number has been generated')
    print('/////////////////////////////////////////')
    print('Your account Number is: %d' % accountNumber)
    print('Kindly keep it safe')
    print('/////////////////////////////////////////')

    login()

def bankOperation(user):
    print('Welcome %s %s ' %(user[0], user[1]))
    selectedOption = int(input('What would you like to do? \t 1.Deposit \t 2.Withdrawal \t 3.Complain \t 4. Logout \n'))

    if selectedOption == 1:

        depositOperation()
        
    elif selectedOption == 2:
        
        withdrawalOperation()
        
    elif selectedOption == 3:

        complain()

    elif selectedOption == 4:
        
        print('You are now logged out. Please login to continue')
        login()
        
    else:
        print('Invalid Option Selected. Try again')
        bankOperation(user)


def depositOperation():
    option1 = int(input('How much would you like to Deposit? \n'))
    print('Tansaction Proccessing...')
    print('Available Balance is: %s' % option1)

def withdrawalOperation():
    option2 = int(input('How much would you like to withdraw? \n'))
    print('Transaction Processing...')
    print('Take your Cash')

def complain():
    complainFromUser = input('What issue would you like to report? \n')
    print('Your complaint have been logged in with ID number: ', random.randint(10000, 1000000))

    #create account number for user
def generateAccountNumber():
    return random.randrange(1111111111, 9999999999)

def logout():
    print('You are now logged out.')
    login()
    
def main():
    print('Welcome to Eccom Banking System')
    haveAccount = int(input('Do you have account with us? \t 1.Yes \t 2.No \n'))

    if(haveAccount == 1):
        login()

    elif(haveAccount == 2):
        register()

    else:
        print('You have selected an invalid option')
        main()

#ACTUAL BANKING PROCCESS
main()
                      
