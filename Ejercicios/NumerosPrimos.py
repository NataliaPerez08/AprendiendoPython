def evalua(number):
    contador=0
    j=1
    while j <= number:
        if (number%j)==0:
            contador+=1
        j+=1
    if(contador <=2):
        return number
    else:
        return 0

inicio = int(input("Inicio: "))
fin = int(input("Final: "))

print("Números primos desde "+str(inicio)+" al "+str(fin))

while inicio <= fin:
    if (inicio%2)!=0:
        if evalua(inicio) >0 and evalua(inicio)!=1:
            print(" "+str(evalua(inicio)))
        pass
    inicio += 1
    pass

