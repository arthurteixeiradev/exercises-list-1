#Ex2
def positivoNegativo(n1):
    if n1 > 0:
        return f'O valor {n1} informado é positivo'
    else:
        return f'O valor {n1} informado é negativo'

n1 = int(input('Digite um algo: '))
print(positivoNegativo(n1))
