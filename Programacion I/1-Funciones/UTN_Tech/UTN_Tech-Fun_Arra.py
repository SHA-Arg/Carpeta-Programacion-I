'''
----------------------------------
#                                #
# Nombre : Sebastian             #
# Apellido : Hereñu Amaral       #
# División: 112                  #
#                                #
----------------------------------
'''

# -----------------------------------------------
# INICIALIZACION DE VARIABLES
# -----------------------------------------------

nombre_empleado = ""
edad = 0
edad_masc = 0
edad_fem = 0
edad_otro = 0
genero = ""
tecnologia = ""
mayor_edad = 0
contador_masc_votaron_IOT_IA = 0
contador_no_votaron_IA = 0
contador_masc = 0
contador_fem = 0
contador_otro = 0
contador_masc_edad_25_50 = 0
nombre_mayor_edad = ""
tecnologia_mayor_edad = ""

# -----------------------------------------------
# FUNCIONES DE VALIDACION
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

    # -----------------------------------------------
    # CALCULOS SOLICITADOS
    # -----------------------------------------------

    if genero == "Masculino":
        contador_masc += 1
        edad_masc += edad
        if 25 <= edad <= 50 and tecnologia in ["IOT", "IA"]:
            contador_masc_votaron_IOT_IA += 1
        if edad > mayor_edad:
            mayor_edad = edad
            nombre_mayor_edad = nombre_empleado
            tecnologia_mayor_edad = tecnologia
    elif genero == "Femenino":
        contador_fem += 1
        edad_fem += edad
    elif genero == "Otro":
        contador_otro += 1
        edad_otro += edad

    if genero != "Femenino" and 33 <= edad <= 40:
        contador_no_votaron_IA += 1

# -----------------------------------------------
# MOSTRAR RESULTADOS
# -----------------------------------------------

print("\n>>> RESULTADOS DE LA ENCUESTA <<<")
print(f"\nEmpleados de género masculino que votaron por IOT o IA, cuya edad está entre 25 y 50 años: {
      contador_masc_votaron_IOT_IA}")
print(f"\nPorcentaje de empleados que no votaron por IA (33-40 años, no Femenino): {
      contador_no_votaron_IA}")
print(f"\nEmpleado de género masculino con mayor edad: {
      nombre_mayor_edad} ({mayor_edad} años) que votó por {tecnologia_mayor_edad}")
