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

segundos = int(input('Segundos: '))
print(segundosParaTempo(segundos))
