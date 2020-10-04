# Ano Bissexto

ano = int(input('Ano a ser analisado:\n'))
if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print(f'\033[32m{ano} é bissexto!\033[m')
else:
    print(f'\033[31m{ano} não é bissexto!\033[m')
