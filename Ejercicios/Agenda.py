import mysql.connector
import json
def registro(baseDatos, datos):
    cursor = baseDatos.cursor()
    try:
        insertar = "INSERT INTO contactos (Nombre, Direccion, Celular, Telefono, Correo) VALUES (%s,%s,%s,%s,%s)"
        val = (datos[0],datos[1],datos[2], datos[3],datos[4])
        cursor.execute(insertar, val)
        baseDatos.commit()
        print(cursor.rowcount, " registro exitoso.")
    except:
        print("Algo salio mal")
  
def recopila(datos):
    nombre = str(input("Nombre: "))
    direccion = str(input("Direccion: "))
    celular = str(input("Celular: "))
    telefono = str(input("Telefono: "))
    correo = str(input("Correo: "))
    datos = [nombre, direccion, celular,telefono, correo]
    return datos

def muestra(baseDatos):
    cursor = baseDatos.cursor()
    try:
        cursor.execute("SELECT * FROM contactos")
        resultado = cursor.fetchall()
        i = 0
        print(" ID |   Nombre   | Direccion   | Celular   | Telefono  |  Correo")
        while i < len(resultado): 
            print(str(resultado[i][0])+"  "+str(resultado[i][1])+" "+str(resultado[i][2])+" "+str(resultado[i][3])+" "+str(resultado[i][4])+" "+str(resultado[i][5]))
            i += 1
    except:
        print("No se ha podido recuperar información")
    

def borrar(baseDatos):
    muestra(baseDatos)
    try:
        id = int(input("Ingrese el identificador del contacto: "))
        borrar = "DELETE FROM contactos WHERE ID = %d"
        attr = (id,)
        cursor = baseDatos.cursor()
        cursor.execute(borrar,attr)
        baseDatos.commit()
        print(cursor.rowcount, "elementos eliminados")
    except Exception as e:
        print("No se ha podido borrar"+e)

def conexion():
    try:
        baseDatos = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="Agenda"
        )
        creaTabla(baseDatos)
    except:
        try:
            baseDatos = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            )
            cursor = baseDatos.cursor()
            cursor.execute("CREATE DATABASE Agenda")
            conexion()
            conexion()
        except:
            print("Error al conectar con servidor")


def menu(baseDatos):
    if baseDatos != None:
        datos=[]
        opcion = 0
        while opcion !=4:
                print("\nMenu: 1. Registrar nuevo contacto   2. Mostrar contactos 3. Borrar registro 4. Salir")
                opcion = int(input("Opción: "))
                if opcion == 1:
                    registro(baseDatos, recopila(datos))
                elif opcion ==2:
                    muestra(baseDatos)
                elif opcion ==3:
                    borrar(baseDatos)

def creaTabla(baseDatos):
    try:
        cursor = baseDatos.cursor()
        cursor.execute("CREATE TABLE contactos (ID INT AUTO_INCREMENT PRIMARY KEY, Nombre VARCHAR(30),Direccion VARCHAR(200), Celular VARCHAR(15),Telefono VARCHAR(15),Correo VARCHAR(100));")
    except:
        print("ya existe")
        menu(baseDatos)  

conexion()
