lista = []

for i in range(5):
    letra = input('informe o caracter')
    lis.append(letra)


cont = 0
for i in range(5):
    if lista[i] not in ("a","e","i","o","u"):
        print(lista[i])
        cont += 1

print(f"A quantidade de consonantes é {cont}")            