#Crear un módulo para validación de nombres de usuarios. 
# Dicho módulo, deberá cumplir con los siguientes criterios de 
# aceptación:

#El nombre de usuario debe contener un mínimo de 6 
# caracteres y un máximo de 12.

#El nombre de usuario debe ser alfanumérico.
#Nombre de usuario con menos de 6 caracteres, 
# retorna el mensaje "El nombre de usuario debe contener 
# al menos 6 caracteres".
#Nombre de usuario con más de 12 caracteres, 
# retorna el mensaje "El nombre de usuario no puede 
# contener más de 12 caracteres".
#Nombre de usuario con caracteres distintos a los alfanuméricos, 
# retorna el mensaje "El nombre de usuario puede contener solo 
# letras y números".
#Nombre de usuario válido, retorna True.


import re

#Para usar RegExen Python es necesario importar el modulo

print("Módulo de validacion de nombre de usuarios")

user_name = input("Ingrese nombre de usuario ")

user_len = len(user_name)

if user_len >= 6 and user_len <= 12:
    #print("Tiene la longitud apropiada")
    char = re.search("[A-Z]*[a-z]*[0-9]+",user_name) 
    #print(char) imprime un objeto match
    if char:
        print ("True")
    else:
        print("El nombre de usuario puede contener solo letras y números")
else:
    if user_len < 6:
         print("El nombre de usuario debe contener al menos 6 caracteres")

    if user_len > 12:
        print("El nombre de usuario no puede contener más de 12 caracteres")


#Dato: pass te permite tener un if vacío y evitar un error






# El módulo re de RegEx proporciona los siguientes métodos
#findall()   que devuelve en un list[] todas las coincidencias
#     x =re.findall("cadenaBusqueda", String)

#search()  devuelve un objeto match que indica la ubicacion del
#          String buscado en el string original
#      x = re.search("StringBusqueda", StringOriginal)

##    Se pueden usar estos métodos en el objeto match
##             .span() devuelve un tuple que contiene la posicion 
#                       del match
#                           x = re.search("busqueda", txt) 
#                           x.span() 
#              .string devuelve el String que se buscaba
#                           x = re.search("busqueda", txt) 
#                           x.string() 
#               .group() devuelve la parte del string donde match
#                           x = re.search("busqueda", txt)
#                           x.group() 


#split()  devuelve un list con substrings resultantes de la separa
#         ción del string original dada un string indicador
#     x = re.split("StringCortador", StringOriginal, numeroOcurrencias)

# sub() reemplaza cada match con el texto que se indique
#    x = re.sub("StringCortador", StringOriginal, numeroOcasiones) 




### Secuencias Especiales
# r asegura que el String sea tratado como nuevo
# \A  Busca el String al inicio
# \b   Verifica que el String se encuetre al principio  
#      y = re.findall(r"\bstring",txt)
#      o al final de este   y = re.findall(r"string\b",txt)
# \B Verifica que que el String no se encuentre como \b
# 
# \d  Verifica que existan digitos [0-9]
#\D Verifica que no existan digitos [0-9]
#\s  Verifica que existan espacios en blanco
#\S Verifica que no existan espacios en blanco
#\w Verifica que existan caracteres alfanumericos y _
#\W Verifica que existan caracteres especiales y de espacio
#\Z Verifica que el string este al final del texto
