class Category:

    balance = 0.00 # This is a property. It starts as 0.00 and it's then updated, when methods are called

    def __init__(self, category, ledger = None):
        self.category = category

        if ledger is None:
            self.ledger = [] # The class should have an instance variable called ledger that is a list. If no ledger exists, then it creates it.

    def deposit(self, amount, description = ""):
        self.ledger.append({"amount":amount , "description": description})
        self.balance += amount

    def withdraw(self, amount, description = ""):
        checking = self.check_funds(amount)

        if checking == False:
            return False
        else:
            short_description = description[:23] # It was part of the exercise reduce the numbers of characters until a maximum of 23
            self.ledger.append({"amount":-amount , "description": short_description})
            self.balance -= amount
            return True

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category_destination, description=""):
        if isinstance(category_destination, Category): # Se category_destination for uma instância de Category, ele acessa o atributo category dessa instância.
            category_destination_str = category_destination.category # Presume-se que a classe Category tem um atributo chamado category.
                # category_destination.category: Acessa o valor do atributo category da instância category_destination.
        else:
            category_destination_str = str(category_destination)

        checking = self.check_funds(amount)
        if checking == False:
            return False
        else:
            self.ledger.append({"amount":-amount , "description": "Transfer to " + category_destination_str})
            self.ledger.append({"amount":amount , "Transfer from ": self.category})
            self.balance -= amount
            category_destination.balance += amount
            return True

    def check_funds(self, amount):
        if self.balance - amount < 0.00:
            return False
        if self.balance - amount >= 0.00:
            return True
        
        
    # def __str__(self):
    #     word_len=len(self.category)
    #     num_asterisks=int((30-word_len)/2)

    #     categoria = num_asterisks * "*" + self.category + num_asterisks * "*"
    #     print1a = self.ledger[0]["description"][:23]
    #     print1b = str(self.ledger[0]["amount"]) + ".00"
    #     print2a = self.ledger[1]["description"][:23]
    #     print2b = str(self.ledger[1]["amount"]) 
    #     print3a = self.ledger[2]["description"][:23]
    #     print3b = str(self.ledger[2]["amount"]) + ".00"
    #     total = "Total: " + str(self.balance) 
        
        # # Not the right way to do! This should be done with a loop.
        
        # variable1 = categoria + "\n" + print1a + (23 - len(print1b))* " " + print1b
        # variable2 = print2a + " " + print2b 
        # variable3 = print3a + " " + print3b
        # variablefinal = variable1 + "\n" + variable2 + "\n" + variable3 + "\n" + total
        # # print(variablefinal)
        # return variablefinal


def create_spend_chart(categories): # takes a list of categories as an argument. It should return a string that is a bar chart.

    # print("Percentage spent by category")
    # percentage_array = ["100|","90|","80|","70|","60|","50|","40|", "30|", "20|", "10|", " 0|"]
    # i = 0
    # for element in percentage_array:
    #     print(percentage_array[i])
    #     i = i +1
    
    for category in categories:
        category_name = str(category.category) # São strings
        isto = "".append(category_name)
        print(isto)
        
        
    i = 0
    array_vazio = []
    print(categories[0])
    while i<len(categories):
        print(array_vazio)
        array_vazio.append(category_name)
        i = i + 1
        

        
        # teste = len(categories)
        # print(teste)
        # category_name = str(category.category) # São strings
        
        # size = len(category_name) # a primeira size = 8, 4 e 13
        
        # i = 0
        # while i<size:
        #     # print(f"{category_name[i]}")
        #     i = i + 1

        
        # lista = list(category_name)
        # print (lista)
        
        

    # for category in categories:
    #     if hasattr(category, 'ledger') and category.ledger:
    #         for entry in category.ledger:
    #             if entry["amount"] < 0:
    #                 print(entry)
        
# THIS HAS TO BE ALWAYS IN THE TESTS!!!!
food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")


food.deposit(900, "deposit")
food.withdraw(105.55)

actual = create_spend_chart([business, food, entertainment])
# print("Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  ")
