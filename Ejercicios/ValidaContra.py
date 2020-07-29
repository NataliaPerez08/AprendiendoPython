#Crear un módulo para validación de contraseñas. 
# Dicho módulo, deberá cumplir con los siguientes
#  criterios de aceptación:

#La contraseña debe contener un mínimo de 
# 8 caracteres. 
# Una contraseña debe contener letras minúsculas,
#  mayúsculas, números y al menos 1 carácter no 
# alfanumérico.

#La contraseña no puede contener espacios 
# en blanco.
#Contraseña válida, retorna True.
#Contraseña no válida, retorna el mensaje "La contraseña elegida no es segura".

import re

print("Validación de contraseñas")

contra = input("Ingrese contraseña: ")

contra_len = len(contra)

if contra_len >= 8:
    espacio = re.search("\s",contra)
    valida = re.search("[A-Z]+[a-z]+\d+\W+",contra) # + Al menos una coincidencia, * de 0 a más

    if espacio:
        print("La contraseña elegida no es segura")
    else:
        if valida:
            print("True")
        else:
            print("La contraseña elegida no es segura")
else:
    print("La contraseña elegida no es segura")