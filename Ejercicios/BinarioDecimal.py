binario = []
preDecimal = []
def verificaBini(preBini):
    if preBini%2 == 0:
        binario.append("0")
    elif preBini%2 != 0:
        binario.append("1")
#try:
respuesta = int(input("Opciones: \n1.Decimal a binario  2. Binario a decimal"))
if respuesta == 1:
    print("Decimal a binario")
    numero = int(input("Ingrese número: "))
    while (numero >=2):
        preBini = numero%2
        numero = int(numero/2)
        verificaBini(preBini)

    verificaBini(numero)

    cont = len(binario)
    while cont > 0:
        cont -=1
        print(binario[cont], end=' ')
        pass
    pass
elif respuesta ==2:
    print("Binario a decimal")
    binarioI = input("Ingrese número: ")
    print(int(str(binarioI),2))
    
#except:
#    print("Error")