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
# CARGA DE DATOS CON VALIDACIONES
# -----------------------------------------------


print(">>>                         ENCUESTA DE UTN TECHNOLOGIES                                        <<<\n")
for i in range(5):
    nombre_empleado = input("\n>> Ingrese el nombre de un empleado: ")
    if nombre_empleado == "":
        nombre_empleado = input("\n<!> Ingrese un nombre de empleado: ")

    edad = input("\n>> Ingrese la edad (no menor a 18): ")
    if edad < 18:
        edad = input("\n<!> Ingrese una edad valida (no menor a 18): ")

    genero = input("\n<!> Ingrese el genero (Masculino - Femenino - Otro): ")
    if genero != "Masculino" and genero != "Femenino" and genero != "Otro":
        genero = input(
            "\n<!> Ingrese un genero valido (Masculino - Femenino - Otro): ")

    tecnologia = input("\n>> Ingrese la tecnologia (IA, RV/RA, IOT): ")
    if tecnologia != "IA" and tecnologia != "RV/RA" and tecnologia != "IOT":
        tecnologia = input(
            "\n<!> Ingrese una tecnologia valida (IA, RV/RA, IOT): ")


# -----------------------------------------------
# CALCULOS SOLICITADOS
# -----------------------------------------------

    # <=> Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años inclusive.
    if genero == "Masculino" and (tecnologia == "IOT" or tecnologia == "IA") and (edad >= 25 and edad <= 50):
        contador_masc_votaron_IOT_IA += 1

    # <=> Porcentaje de empleados que no votaron por IA, siempre y cuando
    if genero != "Femenino" and (edad >= 33 and edad <= 40):
        contador_no_votaron_IA += 1

    # <=> Nombre y tecnología que votó, de los empleados de género masculino
    if genero == "Masculino":
        contador_masc += 1
        edad_masc += edad
    elif genero == "Femenino":
        contador_fem += 1
        edad_fem += edad
    elif genero == "Otro":
        contador_otro += 1
        edad_otro += edad

    #  <=> Nombre y tecnología que votó, de los empleados de género masculino con mayor edad de ese género.
    if genero == "Masculino" and edad > mayor_edad:
        mayor_edad = edad
        nombre_mayor_edad = nombre_empleado
        tecnologia_mayor_edad = tecnologia

# -----------------------------------------------
# IMPRESION DE RESULTADOS
# -----------------------------------------------


print(f"\n>> Cantidad de empleados de género masculino que votaron por IOT o IA, y cuya edad esta entre 25 y 50 años inclusive es:\n{
      contador_masc_votaron_IOT_IA} empleado/s.")

print(f"\n>> Porcentaje de empleados que no voto por IA, y su género no es Femenino o su edad es entre los 33 y 40 años es:\n{
      contador_no_votaron_IA} %.")

# MI INTERPRETACION DEL ENUNCIADO
print(f"\n>> Nombre y tecnología que votó el empleado masculino con mayor edad fue:\nNombre: {
      nombre_mayor_edad} y la tecnologia fue {tecnologia_mayor_edad}.")

print(">>>                         FIN DE LA ENCUESTA                                        <<<\n")


# -----------------------------------------------
