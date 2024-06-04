from funciones_archivos import *

# Crear una lista de números y guardarla en un archivo
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
path_lista = "numeros.txt"
guardar_lista_en_archivo(lista_numeros, path_lista)

# Leer el archivo y obtener solo los múltiplos de 2
multiplos_de_dos = leer_multiplos_de_dos(path_lista)
print(f"Múltiplos de 2 en {path_lista}: {multiplos_de_dos}")

# Transcribir contenido de un archivo a otro
origen_path = "origen.txt"
destino_path = "destino.txt"
transcribir_archivo(origen_path, destino_path)

# Contar elementos en un archivo de texto (poema)
poema_path = "poema.txt"
conteo_elementos = contar_elementos(poema_path)
print(f"Conteo de elementos en {poema_path}: {conteo_elementos}")
