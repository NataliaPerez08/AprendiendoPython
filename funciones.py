# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 22:13:34 2020

@author: Administrador
"""

import numpy as np
import matplotlib.pyplot as plt

def h(x):
    return np.sin(x) 
#Lo que retorne la funcion determinara 
#la grafica ejemplos: (x*x)   np.sin(x) np.cos
#np.exp(x) exponencial

g= lambda x:np.cos(x)
#una funcion lambda retorna el coseno de x
x=np.linspace(0,10,100) #x va se 0 a 10 y se tienen 100 puntos

v=[0,10,-1,1] #Esta list indica
#[valorminimoenX, valormaximoenX,
#valorminimoenY, valormaximoenY]

plt.plot(x,h(x),'r--' ,label ='Funcion seno') #Se grafica x y la funcion h(x)
#r-- para que la grafica sea roja y este formada de rayas
plt.plot(x,g(x),'bo-',label="Funcion coseno")

plt.xlabel("Eje x")
plt.ylabel("Eje y")

plt.title("Titulo de la grafica")
plt.legend(loc=3)
#Coloca la leyenda en la esquina inferior izquierda
# 1 representa la esquina superior derecha

plt.text(4,0,"prueba")

plt.axis(v)#Limita la grafica
plt.grid() #inserta cuadricula

