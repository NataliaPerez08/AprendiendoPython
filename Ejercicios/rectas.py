print("Rectas")
try:
    opcion = input("Opciones \n 1. Pendiente de una recta dados dos puntos \n 2. Ecuacion de una recta dado dos puntos \n 3. Ecuacion lineal")

    selected = int(opcion)

    if selected == 1:
        print("Pendiente")
        try: 
            x1 = int(input("Valor de x1: "))
            y1 = int(input("Valor de y1: "))
            x2= int(input("Valor de x2: "))
            y2 = int(input("Valor de y2: "))

            m = (y2-y1)/(x2-x1)
            if m == 0:
                print("La pendiente es nula")
            if m < 0:
                print("Pendiente negativa: ")
                print(m)
            else:
                print("Pendiente positiva: ")
                print(m)
        except: 
            print("Pendiente nula")
    if selected == 2:
            try: 
                x1 = int(input("Valor de x1: "))
                y1 = int(input("Valor de y1: "))
                x2= int(input("Valor de x2: "))
                y2 = int(input("Valor de y2: "))
                m = (y2-y1)/(x2-x1) 

                print("(y - "+str(y1)+") = "+str(m)+"(x - "+str(x1)+")")
                c = m * x1
                print("y -"+str(y1)+" = "+str(m)+"x - "+ str(c))
                c2 = y1 +(-c)
                print(str(-m)+"x + y -"+str(y1)+"+"+str(c)+"= 0")
                print(str(-m)+"x + y -"+str(c2)+"= 0")
                print(str(m)+"x - y ="+str(c2))
            except: print("Invalido")
    if selected == 3:
        print("Ecuacion lineal tipo Ax + B = C")
        
        A = int(input("Valor de a: "))
        B = int(input("Valor de b: "))
        C = int(input("Valor de c: "))

        terC = C - B
        ind = terC / A

        print(str(A)+"x + "+str(B)+" = "+str(C))
        print(str(A) +"x = "+str(terC))
        print("x = "+str(ind))
        
        #ec = str(input("Ecuacion: "))
        #ecuacion = list((ec)) ##Ecuacion pasa a ser list
        #for i in ecuacion:
        #    print(i)
        #Separa el input hasta  el signo de igual
        #_streq = ec.split("=")
        #Me desespere

except: print("Esa opcion no existe")