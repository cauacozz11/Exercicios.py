maior = menor = float(input('Informe o peso da pessoa número 1: '))
for i in range(2,6):
    peso = float(input(f'informe o peso da pessoa número {i}: '))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print(f'O maior peso é {maior} e o menor peso é {menor}')            