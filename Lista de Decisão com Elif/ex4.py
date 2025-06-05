salario = float(input("informe seu salário: "))

if salario <= 280:
    aumento = salario * 0.2
    final = salario + aumento
    print ("Seu salário antes era" ,salario, "teve um percentual de aumento de 20%, o valor de aumento foi de " ,aumento,"e seu salário final é" ,final)
elif salario > 280 and salario <= 700:
    aumento = salario * 0.15
    final = salario + aumento
    print ("Seu salário antes era" ,salario, "teve um percentual de aumento de 15%, o valor de aumento foi de " ,aumento,"e seu salário final é" ,final)
elif salario > 700 and salario <= 1500:
    aumento = salario * 0.1
    final = salario + aumento
    print ("Seu salário antes era" ,salario, "teve um percentual de aumento de 10%, o valor de aumento foi de " ,aumento,"e seu salário final é" ,final)
elif salario > 1500:
    aumento = salario * 0.05
    final = salario + aumento
    print ("Seu salário antes era" ,salario, "teve um percentual de aumento de 5%, o valor de aumento foi de " ,aumento,"e seu salário final é" ,final)