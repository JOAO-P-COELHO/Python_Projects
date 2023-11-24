# Banking App - Final project

while True:
    transaction = open("transaction_history.txt", "a")
    
    class Banking_App:

        def __init__(self, withdrawl_value=0.00, deposit_value=0.00):
            
            withdrawl_value=0.00
            deposit_value=0.00
            balance=0.00
            
            

            operation = input("What kind of operation you would like to do: Withdrawl (W) or Deposit?(D)?  ")
            operation = operation.lower()

            if operation == "withdrawl" or operation =="w" :
                self.withdrawl()
            elif operation == "deposit" or operation =="d":
                self.deposit()        
            else:
                print("You didn't choose a valid operation")
        
            balance = withdrawl_value + deposit_value
            print(balance)
                                    
        def withdrawl(self):
                withdrawl_value = input("What it's the value? (Use CTRL+C to stop this loop) ")
                withdrawl_value = int(withdrawl_value)
                transaction.write(f"The withdrawl value is: {withdrawl_value}$\n")
                                                              
                self.__init__(withdrawl_value)
                return withdrawl_value
        
        def deposit(self):
                deposit_value = input("What it's the value?  (Use CTRL+C to stop this loop) ")
                deposit_value = int(deposit_value)
                transaction.write(f"The deposit value is: {deposit_value}$\n")
                
                self.__init__(deposit_value)
                return deposit_value
            
    app = Banking_App()   

    

