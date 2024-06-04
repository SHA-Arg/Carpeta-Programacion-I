# Función 1: Guardar una lista de números en un archivo de texto
def guardar_lista_en_archivo(lista, path):
    with open(path, 'w') as archivo:
        for numero in lista:
            archivo.write(f"{numero}\n")
    print(f"Lista guardada exitosamente en {path}.")


# Función 2: Leer un archivo y devolver solo los múltiplos de 2
def leer_multiplos_de_dos(path):
    multiplos_de_dos = []
    with open(path, 'r') as archivo:
        for linea in archivo:
            numero = int(linea.strip())
            if numero % 2 == 0:
                multiplos_de_dos.append(numero)
    return multiplos_de_dos

# Función 3: Transcribir contenido de un archivo de origen a un archivo de destino


def transcribir_archivo(origen_path, destino_path):
    with open(origen_path, 'r') as archivo_origen:
        contenido = archivo_origen.read()
    with open(destino_path, 'w') as archivo_destino:
        archivo_destino.write(contenido)
    print(f"Contenido transcrito exitosamente de {
          origen_path} a {destino_path}.")
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
