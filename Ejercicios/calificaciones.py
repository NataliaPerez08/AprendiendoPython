
def registroAsig(asign):
    registro =[]
    registro.append(asign)
    return registro

def calif(registro):
    registroCalif = []
    for i in registro:
        calificacion = int(input("Cual fue su calificacion en " +str(i)+" "))
        registroCalif.append(calificacion)
    return registroCalif

def ordenar(registro,registroCalif, calif_por_asig):
    for j in registro:
        for k in registroCalif:
            calif_por_asig[str(j)]= str(k)
            return calif_por_asig

def promedio (registroCalif, suma):
    for l in registroCalif:
        suma+=l

cant_mate = int(input("Cuantas asignaturas desea registrar? "))
numero = cant_mate
calif_por_asig={'0':'0'}
suma = 0
while cant_mate >0:
    cant_mate -=1
    asign = input("Nombre de la materia: ")
    calif_por_asig = ordenar(registroAsig(asign),calif(registroAsig(asign)), calif_por_asig)

for key in calif_por_asig:
  print (key, ":", calif_por_asig[key])
  num = int(calif_por_asig[key])
  suma += num

print(str(suma/numero))
