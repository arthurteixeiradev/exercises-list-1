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
            print('É um triângulo Escaleno!')
            return
    else: 
        print('Os valora NÃO PODEM formar um triângulo')
        return

x = float(input('Digite o valor do primeiro lado: '))
y = float(input('Valor do segundo lado: '))
z = float(input('Valor do terceiro lado: '))
tri(x, y, z)