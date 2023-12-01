def split(array):
    result = array.split(' ')
    return result

numbers = ["32 + 698", "3801 - 2"]
resultado = list(map(split, numbers))
print(resultado)

n = len(resultado)

a=0
b=0

while b<3:
    print(resultado[0][b], end = " ")z
    print(resultado[1][b], end = " ")
    b+=1
