valor  = float(input('Digite um valor: '))

if valor > 100:
    por = valor * 0.1
    final = valor - por
    print(f'Sua compra cstava R${valor} e com o desconto ficou R${final}')
else:
    print('A sua conta não tem desconto')    