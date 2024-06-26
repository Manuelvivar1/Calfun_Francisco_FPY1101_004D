import csv
def agregarestudiante(listaestudiantes):
    addstudent=input("Ingrese el nombre del estudiante que desea agregar: ")
    listaestudiantes.append(addstudent)
    return

def verestudiante(listaestudiantes):
    print(listaestudiantes)
    return

def modificarestudiante(listaestudiantes, x):
    try:
        x= int(input("Ingrese el numero de lista que desea modificar: "))
    except:
        print("Ingrese un numero valido")
    else:
        if x < len(listaestudiantes) and x >= 0:
            nombre_de_estudiante_nuevo=input("Ingrese el nuevo nombre del estudiante: ")
            listaestudiantes[x] = nombre_de_estudiante_nuevo
        else:
            print("El numero de lista ingresado no es valido")
    return
def eliminarestudiante(listaestudiantes):
    try:
        numeliminar= int(input("ingrese el numero de lista del estudiante que desea eliminar: "));
    except:
        print("Ingrese un numero valido")
    else:
        if numeliminar < len(listaestudiantes) and numeliminar >= 0:
            del listaestudiantes[numeliminar]
        else:
            print("El numero de lista ingresado no es valido")
    return

def agregarestudianteacsv(listaestudiantes):
    with open("lista.csv","w",newline='', encoding='utf-8') as lista_csv:
        writer = csv.writer(lista_csv)
        writer.writerow(listaestudiantes)
    return