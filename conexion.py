# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 21:15:19 2020

@author: Administrador

Verifica que un dominio este disponible
"""

from requests import get, exceptions

def check_internet_connection():
    try:
        get('http://google.com', timeout = 3)
        print('connected')
    except exceptions.ConnectionError:
        print('not connected')

check_internet_connection()