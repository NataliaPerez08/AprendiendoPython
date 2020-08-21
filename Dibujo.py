# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 20:53:24 2020

@author: Administrador
"""

import turtle

window = turtle.Screen()
flecha = turtle.Turtle()

def triangulo():
    for i in range(3):
        flecha.forward(100)
        flecha.left(120)

def cuadrado():
    for i in range(4):
        flecha.forward(100)
        flecha.left(90)
        
def pentagono():
    for i in range(5):
        flecha.forward(100)
        flecha.left(72)
        
triangulo()
cuadrado()
pentagono()

#Es posible simplificar el codigo
#Se puede definir una unica funcion

def figura(lados):
    for i in range(lados):
        flecha.forward(100)
        flecha.left(360/lados)
        
#hexagono
figura(6)


# Funciones principales para animar
#forward(distance): Avanzar una determinada cantidad de píxeles.
#backward(distance): Retroceder una determinada cantidad de píxeles.
#left(angle): Girar hacia la izquierda un determinado ángulo.
#right(angle): Girar hacia la derecha un determinado ángulo.

#Desplazarnos de un punto a otro sin dejar rastro. 
#Para ello utilizaremos las siguientes funciones:
#home(distance): Desplazarse al origen de coordenadas.
#goto((x, y)): Desplazarse a una coordenada en concreto.
#pendown(): Subir el lápiz para no mostrar el rastro.
#penup(): Bajar el lápiz para mostrar el rastro.
 
#cambiar el color o tamaño del lápiz. 
#En ese caso utilizaremos las siguientes funciones gráficas:
#shape('turtle'): Cambia al objeto tortuga.
#pencolor(color): Cambiar al color especificado.
#pensize(dimension): Tamaño de la punta del lápiz.
