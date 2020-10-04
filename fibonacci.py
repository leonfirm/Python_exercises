# Sequência de Fibonacci
Nant = 1
Fibonacci = 0
n = int(input('Número de termos da sequência: '))
while n >= 0:
    print(f'{Fibonacci}', end=' → ')
    Fibonacci = Fibonacci + Nant
    Nant = Fibonacci - Nant
    n -= 1
print('FIM')
