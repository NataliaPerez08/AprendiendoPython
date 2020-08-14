# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 21:20:42 2020

@author: Administrador
"""

import random #Esta libreria permite generar secuencias de datos random
import string #Esta libreria nos permite a acceder a todos lo caracteres alfanumericos ascii y otros

def crear_contra(n): #Define una funcion para crear contraseña que recibe "n" es decir el largo de la misma
    allChars = list(string.ascii_letters) + list(string.digits) + list(string.punctuation)
    #Crea un list que contiene todas las letras del codigo ascii, ademas accede a los numeros y los signos de puntuacion
    
    password = [] #Declara un list para almacena la contraseña
    
    for i in range(n):
        tmp = random.choice(allChars) #Almacena en una variable temporal una eleccion aleatoria de un elemento del list allChars (todos los caracteres)
        password.append(tmp) #Añade al final del list la eleccion anterior
        
    res = "".join(password) #Une un list cuyo contenido era "" al list password
    return res #La funcion retorna la contraseña creada

n = int(input("Ingresa ancho de una contraseña: "))
test = crear_contra(n) #Llama a la funcion crear contra enviandole como parametro el input del usuario y almacena la respuesta en una variable

try: #Intenta imprimir la respuesta de la funcion
    print(test)
except:
    print("Debe ingresar el ancho del Password")
#Si falla al llamr la funcion, porque el usuario ingreso algo invalido
# o no ingreso nada, o algun otro motivo manda este mensaje 