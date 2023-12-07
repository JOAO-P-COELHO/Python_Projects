class Category:

    balance = 0.00 # This is a property. It starts as 0.00 and it's then updated, when methods are called

    def __init__(self, category, ledger=None):
        self.category = category

        if ledger is None:
            self.ledger = [] # The class should have an instance variable called ledger that is a list. If none ledger exists, then it creates it.

        word_len=len(category)
        num_asterisks=int((30-word_len)/2)

        print(num_asterisks * "*" + category + num_asterisks * "*" )

    def deposit(self, amount, description=""):
        self.ledger.append({"amount":amount , "description": description})
        self.balance += amount

    def withdraw(self, amount, description=""):
        checking = self.check_funds(amount)

        if checking == False:
            return False
        else:
            self.ledger.append({"amount":-amount , "description": description})
            short_description = description[:23] # It was part of the exercise reduce the numbers of characters until a maximum of 23
            self.balance -= amount
            return True

    def get_balance(self):
        print(f"This is the balance of the {self.category} and it's {self.balance}")
        return self.balance

    def transfer(self, amount, category_destination, description=""):
        if isinstance(category_destination, Category):
            category_destination_str = category_destination.category
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
            print(self.ledger)
            print(self.balance)
            print("isto", category_destination.balance)

        # If there are not enough funds, nothing should be added to either ledgers.
        # This method should return True if the transfer took place, and False otherwise.
            return True

    def check_funds(self, amount):
        if self.balance - amount < 0.00:
            return False
        if self.balance - amount >= 0.00:
            return True
        # It returns False if the amount is greater than the balance of the budget category and returns True otherwise.
        # This method should be used by both the withdraw method and transfer method.


# THIS HAS TO BE ALWAYS IN THE TESTS!!!!
food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")

food.deposit(900, "deposit")
food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")

food_balance_before = food.get_balance()
print("aqui1",food_balance_before)
entertainment_balance_before = entertainment.get_balance()
good_transfer = food.transfer(20, entertainment)
food_balance_after = food.get_balance()
print("aqui2", food_balance_after)
entertainment_balance_after = entertainment.get_balance()
actual = food.ledger[2]
print(actual)




# food.deposit(900, "deposit")
# food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
# food.transfer(20, entertainment)
# actual = str(food)
# print(actual)
# print(f"*************Food*************\ndeposit                 900.00\nmilk, cereal, eggs, bac -45.67\nTransfer to Entertainme -20.00\nTotal: 834.33")


def create_spend_chart(lista): # takes a list of categories as an argument. It should return a string that is a bar chart.
    lists = lista
    print("Percentage spent by category")
    percentage_array = ["100|","90|","80|","70|","60|","50|","40|", "30|", "20|", "10|", " 0|"]
    for element in percentage_array:
        print(element)

# create_spend_chart()

# print(create_spend_chart([food, clothing, auto]))