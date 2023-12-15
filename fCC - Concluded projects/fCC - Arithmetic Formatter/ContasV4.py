# READ ME available in this folder

def arithmetic_arranger (array, show=False):
    array_len = len(array)
    
    # Testing if array < 5
    if array_len>5:
        print("Error: Too many problems.")
        return "Error: Too many problems." # Forcing the program to stop, but printing why first
    
    # Function used to split an array so I can evaluate the elements individually
    def split(array): 
        result = array.split(' ')
        return result

    # 
    resultado = list(map(split, array)) # The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.
                                        # map(function, iterables)
                                        # The list converts the map into a list, otherwise it would return something like <map object at 0x034244F0>

    # Testing if the operators are "+" or "-"
    i=0
    while i<array_len:
        if resultado[i][1] != "+" and resultado[i][1] != "-":
            print("Error1: Operator must be '+' or '-'")
            return "Error1: Operator must be '+' or '-'" # Forcing the program to stop, but printing why first
        i = i + 1 

    # Testing if the input is made of numbers (the use of any other characters force the program to stop)
    i=0
    while i<array_len:
        if resultado[i][0].isnumeric() and resultado[i][2].isnumeric(): # Check if this strings is made of numbers
            pass # If so, the program keep running
        else:
            print("Error: Numbers must only contain digits.")
            return("Error: Numbers must only contain digits.") # Forcing the program to stop, but printing why first
        i = i + 1
      
    # Testing if any of the input numbers is bigger than 4 digits - if so, the program stops  
    i=0
    while i<array_len:
        if len(resultado[i][0])<=4 and len(resultado[i][2])<=4:
            pass
        else:
            print("Error: Numbers cannot be more than four digits.")
            return("Error: Numbers cannot be more than four digits.") # Forcing the program to stop, but printing why first
        i = i + 1
    
    print("") # Just formatting the "future input" - a white line at the beginning
    
    # This first loop make the first operands appear align in the same line - also, they have to appear right aligned, that's why blank_size it's created. Depending on the number of digits in the input, the numbers have to be more or less spaced out
    i=0 
    while i<array_len:
        if len(resultado[i][0])>len(resultado[i][2]): # If the first operand has more digits, then, this is the one that defines the number os spaces needed when priting
            blank_size = len(resultado[i][0]) 
        elif len(resultado[i][0])<len(resultado[i][2]): # If the second operand has more digits, then, this is the one that defines the number os spaces needed when priting
            blank_size = len(resultado[i][2])
        elif len(resultado[i][0])==len(resultado[i][2]): # In case the operands have the same length
            blank_size = len(resultado[i][2])
            
        print(resultado[i][0].rjust(blank_size + 2, ' '), end="    ")
        i = i + 1
        
    print("") # This spaces the previous line from the next loop
    
    # This second loop make the operators and the secondo operands appear align in the same line - also, they have to appear right aligned, that's why blank_size it's created. Depending on the number of digits in the input, the numbers have to be more or less spaced out    
    i=0
    while i<array_len:
        if len(resultado[i][0])>len(resultado[i][2]): # Same logic: if the first operand has more digits, it has to be it to decide how many spaces the prints need
            blank_size = len(resultado[i][0]) 
        elif len(resultado[i][0])<len(resultado[i][2]):
            blank_size = len(resultado[i][2])
        elif len(resultado[i][0])==len(resultado[i][2]):
            blank_size = len(resultado[i][2])
            
        print(resultado[i][1].rjust(0, ' '), resultado[i][2].rjust(blank_size, ' '), end="    ")
        i = i + 1
        
    print ("") # This spaces the previous line from the next loop
    
    # The third loop decides how many dashes (-) have to appear - each has to be 2 spaces bigger than the number with the biggest length - also, they have to appear right aligned, that's why dash_size it's created. Depending on the number of digits in the input, the numbers have to be more or less spaced out    
    i=0
    while i<array_len:
        if len(resultado[i][0])>len(resultado[i][2]): # Same logic:
            dash_size = len(resultado[i][0]) + 2
            print((dash_size*"-").ljust(0, ' '), end="    ")
        elif len(resultado[i][0])<len(resultado[i][2]):
            dash_size = len(resultado[i][2]) + 2
            print((dash_size*"-").ljust(0, ' '), end="    ")
        else:
            dash_size = len(resultado[i][2]) + 2
            print((dash_size*"-").ljust(0, ' '), end="    ")
        i = i + 1
        
    print ("") # This spaces the previous line from the next loop
    
    # This fourth loop, if the user decided to have the result shown (show=True) make the result appear align - also, it has to appear right aligned, that's why blank_size it's created. Depending on the number of digits in the input, the numbers have to be more or less spaced out       
    i=0
    while i<array_len:        
        if show==True and resultado[i][1] == "+": # The user decided to see the solution
            operacao = int(resultado[i][0]) + int(resultado[i][2]) # Converts the strings to numbers and do the operation
            operacao_str = str(operacao) # Converts the number to a string so it can be used in the print as a string
            if len(resultado[i][0])>len(resultado[i][2]): # Same logic used for defining the number of spaces
                blank_size = len(resultado[i][0])
            elif len(resultado[i][0])<len(resultado[i][2]):
                blank_size = len(resultado[i][2])
            else:
                blank_size = len(operacao_str)
            print(operacao_str.rjust(blank_size + 2, " "), end="    ")
            
        elif show==True and resultado[i][1] == "-": # The user decided to not see the solution (this is "On" by default)
            operacao = int(resultado[i][0]) - int(resultado[i][2]) # Converts the strings to numbers and do the operation
            operacao_str = str(operacao) # Converts the number to a string so it can be used in the print as a string
            if len(resultado[i][0])>len(resultado[i][2]): # Same logic used for defining the number of spaces
                blank_size = len(resultado[i][0])
            elif len(resultado[i][0])<len(resultado[i][2]):
                blank_size = len(resultado[i][2])
            else:
                blank_size = len(operacao_str)
            print(operacao_str.rjust(blank_size + 2, " "), end="    ")
        i = i + 1 
    
    print("\n") # Just formatting the "future input" - a white line at the end


# Example of use:
arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True) # Each element of the array represents a math operation (+ or -). In this case, he have 5 elements in the array
# It returns the right result and all the elements aligned

## Project dificulty (out of 5): 4,5  
## Time spent: ~12,8 hours
## It passed all the 10 fCC's tests
