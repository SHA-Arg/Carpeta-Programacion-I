def generar_csv(path: str, lista: list):
    with open(path, 'w', encoding= "utf8") as archivo:
        for elemento in lista:
            cadena = f"{elemento['title']},{elemento['views']},{elemento['url']}\n"
            archivo.write(cadena)
            
            
def parser_csv(path: str) -> list:
    lista = []
    with open(path, 'r', encoding= "utf8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            linea = linea.split(",")
            diccionario = {
                "title": linea[0],
                "views": linea[1],
                "url": linea[2]
            }
            lista.append(diccionario)
    return lista

