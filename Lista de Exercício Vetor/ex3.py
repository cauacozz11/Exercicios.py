# vetorc = []

# for i in range(10):
#     valor = str(input('informe um caracter letra: '))
#     if valor not in ('a','e','i', 'o', 'u'):
#         vetorc.append(valor)
        
# print(vetorc)        

todos = []    
par = []
imp = []

for i in range(1, 6):
    num = int(input(f'Digite o {i} número? '))
    todos.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        imp.append(num)
print(todos)
print(f'pares: {par}')
print(f'impares: {imp}')