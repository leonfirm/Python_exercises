# IMC
massa = float(input('Digite seu peso (kg): '))
altu = float(input('Digite sua altura (m): '))
IMC = massa / (altu ** 2)

print(f'Seu IMC é {IMC:.4f}')
if IMC < 18.5:
    print('Você está abaixo do peso, pode comer mais.')
elif 18.5 <= IMC < 25:
    print('Você está no peso ideal. Parabéns!')
elif 25 <= IMC < 30:
    print('Você está no sobrepeso, tente comer menos.')
elif 30 <= IMC < 40:
    print('Você está obeso, experimente uma dieta.')
elif IMC >= 40:
    print('Você está na faixa de obesidade mórbida, faça uma dieta imediatamente!')
