# Pode existir triângulo?
lado1 = float(input('Digite o primeiro lado do triângulo: '))
lado2 = float(input('Digite o segundo lado do triângulo: '))
lado3 = float(input('Digite o terceiro lado do triângulo: '))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print('As 3 medidas formam um triângulo.')
else:
    print('Impossível fazer um triângulo.')
