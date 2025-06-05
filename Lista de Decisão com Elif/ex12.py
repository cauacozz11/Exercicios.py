nota1 = float(input("informe a nota da dua primeira prova: "))
nota2 = float(input("Informe a nota da primeira prova: "))

media =  (nota1 + nota2) / 2 

if media > 9 and media <= 10:
     print("A, APROVADO")
elif media >= 7.5 and media <= 9:
     print("B, APROVADO")
elif media >= 6 and media < 7.5:
     print("C, APROVADO")
elif media >= 4 and media < 6:
     print("D, REPROVADO")
elif media >= 0 and media < 4:
     print("E, REPROVADO")
else:
     print("era entre 0 e 10 animal")