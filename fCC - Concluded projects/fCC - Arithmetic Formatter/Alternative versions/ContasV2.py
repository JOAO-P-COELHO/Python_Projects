def arithmetic_arranger (array, show=False):

    def split(array):
        result = array.split(' ')
        return result

    resultado = list(map(split, array)) # The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.
                                        # map(function, iterables)
                                        # The list converts the map into a list, otherwise it would return something like <map object at 0x034244F0

    array_len = len(array)
    j=0
    while j<3:
        i = 0
        while i<array_len:
            # print(resultado[i][j], end=" ") 
            teste = resultado[i][j]
            print()

            print(teste.rjust(5, ' '), end = " ")
            
            
            
            i = i + 1
        print("") 
        

        
        j = j+1
        if j == 3:
                print(array_len*" ----- ") 
    print ( array_len*" ----- ") 
    
    # if show==True and resultado[1] == "+":
    #     operacao = int(result[0]) + int(result[2])
    #     print(operacao)
    # elif show==True and resultado[1] == "-":
    #     operacao = int(result[0]) - int(result[2])
    #     print (f"{operacao} \n")
    # print("")  
    

                                                # [['32' , '+'    , '698'] , ['3801',  '-'   ,  '2']  , ['45'  ,  '+'   , '43']]
                                                # [0][0] , [0][1] , [0][2] , [1][0] , [1][1] , [1][2] , [2][0] , [2][1] , [2][2]

                                                #  i  j  i+1 j  i+2 j
                                                # [0][0] [1][0] [2][0]
                                                # [0][1] [1][1] [2][1]
                                                # [0][2] [1][2] [2][2]
    # print(resultado)
    # print(resultado[0])
    # print(resultado[0][0])

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)
