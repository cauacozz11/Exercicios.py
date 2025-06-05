import unicodedata

def remover_acentos(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )
cartao = input("Você possui o cartão do mercado Tabajara, responda com SIM ou NÃO: ")
cartao = remover_acentos(cartao.strip().upper())

if cartao == "NAO":
    print("Você não tera desconto")
    compra = float(input("Informe a quantidade de carne em Kg que deseja comprar: "))
    if compra <= 5:
        carne = int(input("Qual carne deseja comprar? Digite 1 para Filé duplo, 2 para Alcatra e 3 para picanha: "))
        if carne == 1:
            filee = 24.90
            preco = compra * filee
            print(f"Você comprou {compra}Kg de Filé Duplo, o preço total é de {preco}, você não pagou com o cartão tabajara e por isso não ganhou 5% de desconto e o preço final é de {preco}")
        elif carne == 2:
            alcatra = 25.90
            preco = compra * alcatra
            desconto = preco * 0.05
            final = preco - desconto
            print(f"Você comprou {compra}Kg de Filé Duplo, o preço total é de {preco}, você não pagou com o cartão tabajara e por isso não ganhou 5% de desconto e o preço final é de {preco}")
        else:
            picanha = 46.90    
            preco = compra * picanha
            print(f"Você comprou {compra}Kg de Filé Duplo, o preço total é de {preco}, você não pagou com o cartão tabajara e por isso não ganhou 5% de desconto e o preço final é de {preco}")                 
    else:
        carne = int(input("Qual carne deseja comprar? Digite 1 para Filé duplo, 2 para Alcatra e 3 para picanha: "))
        if carne == 1:
            filee = 25.80
            preco = compra * filee 
            
        elif carne == 2:
            alcatra = 26.80
            preco = compra * alcatra
            print(f"Você comprou {compra}Kg de Filé Duplo, o preço total é de {preco}, você não pagou com o cartão tabajara e por isso não ganhou 5% de desconto e o preço final é de {preco}")    
        else:
            picanha = 37.80
            preco = compra * picanha
            print(f"Você comprou {compra}Kg de Filé Duplo, o preço total é de {preco}, você não pagou com o cartão tabajara e por isso não ganhou 5% de desconto e o preço final é de {preco}")       
elif cartao == "SIM":
    print("Você terá um desconto de 5%")
    compra = float(input("Informe a quantidade de carne em Kg que deseja comprar: "))
    if compra <= 5:
        carne = int(input("Qual carne deseja comprar? Digite 1 para Filé duplo, 2 para Alcatra e 3 para picanha: "))
        if carne == 1:
            filee = 24.90
            preco = compra * filee
            desconto = preco * 0.05
            final = preco - desconto
            print(f"Você comprou {carne}Kg de Filé Duplo, o preço total é de {preco}, você pagou com o cartão tabajara e por isso ganhou 5% de desconto e o preço final é de {final}")
        elif carne == 2:
            alcatra = 25.90
            preco = compra * alcatra
            desconto = preco * 0.05
            final = preco - desconto
            print(f"Você comprou {compra}Kg de Alcatra, o preço total é de {preco}, você pagou com o cartão tabajara e por isso ganhou 5% de desconto e o preço final é de {final}")
        else:
            picanha = 46.90
            preco = compra * picanha
            desconto = preco * 0.05
            final = preco - desconto
            print(f"Você comprou {compra}Kg de Picanha, o preço total é de {preco}, você pagou com o cartão tabajara e por isso ganhou 5% de desconto e o preço final é de {final}")                   
    else:
        carne = int(input("Qual carne deseja comprar? Digite 1 para Filé duplo, 2 para Alcatra e 3 para picanha: "))
        if carne == 1:
            filee = 25.80
            preco = compra * filee
            desconto = preco * 0.05
            final = preco - desconto
            print(f"Você comprou {compra}Kg de Filé Duplo, o preço total é de {preco}, você pagou com o cartão tabajara e por isso ganhou 5% de desconto e o preço final é de {final}")
        elif carne == 2:
            alcatra = 26.80
            preco = compra * alcatra
            desconto = preco * 0.05
            final = preco - desconto
            print(f"Você comprou {compra}Kg de Alcatra, o preço total é de {preco}, você pagou com o cartão tabajara e por isso ganhou 5% de desconto e o preço final é de {final}")    
        else:
            picanha = 37.80
            preco = compra * picanha
            desconto = preco * 0.05
            final = preco - desconto
            print(f"Você comprou {compra}Kg de Picanha, o preço total é de {preco}, você pagou com o cartão tabajara e por isso ganhou 5% de desconto e o preço final é de {final}")                 
else:
    print("Essa resposta é inválida")