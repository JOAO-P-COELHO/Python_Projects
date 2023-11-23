def my_decorator(func): # This will be the function that uses other function, it's the decorator of another function. PS: by using a decorator, the argument on it, it's always a function
    def wrapper(): # Everybody writes this as "wrapper", because this is a wrapping function, it's important because of its return, without this wrapper function, there wouldn't be a way of returning what it's happening inside of the wrapper(), since it's inside of other function, mydecorator()
        print("This will be the first line") # Prints something
        func() #Calls the function "myfunc", in this case - since it's "myfunc()" that was passed as an argument
        print("This will be the third line") # This also prints something
    return wrapper # It returns everything thats inside of the my_decorator, even if its outside of "def wrapper()", because with @my_decorator, everything it's called

@my_decorator # It calls mydecorator and gives it myfunc() as argument in "(func)"" - we simply use the "@" before the element we would like to decorate
def myfunc(): # This is a regular function, "the decorated function"
    print("This will be the second line") # This is a regular printing
    
myfunc() # In the end, by calling myfunc(), I'm also calling the decorator element

# In practise, a function (in this case, myfunc()) will be used in another function (my_decorator()), by using the "@" before it's written.
# This function (myfunc()) will be used in the function called, in this case mydecorator()

######## In the end, by calling myfunc(), I'm also calling the decorator element (this decorator takes a function as an argument)