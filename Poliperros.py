'''
Diccionarios usados mas en APLI
'''

import random #Generar numeros random
import os #Del sistema
import sys
from PIL import Image #Trabajar con imagenes

def resource_path(relative_path):
    """ Obtiene la ruta absoluta de los recursos (funciona para el .exe) """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Para usar tu foto:
ruta_foto = resource_path("dog.png")
# Ahora usa 'ruta_foto' en lugar del nombre del archivo


datosPoliPerros = { #Diccionario
    "nombre" : [],  #("clave/nombre" : valor_cualquiera,) en este caso un arreglo.
    "huellaDactilar" : [],
    "foto" : []
    #Dentro del diccionario se puede agregar otro diccionario
}
numPerros = 0

def menu():
    print("\n ====== Bienvenido(a) ====\n")
    print(f"Qué acción desea realizar?: ") 
    print(f"* 1) Registro PoliPerros") 
    print(f"* 2) Mostrar PoliPerros") 
    print(f"* 3) Mostrar por huella ") 
    print(f"* 4) Imprimir BBD")
    print(f"* 5) Salir del sistema")
    return int(input("Seleccine una opcion: "))

def registrarPoliPerros(numPerros):
    os.makedirs("BDDPERROS",exist_ok=True) #Es para crear directorios, crea una carpeta/directorio en la compu con ese nombre, si ya existe no hace nada
    #BDDPERROS es la base de datos del sistema (BDD = Base De Datos)
    #archivo = open("poliperros.txt","a") #Abre un archivo txt, y "a" agrega info, "w" escribe y "r" lee el archivo
    with open("poliperros.txt", "a") as archivo:
        for i in range (numPerros):
            print("Ingrese los datos del poliperro",i+1)
            nombre = input("Nombre: ")
            huellaDactilar = input("Huella dactilar: ")
            print("El poliperro tine foto?")
            tieneFoto = input("Ingrese si o no: ")
            if (tieneFoto == "si"):
                rutaOriginal = input("Ingrese la uta de la foto: ") #/CargarPC/max.PNG
                imagen = Image.open(rutaOriginal) 
            else:
                imagen = Image.open(ruta_foto) 
            rutaGuardada = f"BDDPERROS/poliperro_{random.randint(1,1000)}.png"
            imagen.save(rutaGuardada) #Al subir la imagen, esta se guardara y renombrara en la carpeta/directorio BDDPERROS y le dara un numero randomico con extencion png
            datosPoliPerros["nombre"].append(nombre)
            datosPoliPerros["huellaDactilar"].append(huellaDactilar)
            datosPoliPerros["foto"].append(imagen)
            archivo.write("BDD POLIPERROS")
            archivo.write(f"{nombre} -- {huellaDactilar} -- {rutaGuardada} \n")
        archivo.close() #Al finalizar cierra el archivo para que no se desperdicien recursos

def mostrarPoliPerros():
    for i in range(len(datosPoliPerros["nombre"])):
        print("-----------------------------------------")
        print(f"Mostrar datos poliperro {i+1}")
        print(f"* Nombre: {datosPoliPerros['nombre'][i]}")
        print(f"* Huella dactilar: {datosPoliPerros['huellaDactilar'][i]}")
        #imagen = Image.open(datosPoliPerros['foto'][i]) este no me funciona porque estoy guardando la imagen en el diccionario, no la ruta por ende image.open no funciona porque espera una ruta, no una imagen directamente
        imagen = datosPoliPerros['foto'][i]
        imagen.show()

def mostrarxhuella():
    opc = (input("Ingrese la huella dactilar del poliperro: "))
    for i in range (len(datosPoliPerros["nombre"])):
        if (opc == datosPoliPerros['huellaDactilar'][i]):
            print(f"Datos poliperro {i+1}")
            print(f"* Nombre: {datosPoliPerros['nombre'][i]}")
            print(f"* Huella dactilar: {datosPoliPerros['huellaDactilar'][i]}")
            imagen = datosPoliPerros['foto'][i]
            imagen.show()
        else:
            print("\nERROR: Huella dactilar no encontrada")

def importarArchivo():
    archivo = open("poliperrox.txt","r")
    lineas = archivo.readlines()
    for i in lineas:
        print(i,end="")
    archivo.close()

def main(): #En esta funcion se ejecutaran las demas
    print("=======================POLIPERROS=======================")
    opc = menu()
    while (opc != 5):
        if (opc == 1):
            numPerros = int(input("Ingrese el numero de poliperros a registrar: "))
            registrarPoliPerros(numPerros)
        elif (opc == 2):
            mostrarPoliPerros()
        elif (opc == 3):
            mostrarxhuella()
        elif (opc == 4):
            importarArchivo()
        opc = menu()

main() #Se llama a la funcion

