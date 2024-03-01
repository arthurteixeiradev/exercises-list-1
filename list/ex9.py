#Ex9
def pesoIdeal(alt, sexo):
    if sexo == 'masculino':
        peso = 72.7 * alt - 58
        peso = round(peso, 2)
        return peso
    else:
        peso = 62.1 * alt - 44.7
        peso = round(peso, 2)
        return peso

alt = float(input('Digite a sua altura: '))
sexo = input('Qual é o seu sexo: ')
print('Seu peso ideal é:', pesoIdeal(alt, sexo), 'Kg.')