#Mi primer programa en python, now I am
# one of the cool kids


"""
Esto es una manera fea de hacer comentarios
de más de una linea
"""

print("Hello, World xd")

print("Python no requiere declarar variables, estas se crean al momento de darles valor")

nombre = "Fusito"

_my_variable = ' xd'

#Las variables deben iniciar con una letra
#o un guion bajo, los nombres de las variables
#son sensibles a las mayusculas

x, y, z = "Orange", "Banana", "Cherry"

todo = "Mis frutas favoritas son "+ x + ", "+ y + " y " + z

print(todo)

print(nombre+_my_variable)


#Condicional if

if 5 > 2:
    print("\n Five is greater than two")


#Definicion de una funcion que utiliza una variable global

a = "awesome"

print("\nPhyton is "+a)

def  myfunc():
    #Si se sobreescribe una variable dentro de una funcion
    #el programa utilizara el valor que se le dio en el bloque
    #de la función; pero la variable fuera de la funcion
    #conservará su valor original
    #a = "fantastic"

    #A menos que se utilice la palabra reservada global
    global a 
    a = "worse than JAVA jk"

myfunc()

print("\nPhyton is "+a)

