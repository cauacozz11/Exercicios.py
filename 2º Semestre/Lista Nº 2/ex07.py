print('PROGRAMA DE CADASTRO')
print()

lista = []

while True:
    print('1 - Incluir contato\n2 - Alterar contato\n3 - Excluir contato\n4 - Listar contato\n5 - Sair')
    while True:
        try:
            opcao = int(input('Digite a sua opção: '))
            if opcao in (1, 2, 3, 4, 5):
                break
            print('ERRO! Digite um número válido')
        except ValueError:
            print("ERRO! Digite apenas números!")

    if opcao == 5:
        print("Saindo do programa...")
        break
    elif opcao == 1:
        nome = input('Digite o nome do usuário: ')
        while True:
            try:
                numero = int(input('Digite o número do usuário: '))
                numeros_cadastrados = lista[1::2]
                if numero not in numeros_cadastrados:
                    break
                print('Esse número já foi cadastrado por outro usuário!')
            except ValueError:
                print("ERRO! Digite apenas números!")
        lista.append(nome)
        lista.append(numero)
        print("Contato cadastrado com sucesso!")
    elif opcao == 2:
        if not lista:
            print("Nenhum contato cadastrado!")
        else:
            try:
                indice = int(input('Digite o índice do contato que quer alterar (nome): '))
                if 0 <= indice < len(lista) and indice % 2 == 0:
                    lista[indice] = input('Digite a alteração do nome: ')
                    print("Nome alterado com sucesso!")
                else:
                    print('Índice inválido ou não é um nome!')
            except ValueError:
                print("ERRO! Digite apenas números!")
    elif opcao == 3:
        if not lista:
            print("Nenhum contato cadastrado!")
        else:
            try:
                numero_excluir = int(input('Digite o número do usuário que você quer excluir: '))
                if numero_excluir in lista:
                    idx = lista.index(numero_excluir)
                    del lista[idx - 1]
                    print("Contato excluído com sucesso!")
                else:
                    print('Número não encontrado!')
            except ValueError:
                print("ERRO! Digite apenas números!")
    elif opcao == 4:
        if not lista:
            print("Nenhum contato cadastrado!")
        else:
            print("\nLista de contatos:")
            for i in range(0, len(lista), 2):
                print(f'Nome: {lista[i]}     Número: {lista[i+1]}')
            print()
