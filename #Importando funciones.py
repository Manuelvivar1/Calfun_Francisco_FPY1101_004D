
#Importando funciones
import funciones as funk
import time,csv
#Definiendo Variable menu
listaestudiantes=[]
while True:
    try:
        menu= int(input("Bienvenido seleccione la funcion que desea realizar \n 1.- Agregar a un estudiante \n 2.- Ver todos los estudiantes \n 3.- Modificar un estudiante \n 4.- Eliminar a un estudiante \n 5.- Guardar colección en un archivo \n 6.- Salir del programa \n Seleccione su opcion: "));
    except:
        print("Porfavor ingrese un numero valido \n \n")
    else:
        if menu == 1:
            print("Agregar estudiante")
            funk.agregarestudiante(listaestudiantes)
        elif menu== 2:
            print("Ver todos los estudiantes")
            funk.verestudiante(listaestudiantes)
        elif menu== 3:
            print("Modificar estudiante")
            funk.modificarestudiante(listaestudiantes, 0)
        elif menu==4:
            print("Eliminar estudiante")
            funk.eliminarestudiante(listaestudiantes)
        elif menu==5:
            print("Guardar coleccion en un archivo")
            funk.agregarestudianteacsv(listaestudiantes)
        elif menu==6:
            print("Saliendo del programa")
            break
    time.sleep(1)
