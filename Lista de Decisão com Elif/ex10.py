num1 = int(input("informe um número:")) 
num2 = int(input("Informe um número: "))
num3 = int(input("informe um número: "))

if num1 >= num2 and num1 >= num3:
     if num2 >= num3:
         print("a ordem certa é:", num1,num2,num3)
     else:
         print("a ordme certa é:", num1,num3,num2) 
elif num2 >= num1 and num2 >= num3:
     if num1 >= num3:
         print("a ordem certa é:", num2,num1,num3)
     else:
         print("a ordem certa é:", num2,num3,num1) 
elif num3 >= num1 and num3 >= num2:
     if num2 >= num1:
         print("a ordem certa é:", num3,num2,num1)
     else:
         print("a ordem certa é:", num3,num1,num2)