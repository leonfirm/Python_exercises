# Mudança de base
while True:
    ka = int(input('Digite um número inteiro:'))
    print('''Escolha uma base para conversão:
    [ 1 ] converter para BINÁRIO
    [ 2 ] converter para OCTAL
    [ 3 ] converter para HEXADECIMAL
    [ 4 ] Sair''')

    opp = int(input('Sua opção:'))
    if opp == 1:
        print(f'{ka} convertido para BINÁRIO é igual a {ka :b}')  # 0b cortado, poderia usar "bin(ka)" sem cortar
    elif opp == 2:
        print(f'{ka} converitdo para OCTAL é igual a {ka :o}')  # 0o cortado, poderia usar "oct(ka)" sem cortar
    elif opp == 3:
        print(f'{ka} convertido para HEXADECIMAL é igual a {ka :x}')  # 0x cortado, poderia usar "hex(ka)" sem cortar
    elif opp == 4:
        print(f'Até mais :)')
        break
    else:
        print('Opção inválida.')
