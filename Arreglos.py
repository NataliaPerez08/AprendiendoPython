#Existen 4 tipos de datos para formar arreglos


#List  permite elementos duplicados, es ordenable y modificable

_list = ["Fus","Winnie", "Ruffles", "Perrito especial","piltrafa"]

print("Los nombres de "+str(_list[0]+" han sido ")+str(_list)+" por que el es un "+str(_list[-2]))

#Modificar un index
_list[4] = "Esguisi"
print("Correcion "+ str(_list))


#Verificar si existe en el arreglo

if "Pedacito" in _list:
    print("El nombre Pedacito ya existe")
else:
    print("Añadir Pedacito")
    _list.append("Pedacito")
    #Al final


print("Lista de nombre renovada")

#LOOOOOP en el list
for i in _list:
    print(i)

print("Ahora la lista tiene "+ str(len(_list))+" elementos")

#Insertar un elemento en un index determinado

_list.insert(0,"Corazon")
_list.insert(4,"Caquita")
_list.insert(7, "Bolita")
_list.append("Suri")

print(_list)

print("Oh oh errores, deja corregir")

#Elimina un elemento especifico
_list.remove("Caquita")


#Elimina el último elemento
_list.pop() #Suri


del _list[6]  #Bolsita
print(_list)

##Métodos Faltantes
#copy  

# del _list      eliminaria la lista completamente
# _list.clear()     vacía la lista


#Tuple es ordenable pero no puede cambiar, ni permite elementos 
#duplicados


#Set es una coleccion desordenada e no indexada, no permite repe
#ticiones



#Dictionary es una coleccion desordenada, modificable e indexada 
# no permite miembros duplicados