#Operadores aritmeticos
print("Operadores aritmeticos")
print(4+4)
# 8
print(5-8)
#-3
print(7*8)
#56
print(float(4/3))
#1.3333333333
#Si usara int en lugar de float el output seria 1

print(25%3)
#1  El operador % es el residuo de la division

base = 2
exponente = 3
print(2 ** 3)
#8

print(15//2)
#7 // Redonde la division al número entero más cercano

#Operadores de comparar

print("Operadores de comparación")

print(1==2)
#false

print(2!=1)
#true

print(2>4)
#false

print(1<2)
#true

print(5>= 14)
#false

print(2<=2)
#true

#Operadores logicos
print("Operadores Lógicos")
cinco = 5

print(cinco < 3 and cinco < 10)
#Ambas condiciones tienen que ser verdaderas para que el
#output sea verdadero

print(cinco > 3 or cinco < 4)
#Al menos una condicion debe ser verdadera para que el
#output sea verdadero

print(not(cinco < 3 and cinco > 10))
#Ninguna condicion debe ser verdadera para que el output sea
#verdadero

print("Operadores de Identidad")

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z) # returns True because z is the same object as x
#true

print(x is y) # returns False because x is not the same object as y, even if they have the same content
#False

print(x == y) # to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y
#True

print(x is not z) # returns False because z is the same object as x
#False

print(x is not y) # returns True because x is not the same object as y, even if they have the same content
#true

print(x != y) # to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y
#false

print("Operadores de pertenencia")

arrat = ["apple", "bannaa"]
print("banana" in arrat)
#Es sensible a Mayusculas

vida = ["I","me","myself"]

print("Es "+str("you" not in vida)+" because you aren´t in my life")