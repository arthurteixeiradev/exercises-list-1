from functions import*

print('''
1 - Verifica número inteiro e retorna True ou False
2 - Verifica se um número é positivo ou negativo
3 - Verifica se um número é ímpar ou par
4 - Calcula média
5 - converte idade em dias
6 - Ordena valores em ordem crescente
7 - Converte segundos em "horas:minutos:segundos"
8 - Verifica se um valor é perfeito
9 - Verifica peso ideal
10 - Verifica se os valores informados formam um triângulo
0 - Sair
''')

menu = int(input('Digite a opção: '))
while menu != 0:
    if menu == 1:
        n = int(input('Digite um número: '))
        print('Seu número é:', trueOrFalse(n))

    elif menu == 2:
        n1 = int(input('Digite um algo: '))
        print(positivoNegativo(n1))

    elif menu == 3:
        n2 = int(input('Digite um algo: '))
        print(parImpar(n2))

    elif menu == 4:
        nota1 = float(input('Digite sua primeira nota: '))
        nota2 = float(input('Digite sua segunda nota: '))
        nota3 = float(input('Digite sua terceira nota: '))
        letra = input('Média aritmetica (A)\nMédia ponderada (P)\nDigite o método: ')
        print(media(letra, nota1, nota2, nota3))

    elif menu == 5:
        idadeAno = int(input('Digite a sua idade: '))
        idadeMeses = int(input('Quantos meses: '))
        idadeDias = int(input('Quantos dias: '))
        print('Sua idade em dias é:', age(idadeAno, idadeMeses, idadeDias), 'dias.')

    elif menu == 6:
        num = []
        num.append(int(input("Digite o primeiro número inteiro: ")))
        num.append(int(input("Digite o segundo número inteiro: ")))
        num.append(int(input("Digite o terceiro número inteiro: ")))
        resultado = retornaOrdemNumeros(num)
        print(str(resultado[0]),",",str(resultado[1]),",",str(resultado[2]))

    elif menu == 7:
        segundos = int(input('Segundos: '))
        print(segundosParaTempo(segundos))

    elif menu == 8:
        n = int(input('Digite um número perfeito: '))
        print(validacao(n))

    elif menu == 9:
        alt = float(input('Digite a sua altura: '))
        sexo = input('Qual é o seu sexo: ')
        print('Seu peso ideal é:', pesoIdeal(alt, sexo), 'Kg.')
        
    elif menu == 10:
        x = float(input('Digite o valor do primeiro lado: '))
        y = float(input('Valor do segundo lado: '))
        z = float(input('Valor do terceiro lado: '))
        tri(x, y, z)

    else:
        print('Opção inválida!!')

    menu = int(input('Digite a opção: '))
