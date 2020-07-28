#Python tiene los siguientes tipos de datos:
# +Tipo texto         str (Secuencias de caracteres)
# +Tipo númerico   
#     int   float  complex
#Tipo secuencia  
#     list (Conjunto de datos que se 
#      pueden repetir y pueden ser distintos.
#      Es mutable) 
#  tuple (Igual que list pero no es mutable)  
#range (Secuencias de números. Inmutable)
#     byte(Almacena valores binarios representados
#     por caracteres ASCII. Inmutable)
#     bytearray (Igual que byte pero es mutable)
#
#+Tipo mapeo dict
#
#+ Tipo determinado
# set (Almacena conjunto de datos sin repeticion. Mutable)
# Frozenset (Igual que set pero inmutable)
#
#+Tipo booleano bool
#
#+Tipo binario  bytes, bytearray, memortview

import random

entero = 5
print(entero)
print(type(entero))

cadena = "Texttt"
print("\n"+cadena)
print(type(cadena))


print("\n")

complejo = 1j
print(complejo)
print(type(complejo))

print("\n")

lista = ["apple", "banana", "cherry"]
print(lista)
print(type(lista))

print("\n")

_tuple_ = (1,3)
print(_tuple_)
print(type(_tuple_))

print("\n")

_range_ = range(6)
print(_range_)
print(type(_range_))

print("\n")


_dict_ = {"name" : "John", "age" : 36}
print(_dict_)
print(type(_dict_))

print("\n")

_set_ = {"apple", "banana", "cherry"}
print(_set_)
print(type(_set_))

print("\n")


_frozen_ = frozenset({"apple", "banana", "cherry"})	
print(_frozen_)
print(type(_frozen_))

print("\n")

_bytes_ = b"Hello"	
print(_bytes_)
print(type(_bytes_))

print("\n")

_bytearray_ = bytearray(5)	
print(_bytearray_)
print(type(_bytearray_))

print("\n")

_memoryview_ = memoryview(bytes(5))	
print(_memoryview_)
print(type(_memoryview_))

print("\n")
#La funcion type() informa el tipo de dato de la variable


#Float puede usarse para escribir números en notacion cientifica

cientifico = -87.7e100

print("\nFlotante en notacion cientifica")

print(cientifico)

#Python no tiene una funcion para crear un numero aleatorio
#Pero tiene un modulo para esto
#Para usarlo se debe importar con:
#  "import random   "
print(random.randrange(1,10))

myList = [0,1,2,4,5,6,7]

print("\nMi lista ordenada "+str(myList))

#str() especifica el tipo de variable que es
#Así que tambien pueden usarse int(), float()


def myfunction():
    return 0.5

otherlist = [0,1,2,4,5,6,7]
random.shuffle(otherlist, myfunction)

print("\nLista desordenada")
print(otherlist)

print("\nUn número random usando el método triangular")
print(random.triangular(20, 40, 30))


"""
Métodos de random

Method	Description
seed()	Initialize the random number generator
getstate()	Returns the current internal state of the random number generator
setstate()	Restores the internal state of the random number generator
getrandbits()	Returns a number representing the random bits
randrange()	Returns a random number between the given range
#random.randrange(start, stop, step)

randint()	Returns a random number between the given range
choice()	Returns a random element from the given sequence
choices()	Returns a list with a random selection from the given sequence
shuffle()	Takes a sequence and returns the sequence in a random order
sample()	Returns a given sample of a sequence
random()	Returns a random float number between 0 and 1
uniform()	Returns a random float number between two given parameters
triangular()	Returns a random float number between two given parameters, you can also set a mode parameter to specify the midpoint between the two other parameters
betavariate()	Returns a random float number between 0 and 1 based on the Beta distribution (used in statistics)
expovariate()	Returns a random float number between 0 and 1, or between 0 and -1 if the parameter is negative, based on the Exponential distribution (used in statistics)
gammavariate()	Returns a random float number between 0 and 1 based on the Gamma distribution (used in statistics)
gauss()	Returns a random float number between 0 and 1 based on the Gaussian distribution (used in probability theories)
lognormvariate()	Returns a random float number between 0 and 1 based on a log-normal distribution (used in probability theories)
normalvariate()	Returns a random float number between 0 and 1 based on the normal distribution (used in probability theories)
vonmisesvariate()	Returns a random float number between 0 and 1 based on the von Mises distribution (used in directional statistics)
paretovariate()	Returns a random float number between 0 and 1 based on the Pareto distribution (used in probability theories)
weibullvariate()	Returns a random float number between 0 and 1 based on the Weibull distribution (used in statistics)
"""