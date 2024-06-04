# Nombre : Sebastian
# Apellido : Hereñu Amaral
# División: 112

# ESTA FUNCION AYUDA A VALIDAR EL INGRESO DEL USUARIO DENTRO DE LA FUNCION solicitar_entero()


def es_entero(ingreso):
    for caracter in ingreso:
        if caracter not in ('-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            return False
    return True


# ESTA FUNCION AYUDA A VALIDAR EL INGRESO DEL USUARIO DENTRO DE LA FUNCION solicitar_flotante()

def es_flotante(ingreso):
    punto_ingresado = False
    for caracter in ingreso:
        if caracter == '.':
            if punto_ingresado:
                return False
            punto_ingresado = True
        elif caracter not in ('-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            return False
    return True

# ESTA FUNCION AYUDA A VALIDAR EL INGRESO DEL USUARIO DENTRO DE LA FUNCION solicitar_cadena()


def es_cadena_vacia(cadena):
    if cadena == "":
        return True
    return False
