#Ex5
def age(idadeAno, idadeMeses, idadeDias):
    idadeAno = idadeAno * 360
    idadeMeses = idadeMeses * 30
    resultadoIdade = idadeAno + idadeMeses + idadeDias
    return resultadoIdade
    
idadeAno = int(input('Digite a sua idade: '))
idadeMeses = int(input('Quantos meses: '))
idadeDias = int(input('Quantos dias: '))
print('Sua idade em dias é:', age(idadeAno, idadeMeses, idadeDias), 'dias.')