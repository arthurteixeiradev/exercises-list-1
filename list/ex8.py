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

n = int(input('Digite um número perfeito: '))
print(validacao(n))