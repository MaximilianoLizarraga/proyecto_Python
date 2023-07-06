# -*- coding: utf-8 -*-
"""Primera-pre-entrega-Lizarraga.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xYNpY2yRiX9ZRM82Wq3QtS5IyixRQPAU
"""

#Creacion base de datos

usuarios = {}

#Funcion para crear usuario

def crear_usuario():
    nombre_usuario = input("Elige un nombre de usuario: ")
    while nombre_usuario in usuarios:
        print("Nombre de usuario ya existente, ingrese otro: ")
        nombre_usuario = input("Elige un nombre de usuario: ")
    contraseña_usuario = input("Elige una contraseña: ")
    usuarios[nombre_usuario] = contraseña_usuario
    return("Se ha creado el usuario")

#Funcion para leer informacion de base de datos

def leer_base_datos(base_datos):
    if len(base_datos) == 0:
        return "No hay usuarios registrados hasta el momento"

    for usuario, contraseña in base_datos.items():
        print(f"El usuario es: {usuario} y la contraseña es: {contraseña}")

    return "Estos son todos los usuarios"

#Funcion chequeo de login

def login(base_datos):
    username = input("Ingrese su usuario: ")
    while username not in usuarios:
        print("Usuario no registrado, vuelva a intentarlo")
        username = input("Ingrese su usuario: ")
    password = input("Ingrese su password: ")
    while base_datos[username] != password:
        print("Error en la password")
        password = input("Ingrese su password: ")
    return("Te has logueado correctamente")

#Funcion de guardado de datos
ruta = "C:\Users\Maxi\Desktop\aca guardamos los datos"

def guardar_data(usuarios, ruta):
    with open(ruta + "/users_in_db.txt", "w") as f:
        for usuario, contraseña in usuarios.items():
            linea = "El nombre de usuario es " + usuario + " y la contraseña es " + contraseña + "\n"
            f.write(linea)
    print("Se guardaron los datos correctamente.")

#Funcion de ejecucion del programa

while True:
    selector_de_opciones = input("\nElija una de estas opciones:\n 1) Crear un usuario.\n 2) Login de usuario.\n 3) Leer la informacion.\n 4) Guardar informacion.\n 5) Finalizar el programa.\n ")
    if selector_de_opciones.isnumeric() :
        selector_de_opciones = int(selector_de_opciones)
        if selector_de_opciones == 1:
            print(crear_usuario())
        elif selector_de_opciones == 2:
            print(login(usuarios))
        elif selector_de_opciones == 3:
            print(leer_base_datos(usuarios))
        elif selector_de_opciones == 4:
            print(guardar_data(usuarios))
        elif selector_de_opciones == 5:
            print("Se esta finalizando el programa...")
            break
        else:
            print("Elija una opcion valida.")
    else:
        print("Elija una opcion valida.")
print("Finalizo el programa")