base = int(input("Informe a base de um número: "))
expo = int(input("Informe o expoente de um número: "))

resultado = 1
contador = 0

while contador < expo:
    resultado *= base
    contador += 1
    print(resultado)    