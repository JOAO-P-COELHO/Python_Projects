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
        
 #       
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

    first_cat = 900 - business.get_balance()
    second_cat = 900 - food.get_balance()
    third_cat = 900 - entertainment.get_balance()
    sum_cat = first_cat + second_cat + third_cat

    first_cat_per = int(((first_cat / sum_cat)*100)/10) + 1
    array_first =[]
    number_of_spaces= 11 - first_cat_per
    array_first.append(" " *number_of_spaces)
    array_first.append("o" * first_cat_per)
    
    resultList_first = []   
    
    # Traversing in till the length of the input list of lists
    for m in range(len(array_first)):
        # using nested for loop, traversing the inner lists
        for n in range (len(array_first[m])):
            # Add each element to the result list
            resultList_first.append(array_first[m][n]) 
        
    second_cat_per = int(((second_cat / sum_cat)*100)/10) + 1
    
    array_second =[]
    number_of_spaces= 11 - second_cat_per
    
    array_second.append(" " *number_of_spaces)
    array_second.append("o" *second_cat_per)
   
    resultList_second = []

    # Traversing in till the length of the input list of lists
    for m in range(len(array_second)):
        # using nested for loop, traversing the inner lists
        for n in range (len(array_second[m])):
            # Add each element to the result list
            resultList_second.append(array_second[m][n])
            
            
    third_cat_per = int(((third_cat / sum_cat)*100)/10) + 1
    
    array_third =[]
    number_of_spaces= 11 - third_cat_per
    array_third.append(" " *number_of_spaces)
    array_third.append("o" * third_cat_per)
   
    resultList_third = []
    

    # Traversing in till the length of the input list of lists
    for m in range(len(array_third)):
        # using nested for loop, traversing the inner lists
        for n in range (len(array_third[m])):
            # Add each element to the result list
            resultList_third.append(array_third[m][n])
     
     
    third_word= []
    for element in entertainment.category:
        third_word.append(element)  
            
    first_word= []
    for element in business.category:
        first_word.append(element)
        dif_len=len(third_word)-len(first_word)
        
    n=0 
    while dif_len>n:                       
        first_word.append(" ")
        n = n + 1   
    
    
    second_word= []
    for element in food.category:
        second_word.append(element)
        dif_len=len(third_word)-len(second_word)
        
    n=0 
    while dif_len>n:                       
        second_word.append(" ")
        n = n + 1  
      

    
    print(first_word)
    print(second_word)
    print(third_word)
    
    print("Percentage spent by category")
    percentage_array = ["100|","90|","80|","70|","60|","50|","40|", "30|", "20|", "10|", " 0|"]
    n=0
    while n<11:
        print(percentage_array[n].rjust(4),resultList_first[n], "",resultList_second[n],"", resultList_third[n])
        n = n + 1
    print("    ----------")
    
    n=0
    while n < len(third_word):
        print("    ",first_word[n],"",second_word[n],"", third_word[n])
        n = n + 1
        
        
# THIS HAS TO BE ALWAYS IN THE TESTS!!!!
food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")


food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
    
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)

actual = create_spend_chart([business, food, entertainment])
print("Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  ")
