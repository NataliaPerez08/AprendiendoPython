#import mat

print("Regla de Cramer Sistema 3x3\r")

print("Ecuacion 1: ")
a1 = input("a: ")
b1 = input("b: ")
c1 = input("c: ")
d1 = input("d: ")
coeA1 = float(a1)
coeB1 = float(b1)
coeC1 = float(c1)
coeD1 = float(d1)

print("Ecuacion 2: ")
a2 = input("a: ")
b2 = input("b: ")
c2 = input("c: ")
d2 = input("d: ")
coeA2 = float(a2)
coeB2 = float(b2)
coeC2 = float(c2)
coeD2 = float(d2)

print("Ecuacion 3: ")
a3 = input("a: ")
b3 = input("b: ")
c3 = input("c: ")
d3 = input("d: ")
coeA3 = float(a3)
coeB3 = float(b3)
coeC3 = float(c3)
coeD3 = float(d3)


# Matriz del sistema
#   coeA1   coeB1    coeC1
#   coeA2   coeB2    coeC2
#   coeA3   coeB3    coeC3

determinanteSis = (coeA1 * coeB2 * coeC3)  +  (coeB1 * coeC2 *coeA3) + (coeA2 * coeB3 * coeC1) - (coeC1 * coeB2 * coeA3)-(coeB1 * coeA2 * coeC3) - (coeC2 * coeB3 * coeA1)

print("Determinante del sistema: "+str(determinanteSis))

if determinanteSis != 0:
    # Matriz de X
    #  coeD1  coeB1  coeC1
    #  coeD2  coeB2  coeC2
    #  coeD3  coeB3  coeC3

    determinanteX = (coeD1 * coeB2 * coeC3) + (coeB1 * coeC2 * coeD3) + (coeD2 * coeB3 * coeC1) - (coeC1 * coeB2 * coeD3) -  (coeB1 * coeD2 * coeC3) -  (coeC2 * coeB3 * coeD1)
    print("Determinante de X: "+str(determinanteX))

    # Matriz de Y
    #  coeA1  coeD1  coeC1
    #  coeA2  coeD2  coeC2
    #  coeA3  coeD3  coeC3

    determinanteY = (coeA1 * coeD2 * coeC3) + (coeD1 * coeC2 * coeA3) + (coeA2 * coeD3 * coeC1) - (coeC1 * coeD2 * coeA3) - (coeD1 * coeA2 * coeC3) - (coeC2 * coeD3 * coeA1)

    print("Determinante de Y: "+str(determinanteY))

    # Matriz de Z
    #  coeA1  coeB1  coeD1
    #  coeA2  coeB2  coeD2
    #  coeA3  coeB3  coeD3

    determinanteZ = (coeA1 * coeB2 * coeD3) + (coeB1 * coeD2 * coeA3) + (coeA2 * coeB3 * coeD1) - (coeD1 * coeB2 * coeA3) - (coeB1 * coeA2 * coeD3) - (coeD2 * coeB3 * coeA3)
    print("Determinante de Z: "+str(determinanteZ))

    X = determinanteX / determinanteSis
    Y = determinanteY / determinanteSis
    Z = determinanteZ / determinanteSis

    print("X= "+str(X) + "  Y= "+str(Y) + "  Z= "+ str(Z))
else:
    print("El sistema es incompatible")