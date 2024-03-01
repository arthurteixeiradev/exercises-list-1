#Ex3
def parImpar(n2):
    if n2 % 2 == 0:
        return 'Número par'
    else:
        return 'Número ímpar'

n2 = int(input('Digite um algo: '))
print(parImpar(n2))