print("Rectas")
try:
    opcion = input("Opciones \n 1. Pendiente de una recta dados dos puntos \n 2. Ecuacion de una recta dado dos puntos")

    selected = int(opcion)

    if selected == 1:
        print("Pendiente")
        try: 
            x1 = int(input("Valor de x1: "))
            y1 = int(input("Valor de y1: "))
            x2= int(input("Valor de x2: "))
            y2 = int(input("Valor de y2: "))

            m = (y2-y1)/(x2-x1)   

            print(m)
        except: print("Invalido")
    if selected == 2:
            try: 
                x1 = int(input("Valor de x1: "))
                y1 = int(input("Valor de y1: "))
                x2= int(input("Valor de x2: "))
                y2 = int(input("Valor de y2: "))
                m = (y2-y1)/(x2-x1) 
                
                if y1 < 0 and x1 < 0:
                    x1 = -x1
                    y1= -y1
                    print("(y + "+str(y1)+") = "+str(m)+"(x + "+str(x1)+")")
                else:
                    print("(y - "+str(y1)+") = "+str(m)+"(x - "+str(x1)+")")

            except: print("Invalido")

except: print("Esa opcion no existe")