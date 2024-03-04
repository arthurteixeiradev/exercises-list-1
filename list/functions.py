#Ex1
def trueOrFalse(n):
    if n > 0:
        return True
    else:
        return False

#Ex2    
def positivoNegativo(n1):
    if n1 > 0:
        return f'O valor {n1} informado é positivo'
    else:
        return f'O valor {n1} informado é negativo'

#Ex3    
def parImpar(n2):
    if n2 % 2 == 0:
        return 'Número par'
    else:
        return 'Número ímpar'

#Ex4   
def media(letra, nota1, nota2, nota3):
    if letra == 'A':
        mediaA = (nota1 + nota2 + nota3) / 3
        resultado = round(mediaA, 2)
        return f'A média aritmética das notas: {nota1}, {nota2}, {nota3} é {resultado}'
    elif letra == 'P':
        mediaP = ((nota1 * 5) + (nota2 * 3) + (nota3 * 2)) / 10
        resultado = round(mediaP, 2)
        return f'A média ponderada das notas: {nota1}, {nota2}, {nota3} é {resultado}'
    else:
        print('Método inexistente!')
        return

#Ex5   
def age(idadeAno, idadeMeses, idadeDias):
    idadeAno = idadeAno * 360
    idadeMeses = idadeMeses * 30
    resultadoIdade = idadeAno + idadeMeses + idadeDias
    return resultadoIdade

#Ex6
def retornaOrdemNumeros(num):
    if len(num) < 2:
        return num
    else:
        pivo = num[0]
        i = 1
        menorQuePivo = []
        maiorQuePivo = []
        while i < len(num):
            if num[i] <= pivo:
                menorQuePivo.append(num[i])
            else:
                maiorQuePivo.append(num[i])
            i+=1
        return retornaOrdemNumeros(menorQuePivo) + [pivo] + retornaOrdemNumeros(maiorQuePivo)

#Ex7    
def segundosParaTempo(seg):
    segRestante = 0
    minutos = 0
    horas = 0
    if seg > 0:
        segRestante = seg % 60
        minutos = int(seg / 60)
    if minutos > 0:
        horas = int(minutos / 60)
        minutos = minutos % 60
    return f'{horas}:{minutos}:{segRestante}'

#Ex8
def validacao(n):
    perfectCount = 0
    count = n - 1
    while count > 0:
        restOfDivision = n % count
        if restOfDivision == 0:
            perfectCount += count
        count -= 1

    return perfectCount == n

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

#Ex10
def tri(x, y, z):
    if x < y + z and y < x + z and y < x + y:
        print('Os valores PODEM formar um triângulo')
        if x == y and x == z:
            print('É um Triângulo Equilátero!')
            return
        elif x == y and x != z:
            print('É um Triângulo Isósceles!')
            return
        else:
            print('É um Triângulo Escaleno!')
            return
    else: 
        print('Os valores NÃO PODEM formar um triângulo')
        return