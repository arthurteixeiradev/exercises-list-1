#Ex2
def positivoNegativo(n1):
    if n1 > 0:
        resultado = print('O valor', n1, 'informado é positivo')
        return resultado
    else:
        resultado = print('O valor', n1, 'informado é negativo')
        return resultado

n1 = int(input('Digite um algo: '))
positivoNegativo(n1)