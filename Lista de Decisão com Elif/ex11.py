turno = (input("Informe o turno que você estuda, com M para matutino, V para vespertino e N para noturno: ")).upper()

if turno == "M":
     print("Bom dia!")
elif turno == "V":
     print("Boa Tarde!") 
elif turno == "N":
     print("Boa Noite!")    
else:
     print("Era M, V ou N burro")       


salario = float(input("Informe o seu salário: "))

if salario <= 280:
     valor = salario * 0.2
     salario1 =  salario + valor
     print("Seu salário era: ", salario," Seu percentual de aumento foi de 20%, o valor do seu aumento foi de ", valor, "e seu novo salário é ", salario1)
elif salario > 280 and salario <= 700:
    valor = salario * 0.15
    salario1 =  salario + valor
    print("Seu salário era: ", salario," Seu percentual de aumento foi de 15%, o valor do seu aumento foi de ", valor, "e seu novo salário é ", salario1)
elif salario > 700 and salario <= 1500:
    valor = salario * 0.1
    salario1 =  salario + valor
    print("Seu salário era: ", salario," Seu percentual de aumento foi de 10%, o valor do seu aumento foi de ", valor, "e seu novo salário é ", salario1)
elif salario < 1500:
    valor = salario * 0.05
    salario1 =  salario + valor
    print("Seu salário era: ", salario," Seu percentual de aumento foi de 5%, o valor do seu aumento foi de ", valor, "e seu novo salário é ", salario)