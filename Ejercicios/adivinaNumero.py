from random import randint
def crearNumero(a,b):
    if a and b != 0:
       return randint(a,b)
    else:
        print("Se ingreso cero es invalido")
        return intento == 0
try:
    i = 0
    menor = int(input("Ingrese numero menor del rango diferente de 0 "))
    mayor = int(input("Ingrese numero mayor del rango "))
    numero = crearNumero(menor,mayor)
    print("Comienza el juego! Intenta adivinar el número para rendirse escribe 0")
    intento = 1
    misIntentos = []
    while intento != 0:
        i +=1
        print("Intento "+str(i)+":")
        intento = int(input(" "))
        if intento > numero:
            print("Es más pequeño")
        if intento < numero:
            print("Es más grande")
        if intento in misIntentos:
            print("Ya se ingreso este numero")
            pass
        else:
            misIntentos.append(intento)
        if intento == numero:
            print("Has ganado con "+str(i)+" intento(s))")
            print("El número era "+str(numero))
            break
        else:
            print("Prueba de nuevo")
            continue
except:
    print("Algo salió mal")