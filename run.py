#Importando funciones
import funciones as func
import time,csv
#Definiendo Variable menu
try:
    menu= int(input("Bienvenido seleccione la funcion que desea realizar \n 1.- Agregar a un estudiante \n 2.- Ver todos los estudiantes \n 3.- Modificar un estudiante \n 4.- Eliminar a un estudiante \n 5.- Guardar colección en un archivo \n 6.- Salir del programa"));
except:
    print("Porfavor ingrese un numero valido")
else:
    if menu == 1:
        print("Agregar estudiante")

    elif menu== 2:
        print("Ver todos los estudiantes")

    elif menu== 3:
        print("Modificar estudiante")
        
    elif menu==4:
        print("Eliminar estudiante")
        
    elif menu==5:
        print("Guardar coleccion en un archivo")

    elif menu==6:
        print("Salir del programa")
        exit
    else:
        print("Porfavor seleccione una opcion valida");
#Iniciando Aplicacion