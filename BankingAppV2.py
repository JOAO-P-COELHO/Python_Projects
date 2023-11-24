# Banking App - Final project

class Banking_App:
    
    balance_value = 0.00
                        
    def __init__(self):  
        while True:
            operation = input("\nWhat kind of operation you would like to do: Withdrawl (W) or Deposit?(D)? Press (L) to leave.   ")
            operation = operation.lower()
            if operation == "withdrawl" or operation =="w" :
                self.withdrawl()
            elif operation == "deposit" or operation =="d":
                self.deposit()   
            elif operation == "leave" or operation =="l":
                break          
            else:
                print("You didn't choose a valid operation")

    def deposit(self):
        deposit_value = input("What it's the value? ")
        deposit_value = float(deposit_value)
        with open("transaction_history.txt", "a") as transaction:
            transaction.write(f"The deposit value is: {deposit_value}$\n")
            self.balance_value += deposit_value
            transaction.write(f"Your balance is now: {self.balance_value}$\n\n")
            print(f"Your balance is now: {self.balance_value}$")    
                                           
    def withdrawl(self):
        withdrawl_value = input("What it's the value? ")
        withdrawl_value = float(withdrawl_value)
        with open("transaction_history.txt", "a") as transaction:
            transaction.write(f"The withdrawl value is: {withdrawl_value}$\n")
            self.balance_value -= withdrawl_value
            transaction.write(f"Your balance is now: {self.balance_value}$\n\n")
            print(f"Your balance is now: {self.balance_value}$") 
                               
app = Banking_App()   

    

