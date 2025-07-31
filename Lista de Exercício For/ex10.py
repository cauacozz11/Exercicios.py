homem = []
mulher = []
menor = 0
velho = 0
for i in range(4):
    print('Digite 1 para homem\nDigite 2 para mulher')
    
    sexo = int(input('Digite aqui: '))
    nome = str(input('Digite o nome:'))
    idade = int(input('Digite a idade: '))
    
    if sexo == 1:
        
        homem.append(idade)
        
        if idade > velho:
            
            velho = idade
            nome_final = nome
        
    elif sexo == 2:
        
        mulher.append(idade)
        
        if idade < 20:
            menor += 1
            
soma_home = sum(homem)   
soma_mulher = sum(mulher)  

total_pessoas = len(homem) + len(mulher)
soma_geral = (soma_home + soma_mulher)  / total_pessoas 

print(f'A média de idade é {soma_geral},o homem mais velho se chama {nome_final} e sua idade é {velho} existem {menor} mulheres menores de 20 anos')
        