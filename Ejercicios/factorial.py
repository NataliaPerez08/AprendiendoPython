#Pedir al usuario un número entero, 
#y mostrar la lista de 1 a ese número, 
# junto con el correspondiente factorial. 

def calcu(num):
    if (num==0):
        return 1
    else:
        return(num * calcu(num-1))

num=int(input("Número para factorial: "))
cont = 1
while cont <= num:
    print(str(cont)+" "+str(calcu(cont)))
    cont+=1
