prod1 = float(input("Informe o preço do produto 1:" ))
prod2 = float(input("Informe o preço do produto 2:" ))
prod3 = float(input("Informe o valor do produto 3:" ))

if prod1 == prod2 or prod1 == prod3 or prod2 == prod3:
    print("os valores são iguais")     
elif prod2 < prod1 and prod2 < prod3:
    print(prod2)
elif prod3 < prod1 and prod3 < prod2: 
    print(prod3) 
elif prod1 < prod2 and prod1 < prod3:
    print(prod1)