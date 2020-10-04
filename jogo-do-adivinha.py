# Game do adivinhe o número:
from random import randint

computador = randint(1, 5)

print('-=-' * 20)
print('Vou pensar em um número de 1 a 5, tente adivinhar! hahaha')
print('-=-' * 20)

jogador = int(input('Vc pensou em: '))

print(f'Eu pensei em {computador}')

if jogador == computador:
    print('Woww, vc tem sorte hein amigão...')
else:
    print('ERROUUU!!!')
