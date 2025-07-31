import datetime

data = datetime.datetime.now().year

maior = 0
menor = 0

for i in range(7):
    ano = int(input(f'Pessoa número {i}, informe o ano de seu nascimeto: '))
    if data - ano >= 18:
        maior += 1
    else:
        menor += 1
print(f'Existem {maior} pessoas maiores ou iguais a 18 anos, e {menor} menores de 18 anos')            