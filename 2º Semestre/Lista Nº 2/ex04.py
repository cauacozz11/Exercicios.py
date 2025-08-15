lista = []
soma = 0
while True:
    num = int(input('Digite um número: '))
    if num == 0:
        break
    else:
        soma += num
        lista.append(num)
 
 
print(f'A lista inteira é {lista} e sua soma é {soma}')        