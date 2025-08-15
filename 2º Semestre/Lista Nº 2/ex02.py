from random import randint
lista = []

for i in range(0,5):
    lista.append(randint(1,100))
    
maior = 0

for i in lista:
    if i > maior:
        maior = i

print(f'O maior número da lista {lista} é o número {maior}')        