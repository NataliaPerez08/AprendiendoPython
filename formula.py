import  math

print("Formula General")
#    -b +- ( (b^2) - 4ac)^1/2
# x = _______________
#         2a
a = input("A = ")
b =input("B = ")
c = input("C = ")

try:
    coeA = int(a)
    coeB = int(b)
    coeC = int(c)

    discri = (coeB**2) - (4 * coeA * coeC)
    
    if discri >= 0:
        print("La solucion de la ecuacion esta en los reales")
        
        raiz = math.sqrt(discri)
        x1 = (-coeB + raiz)/(coeA * 2)
        x2 = (-coeB - raiz)/(coeA*2)
        print("x1 = "+str(x1))
        print("x2= "+str(x2))
    else:
        print("La solucion no esta en los reales")
        absoluto = math.fabs(discri)
        raiz = math.sqrt(absoluto)
        x1 = (-coeB + raiz)/(coeA * 2)
        x2 = (-coeB - raiz)/(coeA*2)
        print("x1 = "+str(x1)+"i")
        print("x2= "+str(x2)+"i")

except:
    print("Algo salio mal")