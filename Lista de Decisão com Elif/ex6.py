num = int(input("Informe um número inteiro até 1000: "))



if num >= 1000 or num < 0:
    print("o número é inválido")
else:
    cent = num // 100
    dez = (num % 100) // 10
    uni = num % 10
    if cent > 0 and dez > 0 and uni > 0:
        print(f"{cent} centenas,{dez} dezenas e {uni} unidades")
        
    elif cent > 0 and dez > 0 and uni == 0:
        print(f"{cent} centenas e {dez} dezenas")
        
    elif cent > 0 and dez == 0 and uni > 0:
        print(f"{cent} centenas e {uni} unidades")
        
    elif cent == 0 and dez > 0 and uni > 0:
        print(f"{dez} dezenas e {uni} unidades")
        
    elif cent == 0 and dez == 0 and uni > 0:
        print(f"{uni} unidades")
        
    elif cent == 0 and dez > 0 and uni == 0:
        print(f"{dez} dezenas")    
        
    elif cent > 0 and  dez == 0 and uni == 0:
        print(f"{cent} centenas")