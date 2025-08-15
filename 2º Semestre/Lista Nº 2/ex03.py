while True:
    idade = int(input('Digite a idade da pessoa: [0 para sair]: '))
    if idade == 0:
        break
    else:
        if 0 < idade <= 12:
            print('Criança')
        elif 12 < idade <= 17:
            print('Adolescente')
        elif 17 < idade <= 59:
            print('Adulto')
        else:
            print('Idoso')    
                   