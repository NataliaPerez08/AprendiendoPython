
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

def reprobadas(asig_repro):
    if len(asig_repro) > 0:
        print("Reprobaste: ")
        for y in asig_repro:
            print(" "+y)

cant_mate = int(input("Cuantas asignaturas desea registrar? "))
numero = cant_mate
calif_por_asig={}
asig_repro=[]
suma = 0
while cant_mate >0:
    cant_mate -=1
    asign = input("Nombre de la materia: ")
    calif_por_asig = ordenar(registroAsig(asign),calif(registroAsig(asign)), calif_por_asig)

for key in calif_por_asig:
  print (key, ":", calif_por_asig[key])
  num = int(calif_por_asig[key])
  suma += num
  if int(calif_por_asig[key]) < 6:
      asig_repro.append(str(key))

print("Promedio: "+str(suma/numero))
reprobadas(asig_repro)


