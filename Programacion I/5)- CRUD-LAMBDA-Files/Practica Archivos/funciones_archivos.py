"""Práctica Archivos

1 - Crear una función que reciba como parámetros una lista de números y el path de un archivo. La misma deberá guardar la lista en un archivo de texto.
2 - Crear una función que reciba como parámetro el path de un archivo. La misma deberá leer el archivo del ejercicio anterior, solo dejando pasar a la lista los números múltiplos de 2.
3 - Crear una función que reciba como parámetros dos paths: uno correspondiente a un archivo de origen y otro correspondiente a un archivo de destino. La función debe leer el contenido del archivo de origen y luego transcribirlo en el archivo de destino. En caso de error la función retornará algún tipo de código de error indicando que paso.
4 - Crear una función llamada contar_elementos que recibe como parámetro el path de un archivo de texto que contiene un poema. La función deberá contar la cantidad de líneas, la cantidad de palabras y la cantidad de caracteres que contiene el poema. La función retornará un diccionario con los datos obtenidos.

"""

# especificar donde se guardará el archivo
path = 'C:/Users/Usuario/Desktop/Python-Course/Programacion%20I/5%29-%20CRUD-LAMBDA-Files/Practica%20Archivos/numeros.txt'
# Función 1: Guardar una lista de números en un archivo de texto


def guardar_lista_en_archivo(numeros, path):
    with open(path, 'w') as archivo:
        for numero in numeros:
            archivo.write(f"{numero}\n")
    print(f"Lista de números guardada exitosamente en {path}.")
    return 0  # 0 indica que la operación fue exitosa


# Función 2: Leer un archivo y devolver solo los múltiplos de 2
def leer_multiplos_de_dos(path):
    multiplos_de_dos = []
    with open(path, 'r') as archivo:
        for linea in archivo:
            numero = int(linea.strip())
            if numero % 2 == 0:
                multiplos_de_dos.append(numero)
    return multiplos_de_dos

# Función 3: Transcribir contenido de un archivo de origen a un archivo de destino (copia)sin usar try except


def transcribir_archivo(origen, destino):
    with open(origen, 'r') as archivo_origen:
        contenido = archivo_origen.read()

    with open(destino, 'w') as archivo_destino:
        archivo_destino.write(contenido)

    return 0  # 0 indica que la operación fue exitosa

# Función 4: Contar elementos en un archivo de texto que contiene un poema


def contar_elementos(path):
    with open(path, 'r') as archivo:
        contenido = archivo.read()

    lineas = contenido.split('\n')
    palabras = contenido.split()
    caracteres = len(contenido)

    return {
        "lineas": len(lineas),
        "palabras": len(palabras),
        "caracteres": caracteres
    }
