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

#Es posible usar el método pop pero no puedes 
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

print("Los dias de la semana ")
print(dias)

print("Los números ")
print(num)



#Dictionary es una coleccion desordenada, modificable e indexada 
#no permite miembros duplicados
#
#
