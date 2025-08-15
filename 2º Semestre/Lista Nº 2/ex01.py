lista = []
for i in range(0,5):
    num  = int(input('Digite um número: '))
    lista.append(num)

escolha = int(input('Digite o número que deseja procurar: '))

if escolha not in lista:
    print(f'O número {escolha} não está na lista')
else:
    print(f'O número {escolha} está na lista')    

