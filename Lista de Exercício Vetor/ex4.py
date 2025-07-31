# media = []
# for i in range(3):
#     n1 = float(input('informe sua nota: '))
#     n2 = float(input('informe sua nota: '))
#     n3 = float(input('informe sua nota: '))
#     n4 = float(input('informe sua nota: '))
#     media69 = (n1 + n2 + n3 + n4)/ 4
    
#     if media69 >= 6:
#         media.append(media69)
# print(media)        

lista = []
n1 = 0
n2 = 0
n3 = 0
n4 = 0

for i in range (1, 4):
    for n in range (1, 5):
        nota = int(input(f'Digite a {n} do {i} aluno: '))
        if n == 1:
            n1 = nota
        elif n == 2:
            n2 = nota
        elif n == 3:
            n3 = nota
        elif n == 4:
            n4 = nota
    media = (n1+n2+n3+n4)/4
    if media >= 6:
        lista.append(media)
print(lista)