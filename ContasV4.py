def arithmetic_arranger (array, show=False):
    array_len = len(array)
    
    # Testing if array < 5
    if array_len>5:
        print("Error: Too many problems.")
        return "Error: Too many problems."
    
    def split(array):
        result = array.split(' ')
        return result

    resultado = list(map(split, array)) # The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.
                                        # map(function, iterables)
                                        # The list converts the map into a list, otherwise it would return something like <map object at 0x034244F0

    # Testing if the operators are "+" or "-"
    i=0
    while i<array_len:
        if resultado[i][1] != "+" and resultado[i][1] != "-":
            print("Error1: Operator must be '+' or '-'")
            return "Error1: Operator must be '+' or '-'"
        i = i + 1 

    # Testing if the input is numbers (doesn't accept other else)
    i=0
    while i<array_len:
        if resultado[i][0].isnumeric() and resultado[i][2].isnumeric():
            pass
        else:
            print("Error: Numbers must only contain digits.")
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
        if len(resultado[i][0])>len(resultado[i][2]):
            blank_size = len(resultado[i][0])
        elif len(resultado[i][0])<len(resultado[i][2]):
            blank_size = len(resultado[i][2])
        elif len(resultado[i][0])==len(resultado[i][2]):
            blank_size = len(resultado[i][2])
        
        print(resultado[i][0].rjust(blank_size + 2, ' '), end="    ")
        i = i + 1
    print("")
    
    i=0 # Sinal e segundo número
    while i<array_len:
        if len(resultado[i][0])>len(resultado[i][2]):
            blank_size = len(resultado[i][0]) 
        elif len(resultado[i][0])<len(resultado[i][2]):
            blank_size = len(resultado[i][2])
        elif len(resultado[i][0])==len(resultado[i][2]):
            blank_size = len(resultado[i][2])
            
        print(resultado[i][1].rjust(0, ' '), resultado[i][2].rjust(blank_size, ' '), end="    ")
        i = i + 1
    print ("")
    
    # Dashes number
    i=0
    while i<array_len:
        if len(resultado[i][0])>len(resultado[i][2]):
            dash_size = len(resultado[i][0]) + 2
            print((dash_size*"-").ljust(0, ' '), end="    ")
        elif len(resultado[i][0])<len(resultado[i][2]):
            dash_size = len(resultado[i][2]) + 2
            print((dash_size*"-").ljust(0, ' '), end="    ")
        else:
            dash_size = len(resultado[i][2]) + 2
            print((dash_size*"-").ljust(0, ' '), end="    ")
        i = i + 1
    print ("")
    
    
    # FIQUEI AQUI - FALTA CORRIGIR A FORMA COMO O ÚLTIMO NUMERO APARECE
    # TESTE QUE FALTAVAM PASSAR:  id='test_two_problems_with_solutions'), e  id='test_five_problems_with_solutions'),
    
    i=0
    while i<array_len:        
        if show==True and resultado[i][1] == "+":
            operacao = int(resultado[i][0]) + int(resultado[i][2])
            operacao_str = str(operacao)
            if len(resultado[i][0])>len(resultado[i][2]):
                blank_size = len(resultado[i][0])
            elif len(resultado[i][0])<len(resultado[i][2]):
                blank_size = len(resultado[i][2])
            else:
                blank_size = len(operacao_str)
            print(operacao_str.rjust(blank_size + 2, " "), end="    ")
            
        elif show==True and resultado[i][1] == "-":
            operacao = int(resultado[i][0]) - int(resultado[i][2])
            operacao_str = str(operacao)
            if len(resultado[i][0])>len(resultado[i][2]):
                blank_size = len(resultado[i][0])
            elif len(resultado[i][0])<len(resultado[i][2]):
                blank_size = len(resultado[i][2])
            else:
                blank_size = len(operacao_str)
            print(operacao_str.rjust(blank_size + 2, " "), end="    ")
    
        i = i + 1 
    
    print("\n")

arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True)
