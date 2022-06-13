# Banking system using python-oop
from random import randint

class bank:
    def __init__(self) :
        self.savingAccount={}
    
    def creatAccount(self,name,amount):
        self.accountNumder=randint(10000,99999)
        self.savingAccount[self.accountNumder]=[name,amount]
        print("Account created successfully")
        return self.accountNumder
        
    def authenticate(self,name,accountNumber):
        if accountNumber in self.savingAccount.keys():
            if self.savingAccount[accountNumber][0]==name:
                self.accountNumder=accountNumber
                print("Authentication Successfull")
                return True
            else:
                print("Authentication Faild!")
                print("Acoount-Name is not valid")
                return False
        else:
                print("Authentication Faild!")
                print("Account-Number is not valid")
                return False

    def widral(self,widralAmount):
        if widralAmount > self.savingAccount[self.accountNumder][1]:
            print("Do not have Sufficient Balcne")
            print("Your balance is",self.savingAccount[self.accountNumder][1])
        else:
            self.savingAccount[self.accountNumder][1] -= widralAmount
            print("Widral Successfull")
            print("Now, your balance is",self.savingAccount[self.accountNumder][1])

    def deposit(self,depositAmount):
        self.savingAccount[self.accountNumder][1] += depositAmount
        print("Now, your balance is",self.savingAccount[self.accountNumder][1])

    def displayBalance(self):
        amount = self.savingAccount[self.accountNumder][1]
        print("Your balance is",amount)



if __name__=='__main__':

    while True:
        print("""
        Enter 1 to creat account
        Enter 2 to access account
        Enter 3 to exit
        """)
        val=int(input(">"))
        
        if val==1:
            name=input("Enter your name : ").capitalize()
            amount=int(input("Enter amount for intial Deposit : "))
            print()
            object=bank()
            account_number=object.creatAccount(name,amount)
            print("Your account number is =>",account_number)

        elif val==2:
            name=input("Enter your name : ").capitalize()
            account_number=int(input("Enter your account number : "))
            authentication=object.authenticate(name,account_number)
            if authentication==True:
                while True:
                    print("""
        Enter 4 to Widral amount
        Enter 5 to Deposit amount
        Enter 6 to Display balance
        Enter 7 for previous manue
        """)
                    var=int(input(">"))

                    if var==4:
                        widral_amount=int(input("Enter amount you wnat to widral : "))
                        print()
                        object.widral(widral_amount)
                    elif var==5:
                        deposit_amount=int(input("Enter amount you wnat to Deposit : "))
                        print()
                        object.deposit(deposit_amount)
                    elif var==6:
                        print()
                        object.displayBalance()
                    elif var==7:
                        break
                    else:
                        print("Wrong input!")
                        print("Please enter a valid value")
        
        elif val==3:
            break
        else:
            print("Wrong input!")
            print("Please enter a valid value")