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

num = []
num.append(int(input("Digite o primeiro número inteiro: ")))
num.append(int(input("Digite o segundo número inteiro: ")))
num.append(int(input("Digite o terceiro número inteiro: ")))

resultado = retornaOrdemNumeros(num)
print(str(resultado[0]),",",str(resultado[1]),",",str(resultado[2]))
