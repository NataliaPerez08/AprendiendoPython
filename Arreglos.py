#Existen 4 tipos de datos para formar arreglos


#List  permite elementos duplicados, es ordenable y modificable

_list = ["Fus","Winnie", "Ruffles", "Perrito especial","piltrafa"]

#Tambien se puede declarar:  _list = list(("elem","elem"))

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
#copy()   crea una copia del list  
#         copia = originalList.copy() 
#         tambien see puede así copia = list(originalList) 

# del _list      eliminaria la lista completamente
# _list.clear()     vacía la lista

#extend()  añade los elementos de un arreglo a otro
# list1.extend(list2)



#count()  retorna el numero de apariciones de un elemento

apari = _list.count("Fus")
print("El nombre Fus aparece "+str(apari)+" veces")

#index retorna el index de la primera aparicion del elemento

print("En la posicion "+str(_list.index("Fus")))

#reverse()
_list.reverse()

print("Método reverse invierte el orden "+str(_list))

#sort()  Ordena el list  
#               list(reverse = True|False, key = myFunc)
#               reverse = true (Descendiente /mayor a menor/)
#               key =  funcion que especifica un criterio para ordenar

##Por la longitud del elemento
def Alfabetico(elemento): #recibe elemento
    return len(elemento)  #Regresa la longitud del elemento

_list.sort(reverse = True, key = Alfabetico)

print("Método sort ordena list "+str(_list))


print("\nList de dictionaries")

def orden(elem):
    return elem['year']

cars = [
    {'car': 'Ford', 'year':2005},
    {'car': 'Mitsubishi', 'year': 2000},
    {'car': 'BMW', 'year': 2019},
    {'car':'VW', 'year': 2011}
]

cars.sort(key=orden)

print(cars)



#Tuple es ordenable pero no puede cambiar, ni permite elementos 
#duplicados

print("\nLos \'Tuple\' funcionan muy similar a las listas sin embargo no es posible editar el contenido de este")
#Se pueden usar los métodos count() e index()

print("Se crea un tuple así: thistuple = (\'elem\',)")


tu_ = ("elem",)
#La coma al final es necesaria para crear un tuple
#y no una clase 

print(type(tu_))


#Set es una coleccion desordenada e no indexada, no permite repe
#ticiones

print("\n-------Sets-------")

semana = {"Domingo", "Lunes", "Martes", "Miercoles"}

#Se puede usar for para recorrer el set como los list

print("Es banana un dia de la semana? "+str("banana" in semana))

#No se pueden crear elementos en un set 

#Para añadir un elemento
semana.add("Jueves")

#Para añadir varios elementos

semana.update(["Viernes","Sabado","diciembre","enero"])

print(semana)  
#Los set estan desordenados por lo que no sabes  
#en que orden apareceran

print("La longitud de la semana es "+ str(len(semana)))

#Para eliminar un elemento se puede usar

semana.remove("diciembre")
#Si este no existe lanzara un error

semana.discard("enero")

print("Corregido "+str(semana))

#Es posible usar el método pop() pero no puedes 
#controlar el elemento eliminado
#Se puede usar el this.clear() para vaciar el set
# del thisSet   para eliminar el set 

numeros = {1,2,3,4,5,6,7}


print("\rMezcla de números y días de la semana")
union = semana.union(numeros)
print(union)


##Métodoosssss

#difference() devuelve un set que contiene la 
# diferencia entre dos set 

print("Metodo difference en uso")
dias = union.difference(numeros)

num = union.difference(semana)

#Otro método similar es difference_update
# unSet.difference_update(otro set)
#Este modifica el set original

#difference() devuelve otro set

print("Los dias de la semana ")
print(dias)

print("Los números ")
print(num)

#intersection() genera un nuevo set con los 
# elementos en común de los set

uno = {1j,2,3, 7, 5, 2j, 3,6}
dos ={1j, 4j, 4, 6j, 2j, 10}

tres = uno.intersection(dos)

print("\nNumeros complejos "+str(tres))

#El metodo intersection_update() elimina todos
#los elementos que no estén en ambos conjuntos 

print("Los set uno y dos tienen NO elementos en común "+str(uno.isdisjoint(dos)))
#Si hay interseccion de los sets devuelve false, 
# si no hay interseccion devuelve true


tres = {1, 2, 3 ,4 ,5,14,15,17}
cuatro = {0, 1,2,3,4,5,6,7,8,9,10,11}

print("El set tres es subconjunto del cuatro "+ str(tres.issubset(cuatro)))
#Es 'subconjunto'


print("El set cuatro contiene al set tres "+str(cuatro.issuperset(tres)))
#Lo contiene   tres pertenece a cuatro


print("Los elementos pertenecientes a los set diferentes entre el set tres y el cuatro son: "+str(tres.symmetric_difference(cuatro)))

#symmetric_difference()  devuelve un nuevo set 
# & symmetric_difference_update  modifica el set
#original 

print("----------Dictionaries----------")

#Dictionary es una coleccion desordenada, modificable e indexada 
#no permite miembros duplicados

auto = {
    "marca": "Ford",
    "modelo": "Mustang",
    "año": 1964
}

print(auto)

#Se parece a un arreglo asociativo
print("Se puede acceder al modelo "+ str(auto["modelo"])+" y al año "+str(auto.get("año")))

#Se puede modificar la informacion de este
auto["año"]= 2020

print("Estas son las key del diccionario ")
for i in auto:
    print(i)

#Tambien se puede hacer de esta manera:
#   for x in Diccionetio.values():
#     print(x)
 
print("Y esta es la informacion")
for i in auto:
    print(auto[i])

print("Para mostrar ambas se usa items() ")

for x, y in auto.items():
    print(x,y)

#Para consultar la existencia se usa in

print("En el diccionario auto se utiliza la llave tamaño? ")

if "tamaño" in auto:
    print("Sí, una llave es tamaño")
else:
    print("No, que llave más rara sería")

print("El diccionario tiene "+str(len(auto))+ " llaves")


print("Un auto deberia tener un color añadamoslo al diccionario")

auto["color"] = "amarillo pollito"

auto.update({"placas":"ADT-451"})

auto["multas"] = "muchas"

print(auto)

print("Eliminemos las multas")

auto.pop("multas") #del funciona igual
# sería: 
#         del auto["multas"]

#Otra manera es usando el método popitem()
# Sería:
#        auto.popitem()
# ya que elimina el último elemento añadido


print(auto)

#clear() vacia el diccionario
#   Seria:
#           auto.clear()


#Puedes hacer copias de un diccionario así:
# copy()    copia = auto.copy() 
# dict()    copia = dict(auto)



#Diccionario de diccionarios

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print("Diccionario de diccionarios "+str(myfamily))
print("Las llaves del diccionario de diccionarios "+str(myfamily.keys()))
print("Los elementos del diccionario de diccionarios "+str(myfamily.items()))

lol = ('centenas', 'decenas','unidades')
llaveDic = dict.fromkeys(lol)
print("Diccionario desde llaves")
print(llaveDic)

_yo = {
    "nombre": "Natalia",
    "edad": "18"
}

dor = _yo.setdefault("Dormida","False")
#Establece un valor predeterminado
print("Estoy dormida? "+str(dor)+str(_yo))
