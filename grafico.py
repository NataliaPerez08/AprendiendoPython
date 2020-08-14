# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 21:42:56 2020

@author: Administrador
"""
#Importar modulos necesarios
import math
import numpy as np
from matplotlib import pyplot as plt

#Generacion datos para el grafico

x = np.array(range(500))*0.1 
#genera una secuencia de numeros desde 0 a 500 y lo multiplica por 0.1
#lo que significa que la gráfica en x avanzara de 10 en 10
y = np.zeros(len(x))
#zeros es una funcion de numpy
#regresa un nuevo array de las mismas caracteristicas
#pero lleno de ceros

#y es igual a la logitud del arreglo x

for i in range(len(x)): #i = [2,499]
    y[i] = math.sin(x[i])
    
 #Se crea el gráfico
plt.ion() #Muestra el grafico
plt.plot(x,y) #Se le envian los datos