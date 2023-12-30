number = int(input('Digite um número inteiro: '))
calc = number % 2
if number == 0:
    print(f'O número {number} é NULO.')
else:
    if calc == 0:
        print(f'O número {number} é PAR.')
    else:
        print(f'O número {number} é ÍMPAR.')
