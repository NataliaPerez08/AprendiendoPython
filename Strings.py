Cadena = """Los string pueden mostrarse directamente en consola
usando el método print, pero también pueden almacenarse en 
una variable y luego usar esa variable en el método print"""

#Los string son arrays por lo que de esta manera:
print(Cadena[2])
#Puedo acceder a un caracter de acuerdo a su posicion

#Tambien es posible acceder a un rango de caracteres:
print("\n"+str(Cadena[0:10]))
#Este rango puede empezar de izquierda a derecha con números 
#positivos

print("\n"+str(Cadena[-12:-1]))

#O de derecha a izquierda con números negativos


#Para obtener la longitud del string se usa el metodo len
print(len(Cadena))


#Python tiene varios metodos para los string

#Strip() remueve cualquier espacio blanco de el inicio y/o del final 

#lower devuelve el string en minusculas
#upper en mayusculas


#replace reemplaza un string con otro
a = 'La prigramaciin es dificil'
print("\n"+a.replace("a","i")+"\r")


b = "Jirafas, rinocerontes, leones, cocodrilos"
print(b.split(","))
#Separa el string en substring si encuentra el separador indicador

#Verifica si algo esta en el string
texto = "The rain in Spain stays mainly in the plain"
prueba = "ai" in texto
print(prueba)


#Verifica si algo no esta en el string
txt = "The rain in Spain stays mainly in the plain"
x = "ain" not in txt
print(x) 

#Se usa format para convertir number a String
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price)) 


#Escape characters
#\'	Single Quote	
#\\	Backslash	
#\n	New Line	
#\r	Carriage Return	
#\t	Tab	
#\b	Backspace	
#\f	Form Feed	
#\ooo	Octal value	
#\xhh	Hex value'''

