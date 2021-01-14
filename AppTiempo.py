# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 11:04:14 2020
https://openweathermap.org/current
@author: nataa
"""

# api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
# 997fa3afa9f763df860f45e5c78c3847

from tkinter import *
import requests

def mostrar_respuesta(clima):
    try:
        nombre = clima["name"]
        pais= clima["sys"]["country"]
        des = clima["weather"][0]["description"]
        tem = clima["main"]["temp"]
        
        ciudad["text"]=nombre+","+pais
        temperatura["text"]=str(int(tem))+"°C"
        description["text"]=des
    except:
        ciudad["text"]= "No se ha encontrado"
    

def clima(ciudad):
    try:
        API_key = "997fa3afa9f763df860f45e5c78c3847"
        URL = "https://api.openweathermap.org/data/2.5/weather"
        parametros = {"APPID": API_key, "q":ciudad, "units":"metric", "lang":"sp"}
        response = requests.post(URL, params= parametros)
        clima = response.json()
        mostrar_respuesta(clima)
        # print(clima)
    except:
        print("Error")
        
    
ventana = Tk()
ventana.geometry("350x550")

texto_ciudad = Entry(ventana, font = ("Courier", 20, "normal"), justify = "center")
texto_ciudad.pack(padx = 30, pady = 30)

obtener_clima = Button(ventana, text="Obtener Clima", command = lambda:clima(texto_ciudad.get()))
obtener_clima.pack()

ciudad = Label(font = ("Courier", 20, "normal"))
ciudad.pack(padx=10,pady=20)

temperatura = Label(font = ("Courier", 50, "normal"))
temperatura.pack(padx=10,pady=30)

description = Label(font = ("Courier", 20, "normal"))
description.pack(padx=10,pady=30)


ventana.mainloop()