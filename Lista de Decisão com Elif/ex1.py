preco1 = float(input("Informe o valor do proiduto 1: "))
preco2 = float(input("Informe o vaor do produto 2: "))
preco3 = float(input("Informe o valor do produto 3: "))

if preco1 < preco2 and preco1 < preco3:
    print(preco1,)
elif preco2 < preco1 and preco2 < preco3:
    print(preco2,) 
else:
    print(preco3,)   