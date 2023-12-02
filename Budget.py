class Category:
    ledger = []
    
    def deposit(self, amount, description=""):
        self.ledger.append({"amount":amount , "description": description})
        print("Isto chamou o deposit method")
    
    def withdraw(self, amount, description=""): 
        self.ledger.append({"amount":-amount , "description": description})
        print("Isto chamou o withdraw method")
        # If there are not enough funds, nothing should be added to the ledger. 
        # This method should return True if the withdrawal took place, and False otherwise.
    
    def get_balance(self):
        return(self)
        # A get_balance method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
    
    def transfer(self, amount, category_destination):
        
        
    
category = Category() # Initiating the class Category

class food(Category):
    def speak(self):
        print ("Ele usa a tromba")
        

class clothing(Category):
    def speak(self):
        print ("subclasse clothing")
        

class entertainment(Category):
    def speak(self):
        print ("subclasse entertainment")

clothing = clothing() # Initiating the sub-class clothing

category.deposit(100, "Depósito inicial") # Calling the method "deposit" and giving it parameters. This method will change the "ledger" variable
print(category.ledger) # Because I gave parameters do the previous method, ledger variable now prints "[{'amount': 100, 'description': 'Depósito inicial'}]" - its no longer empty, after the line I wrote before
        
clothing.speak()