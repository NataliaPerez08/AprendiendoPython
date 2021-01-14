# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 11:04:38 2020

@author: nataa
"""

import  pandas as pd
import matplotlib.pyplot as plt

workbook1 = "hoja.xls"

df = pd.read_excel(workbook1)
# print(df.head())

campos = df[["Producto", "Precio"]]
print(campos)

ax = campos.plot.bar(x="Producto", y= "Precio", rot = 0)
plt.show()