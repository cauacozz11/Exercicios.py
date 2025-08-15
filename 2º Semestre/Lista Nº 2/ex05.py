lista = []
soma = 0
maior = menor = None
while True:
    nota = int(input('Digite uma nota [nota negativa para sair do loop]: '))
    if nota < 0:
        break
    soma += nota
    lista.append(nota)
    if maior == None or nota > maior:
        maior = nota
    if menor == None or nota < menor:
        menor = nota
media = soma / len(lista)

print(f'A soma das notas foi {soma}, a maior nota foi {maior}, a menor foi {menor} e a média foi {media}')