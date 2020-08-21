# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 21:39:00 2020

@author: Administrador
"""

import turtle

window = turtle.Screen()
pluma = turtle.Turtle()

def arriba():
    pluma.setheading(90)
    pluma.forward(100)

def derecha():
    pluma.setheading(0)
    pluma.forward(100)
    
def abajo():
    pluma.setheading(270)
    pluma.forward(100)

def izquierda():
    pluma.setheading(100)
    pluma.forward(100)
    
window.onkeypress(arriba,"Up")
window.onkeypress(derecha,"Right")
window.onkeypress(izquierda,"Left")
window.onkeypress(abajo,"Down")

window.listen()