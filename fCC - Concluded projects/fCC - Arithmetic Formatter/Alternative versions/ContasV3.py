def arithmetic_arranger (array, show=False):
    array_len = len(array)
    
    if array_len>5:
        return "Error: Too many problems."
    
    def split(array):
        result = array.split(' ')
        return result

    resultado = list(map(split, array)) # The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.
                                        # map(function, iterables)
                                        # The list converts the map into a list, otherwise it would return something like <map object at 0x034244F0

    i=0
    while i<array_len:
        if resultado[i][1] != "+" and resultado[i][1] != "-":
            return("Error1: Operator must be '+' or '-'")
        i = i + 1 

    i=0
    while i<array_len:
        if resultado[i][0].isnumeric() and resultado[i][2].isnumeric():
            pass
        else:
            return("Error: Numbers must only contain digits.")
        i = i + 1
        
    i=0
    while i<array_len:
        if len(resultado[i][0])<=4 and len(resultado[i][2])<=4:
            pass
        else:
            return("Error: Numbers cannot be more than four digits.")
        i = i + 1
    
    i=0 # Primeiro número
    while i<array_len:
        print(resultado[i][0].rjust(7, ' '), end=" ")
        i = i + 1
    print("")
    
    i=0# Sinal e segundo número
    while i<array_len:
        print(resultado[i][1].ljust(0, ' '), resultado[i][2].rjust(5, ' '), end=" ", )
        i = i + 1
    print ("")
    
    i=0
    while i<array_len:
        print("-------".ljust(7, ' '), end=" ", )
        i = i + 1
    
    print ("")
    i=0
    while i<array_len:        
        if show==True and resultado[i][1] == "+":
            operacao = int(resultado[i][0]) + int(resultado[i][2])
            print(str(operacao).rjust(7, " "), end=" ")
        elif show==True and resultado[i][1] == "-":
            operacao = int(resultado[i][0]) - int(resultado[i][2])
            print(str(operacao).rjust(7, " "), end=" ")
    
        i = i + 1 

# def raciciocio_matematico:
    # [['32' , '+'    , '698'] , ['3801',  '-'   ,  '2']  , ['45'  ,  '+'   , '43']]
    # [0][0] , [0][1] , [0][2] , [1][0] , [1][1] , [1][2] , [2][0] , [2][1] , [2][2]

    #  i  j  i+1 j  i+2 j
    # [0][0] [1][0] [2][0]
    # [0][1] [1][1] [2][1]
    # [0][2] [1][2] [2][2]

x = arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)

# print("\n this is returning:", x)
