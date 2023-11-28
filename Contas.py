def arithmetic_arranger (array, show=False):
    i = 0
    while i < len(array):
        div=array[i]
        result = div.split(' ')

        print(f"{result[0].rjust(5)}")
        print(f"{result[1]} {result[2]}")
        print("-----")
        
        # print("-----", end="-")
        if show==True and result[1] == "+":
            operacao = int(result[0]) + int(result[2])
            print(operacao)
        elif show==True and result[1] == "-":
            operacao = int(result[0]) - int(result[2])
            print (f"{operacao} \n")
        print("")  
        i += 1

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)