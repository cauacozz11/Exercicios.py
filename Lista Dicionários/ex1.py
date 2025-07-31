# lista = []

# disc = {}

# for i in range(0,3):
#     disc['nome'] = str(input('Digite o nome de uma pessoa: '))
#     print('-'*30)
#     disc['idade'] = int(input('Digite a idade da pessoa: '))
#     print('-'*30)
#     lista.append(disc.copy())
#     disc.clear()
# cont = 0
# for i in lista:
#     cont += 1
#     print(f"O noma da {cont}º pessoa é {i['nome']} e a idade é {i['idade']}")    
    
    
    
    
# lista = []

# disc = {}

# for i in range(0,3):
#     disc['nome'] = str(input('Digite o nome de uma pessoa: '))
#     print('-'*30)
#     disc['idade'] = int(input('Digite a idade da pessoa: '))
#     print('-'*30)
#     lista.append(disc.copy())
#     disc.clear()    
    
# for i, d in enumerate(lista):
#     print(f"A {i+1}º pessoa: Nome = {d['nome']}, Idade = {d['idade']} ")    



# lista = []
# disc = {}
# mulher = []
# res = 'S'
# soma = 0
# while res == "S":
#     disc['nome'] = str(input('Informe o nome da pessoa: '))
#     disc['idade'] = int(input('Digite a idade da pessoa: '))
#     soma += disc['idade']
#     while True: 
#         disc['sexo'] = str(input('Digite o sexo - [M/F]: ')).upper().strip()[0]
#         if disc['sexo'] in "MF":
#             break
#         print('SEXO INVÁLIDO! TENTE NOVAMENTE')
#     lista.append(disc.copy())
#     disc.clear()
#     while True:
#         res = str(input('Você Deseja continuar? ')).upper().strip()[0]
#         if res in 'SN':
#             break
#         print('ERRO! TENTE NOVAMENTE')

# media = soma / len(lista)     
# print(f"Ao total foram cadastradas {len(lista)} pessoas")

# for m in lista:
#     if m['sexo'] == 'F':
#         mulher.append(m['nome'])

# print(f'As mulheres cadastradas foram {mulher}')        
        

# print('As pessoas com idade acima da média são: ', end='')
# for i in lista:
#     if i['idade'] > media:
#         print(f"{i['nome']} ",end='')
               


lista = []
disc = {}
gols = []

while True:
    gols.clear()
    disc['jogador'] = str(input('Digite o nome do jogador: '))
    disc['jogos'] = int(input('Digite quantos partidas ele jogou: '))
    for i in range(disc['jogos']):
        gols.append(int(input(f"Quantos gols ele fez no {i+1}º jogo: ")))
    disc['gol_por_jogo'] = gols
    lista.append(disc.copy())
    while True:
        res = str(input('Deseja continuar: [S/N]')).upper().strip()[0]
        if res in "SN":
            break
        print('ERRO! ESSA OPÇÃO NÃO EXISTE')
    if res == "N":
        break    
    
print(f'{"TABELA":^15}')
print('-='*45)
print(f'{"Cód":<4} {"Nome":<15} {"Partidas":^10} {"Gols":>5}')
print('-=' * 45)

for i, v in enumerate(lista):
    print(f"{i+1:<4} {v['jogador']:<15} {v['jogos']:^10} {v['gol_por_jogo']}")
    
