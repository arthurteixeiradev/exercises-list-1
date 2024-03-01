#Ex4
def media(letra, nota1, nota2, nota3):
    if letra == 'A':
        mediaA = (nota1 + nota2 + nota3) / 3
        resultado = round(mediaA, 2)
        mensagem = print('A média aritmética das notas:', nota1, ',', nota2, ',', nota3, 'é', resultado)
        return mensagem
    elif letra == 'P':
        mediaP = ((nota1 * 5) + (nota2 * 3) + (nota3 * 2)) / 10
        resultado = round(mediaP, 2)
        mensagem = print('A média ponderada das notas:', nota1, ',', nota2, ',', nota3, 'é', resultado)
        return mensagem
    else:
        print('Método inexistente!')
        return

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
nota3 = float(input('Digite sua terceira nota: '))
letra = input('Média aritmetica (A)\nMédia ponderada (P)\nDigite o método: ')
media(letra, nota1, nota2, nota3)