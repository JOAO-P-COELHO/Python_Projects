def arithmetic_arranger (array, show=False):

    def split(array):
        result = array.split(' ')
        return result

    resultado = list(map(split, array))

    i = 0
    n = len(resultado)
    
    while i < n:
        j=0
        print(resultado[i][j],resultado[i+1][j],resultado[i+2][j],resultado[i+3][j],resultado[i+4][j],resultado[i+5][j])
        j=+1
        
        print(resultado[0][i+1],resultado[1][i+1],resultado[2][1],resultado[3][1],resultado[4][1],resultado[5][1])
        print(resultado[0][2],resultado[1][2])
        print("-----")
        
        i += 1



arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)
