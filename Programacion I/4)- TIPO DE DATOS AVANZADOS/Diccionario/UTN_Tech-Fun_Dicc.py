# Nombre : Sebastian
# Apellido : Hereñu Amaral
# División: 112


# -----------------------------------------------
# INICIALIZACION DE VARIABLES
# -----------------------------------------------

empleados = []
estadisticas = {
    "edad_masc": 0,
    "edad_fem": 0,
    "edad_otro": 0,
    "contador_masc_votaron_IOT_IA": 0,
    "contador_no_votaron_IA": 0,
    "contador_masc": 0,
    "contador_fem": 0,
    "contador_otro": 0,
    "mayor_edad": 0,
    "nombre_mayor_edad": "",
    "tecnologia_mayor_edad": ""
}

# -----------------------------------------------
# FUNCIONES DE VALIDACIONe
# -----------------------------------------------


def obtener_nombre():
    nombre = input("\n>> Ingrese el nombre de un empleado: ")
    while not nombre.strip():
        nombre = input("\n<!> Ingrese el nombre de un empleado válido: ")
    return nombre


def obtener_edad():
    edad = int(input("\n>> Ingrese la edad (no menor a 18): "))
    while edad < 18:
        edad = int(input("\n<!> Ingrese la edad (no menor a 18): "))
    return edad


def obtener_genero():
    genero = input("\n>> Ingrese el genero (Masculino - Femenino - Otro): ")
    while genero not in ["Masculino", "Femenino", "Otro"]:
        genero = input(
            "\n<!> Ingrese el genero válido (Masculino - Femenino - Otro): ")
    return genero


def obtener_tecnologia():
    tecnologia = input("\n>> Ingrese la tecnologia (IA, RV/RA, IOT): ")
    while tecnologia not in ["IA", "RV/RA", "IOT"]:
        tecnologia = input(
            "\n<!> Ingrese una de estas tecnologias válidas (IA, RV/RA, IOT): ")
    return tecnologia

# -----------------------------------------------
# CARGA DE DATOS CON VALIDACIONES
# -----------------------------------------------


for _ in range(5):
    print(">>> ENCUESTA DE UTN TECHNOLOGIES <<<\n")
    nombre_empleado = obtener_nombre()
    edad = obtener_edad()
    genero = obtener_genero()
    tecnologia = obtener_tecnologia()

    empleados.append({
        "nombre": nombre_empleado,
        "edad": edad,
        "genero": genero,
        "tecnologia": tecnologia
    })

    # -----------------------------------------------
    # CALCULOS SOLICITADOS
    # -----------------------------------------------

    if genero == "Masculino":
        estadisticas["contador_masc"] += 1
        estadisticas["edad_masc"] += edad
        if 25 <= edad <= 50 and tecnologia in ["IOT", "IA"]:
            estadisticas["contador_masc_votaron_IOT_IA"] += 1
        if edad > estadisticas["mayor_edad"]:
            estadisticas["mayor_edad"] = edad
            estadisticas["nombre_mayor_edad"] = nombre_empleado
            estadisticas["tecnologia_mayor_edad"] = tecnologia
    elif genero == "Femenino":
        estadisticas["contador_fem"] += 1
        estadisticas["edad_fem"] += edad
    elif genero == "Otro":
        estadisticas["contador_otro"] += 1
        estadisticas["edad_otro"] += edad

    if genero != "Femenino" and 33 <= edad <= 40:
        estadisticas["contador_no_votaron_IA"] += 1

# -----------------------------------------------
# MOSTRAR RESULTADOS
# -----------------------------------------------

print("\n>>> RESULTADOS DE LA ENCUESTA <<<")
print(f"\nEmpleados de género masculino que votaron por IOT o IA, cuya edad está entre 25 y 50 años: {
      estadisticas['contador_masc_votaron_IOT_IA']}")
print(f"\nPorcentaje de empleados que no votaron por IA (33-40 años, no Femenino): {
      estadisticas['contador_no_votaron_IA']}")
print(f"\nEmpleado de género masculino con mayor edad: {estadisticas['nombre_mayor_edad']} ({
      estadisticas['mayor_edad']} años) que votó por {estadisticas['tecnologia_mayor_edad']}")
