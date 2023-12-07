# Banking App - Final project

while True:
    transaction = open("transaction_history.txt", "a")
    
    class Banking_App:
               
        def __init__(self, balance=0.00):
            self.new_value = self.withdrawl
            
            
                                    
        def withdrawl(self):
                withdrawl_value = input("What it's the value? (Use CTRL+C to stop this loop) ")
                withdrawl_value = int(withdrawl_value)
                transaction.write(f"The withdrawl value is: {withdrawl_value}$\n")
                
                # transaction.write(f"Your balance is: {balance}$\n")
                                
                return withdrawl_value
        
        def deposit(self):
                deposit_value = input("What it's the value?  (Use CTRL+C to stop this loop) ")
                deposit_value = int(deposit_value)
                transaction.write(f"The deposit value is: {deposit_value}$\n")
                
                return deposit_value
            
        # Ele não atualiza o valor do initial_amount só com o return!

    operation = input("What kind of operation you would like to do? Withdrawl (W) or Deposit?(D)  ")
    operation = operation.lower()
    app = Banking_App()   

    if operation == "withdrawl" or operation =="w" :
        app.withdrawl()
        # transaction.write(f"O balanço é: {app.initial_amount}$\n")
            
    elif operation == "deposit" or operation =="d":
        pass
        app.deposit()
        # app.__init__(deposit_value)
        # transaction.write(f"O balanço é: {}$\n")
        
    else:
        print("You didn't choose a valid operation") 

