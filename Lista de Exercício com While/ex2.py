conta = 0
soma_p = 0
qnt_n = 0

while conta < 5:
    num = int(input("Informe um número positívo ou negativo: "))
    
    if num > 0:
        soma_p += num
        
    elif num < 0:
        qnt_n += 1 
        
    conta += 1
print(soma_p)
print(qnt_n)           
        
        