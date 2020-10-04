# Jokenpo
from random import randint as rd
from time import sleep
jogo = ('PEDRA', 'PAPEL', 'TESOURA')
print('=-' * 5)
print('JO KEN PÔ')
print('=-' * 5)
print('''Sua opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
try:
    player = int(input('Qual é a sua jogada?'))
    pc = rd(0, 2)
except ValueError:
    print('\033[1;31mVocê só possui 3 opções:\033[m\n[0] PEDRA\n[1] PAPEL\n[2] TESOURA\nESSA OPÇÃO NÃO EXISTE!')
    raise SystemExit(0)

print('JO!')
sleep(0.25)
print('KEN!!')
sleep(0.25)
print('PÔ!!!')

try:
    print('=-' * 13)
    print(f'O computador jogou {jogo[pc]}!\nVocê jogou {jogo[player]}!')
    print('=-' * 13)
except IndexError:
    print('\033[1;31mOPÇÃO INVÁLIDA\033[m')
    print('=-' * 13)
    raise SystemExit(0)


if player == pc:
    print('EMPATE!')
elif (player == 0 and pc == 1) or (player == 1 and pc == 2) or (player == 2 and pc == 0):
    print('Você PERDEU!')
else:
    print('Você GANHOU!')
