from random import randint
num = randint(1,100)

while True:
    palp = int(input('Adivinhe o número que o programa sorteou: '))
    if palp < num:
        print('O número sorteado é maior')
    elif palp > num:
        print('O número é menor')
    elif palp == num:
        print('ACERTOU!')
        break        