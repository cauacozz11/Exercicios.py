lado1 = float(input("lado 1: "))
lado2 = float(input("lado2: "))
lado3 = float(input("lado3: "))

soma = lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1

if soma:
    if lado1 == lado2 == lado3:
        print("é um triângulo equilátero")
    elif  lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print("é um triângulo isósceles")
    else: 
        print("é um triângulo escaleno") 
else:
    print("esses valores não forma um triângulo")