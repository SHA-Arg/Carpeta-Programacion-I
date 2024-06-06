# Funciones en Python

def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def division(a, b):
    return a / b


def potencia(a, b):
    return a ** b


def raiz_cuadrada(a):
    return a ** 0.5


def raiz_cubica(a):
    return a ** (1/3)


def area_circulo(radio):
    return 3.1416 * radio ** 2


def area_triangulo(base, altura):
    return (base * altura) / 2


def area_cuadrado(lado):
    return lado ** 2


def area_rectangulo(base, altura):
    return base * altura


def area_trapecio(base_mayor, base_menor, altura):
    return ((base_mayor + base_menor) * altura) / 2


def area_rombo(diagonal_mayor, diagonal_menor):
    return (diagonal_mayor * diagonal_menor) / 2


def area_poligono_regular(perimetro, apotema):
    return (perimetro * apotema) / 2


def area_cubo(lado):
    return 6 * lado ** 2


def area_cilindro(radio, altura):
    return 2 * 3.1416 * radio * (radio + altura)


def area_cono(radio, generatriz):
    return 3.1416 * radio * (radio + generatriz)


def area_esfera(radio):
    return 4 * 3.1416 * radio ** 2


def area_piramide_regular(perimetro_base, apotema_base, apotema_lateral):
    return (perimetro_base * apotema_base) / 2 + perimetro_base * apotema_lateral


def area_prisma_regular(perimetro_base, apotema_base, altura_prisma):
    return 2 * (perimetro_base * apotema_base) + perimetro_base * altura_prisma

# Funciones complementarias para el manejo de listas


def promedio(lista):
    suma = 0
    for elemento in lista:
        suma += elemento
    return suma / len(lista)


def mediana(lista):
    lista.sort()
    n = len(lista)
    if n % 2 == 0:
        mediana = (lista[n // 2] + lista[n // 2 - 1]) / 2
    else:
        mediana = lista[n // 2]
    return mediana


def moda(lista):
    frecuencias = {}
    for elemento in lista:
        if elemento in frecuencias:
            frecuencias[elemento] += 1
        else:
            frecuencias[elemento] = 1
    maximo = max(frecuencias.values())
    moda = [key for key in frecuencias if frecuencias[key] == maximo]
    return moda


def varianza(lista):
    suma = 0
    prom = promedio(lista)
    for elemento in lista:
        suma += (elemento - prom) ** 2
    return suma / len(lista)


def desviacion_estandar(lista):
    return varianza(lista) ** 0.5


def rango(lista):
    return max(lista) - min(lista)


def coeficiente_correlacion(lista1, lista2):
    n = len(lista1)
    suma_x = 0
    suma_y = 0
    suma_x2 = 0
    suma_y2 = 0
    suma_xy = 0
    for i in range(n):
        suma_x += lista1[i]
        suma_y += lista2[i]
        suma_x2 += lista1[i] ** 2
        suma_y2 += lista2[i] ** 2
        suma_xy += lista1[i] * lista2[i]
    numerador = n * suma_xy - suma_x * suma_y
    denominador = ((n * suma_x2 - suma_x ** 2) *
                   (n * suma_y2 - suma_y ** 2)) ** 0.5
    return numerador / denominador


def covarianza(lista1, lista2):
    n = len(lista1)
    suma_x = 0
    suma_y = 0
    suma_xy = 0
    for i in range(n):
        suma_x += lista1[i]
        suma_y += lista2[i]
        suma_xy += lista1[i] * lista2[i]
    return (n * suma_xy - suma_x * suma_y) / n


def correlacion(lista1, lista2):
    return covarianza(lista1, lista2) / (desviacion_estandar(lista1) * desviacion_estandar(lista2))


def regresion_lineal(lista1, lista2):
    n = len(lista1)
    suma_x = 0
    suma_y = 0
    suma_x2 = 0
    suma_xy = 0
    for i in range(n):
        suma_x += lista1[i]
        suma_y += lista2[i]
        suma_x2 += lista1[i] ** 2
        suma_xy += lista1[i] * lista2[i]
    a = (n * suma_xy - suma_x * suma_y) / (n * suma_x2 - suma_x ** 2)
    b = (suma_y - a * suma_x) / n
    return a, b


def regresion_lineal_prediccion(a, b, x):
    return a * x + b


def regresion_lineal_error(lista1, lista2):
    a, b = regresion_lineal(lista1, lista2)
    n = len(lista1)
    suma = 0
    for i in range(n):
        suma += (lista2[i] - a * lista1[i] - b) ** 2
    return suma / n


def regresion_lineal_coeficiente_determinacion(lista1, lista2):
    a, b = regresion_lineal(lista1, lista2)
    n = len(lista1)
    suma_y = 0
    for i in range(n):
        suma_y += lista2[i]
    prom_y = suma_y / n
    suma_total = 0
    suma_residual = 0
    for i in range(n):
        suma_total += (lista2[i] - prom_y) ** 2
        suma_residual += (lista2[i] - a * lista1[i] - b) ** 2
    return 1 - suma_residual / suma_total


def regresion_lineal_coeficiente_correlacion(lista1, lista2):
    return regresion_lineal_coeficiente_determinacion(lista1, lista2) ** 0.5


def regresion_lineal_coeficiente_correlacion_cuadrado(lista1, lista2):
    return regresion_lineal_coeficiente_determinacion(lista1, lista2)


def regresion_lineal_coeficiente_correlacion_ajustado(lista1, lista2):
    a, b = regresion_lineal(lista1, lista2)
    n = len(lista1)
    k = 1
    suma = 0
    for i in range(n):
        suma += (lista2[i] - a * lista1[i] - b) ** 2
    return 1 - (suma / (n - k - 1)) / (varianza(lista2) * (n - 1) / (n - k))


def regresion_lineal_coeficiente_correlacion_prediccion(lista1, lista2):
    a, b = regresion_lineal(lista1, lista2)
    n = len(lista1)
    suma = 0
    for i in range(n):
        suma += (lista2[i] - a * lista1[i] - b) ** 2
    return (1 - (suma / (n - 2)) / varianza(lista2)) ** 0.5


def regresion_lineal_coeficiente_correlacion_prediccion_cuadrado(lista1, lista2):
    a, b = regresion_lineal(lista1, lista2)
    n = len(lista1)
    suma = 0
    for i in range(n):
        suma += (lista2[i] - a * lista1[i] - b) ** 2
    return 1 - (suma / (n - 2)) / varianza(lista2)


def regresion_lineal_coeficiente_correlacion_prediccion_ajustado(lista1, lista2):
    a, b = regresion_lineal(lista1, lista2)
    n = len(lista1)
    k = 1
    suma = 0
    for i in range(n):
        suma += (lista2[i] - a * lista1[i] - b) ** 2
    return 1 - (suma / (n - k - 1)) / (varianza(lista2) * (n - 1) / (n - k))


def regresion_lineal_coeficiente_correlacion_prediccion_ajustado_cuadrado(lista1, lista2):
    a, b = regresion_lineal(lista1, lista2)
    n = len(lista1)
    k = 1
    suma = 0
    for i in range(n):
        suma += (lista2[i] - a * lista1[i] - b) ** 2
    return 1 - (suma / (n - k - 1)) / varianza(lista2)


def diccionario_promedio(diccionario):
    suma = 0
    n = 0
    for key in diccionario:
        suma += diccionario[key]
        n += 1
    return suma / n


def diccionario_mediana(diccionario):
    lista = list(diccionario.values())
    lista.sort()
    n = len(lista)
    if n % 2 == 0:
        mediana = (lista[n // 2] + lista[n // 2 - 1]) / 2
    else:
        mediana = lista[n // 2]
    return mediana


def diccionario_moda(diccionario):
    frecuencias = {}
    for key in diccionario:
        if diccionario[key] in frecuencias:
            frecuencias[diccionario[key]] += 1
        else:
            frecuencias[diccionario[key]] = 1
    maximo = max(frecuencias.values())
    moda = [key for key in frecuencias if frecuencias[key] == maximo]
    return moda


def diccionario_varianza(diccionario):
    suma = 0
    prom = diccionario_promedio(diccionario)
    n = 0
    for key in diccionario:
        suma += (diccionario[key] - prom) ** 2
        n += 1
    return suma / n


def diccionario_desviacion_estandar(diccionario):
    return diccionario_varianza(diccionario) ** 0.5


def diccionario_rango(diccionario):
    return max(diccionario.values()) - min(diccionario.values())


def diccionario_coeficiente_correlacion(diccionario1, diccionario2):
    n = 0
    suma_x = 0
    suma_y = 0
    suma_x2 = 0
    suma_y2 = 0
    suma_xy = 0
    for key in diccionario1:
        if key in diccionario2:
            suma_x += diccionario1[key]
            suma_y += diccionario2[key]
            suma_x2 += diccionario1[key] ** 2
            suma_y2 += diccionario2[key] ** 2
            suma_xy += diccionario1[key] * diccionario2[key]
            n += 1
    numerador = n * suma_xy - suma_x * suma_y
    denominador = ((n * suma_x2 - suma_x ** 2) *
                   (n * suma_y2 - suma_y ** 2)) ** 0.5
    return numerador / denominador


def diccionario_covarianza(diccionario1, diccionario2):
    n = 0
    suma_x = 0
    suma_y = 0
    suma_xy = 0
    for key in diccionario1:
        if key in diccionario2:
            suma_x += diccionario1[key]
            suma_y += diccionario2[key]
            suma_xy += diccionario1[key] * diccionario2[key]
            n += 1
    return (n * suma_xy - suma_x * suma_y) / n


def diccionario_correlacion(diccionario1, diccionario2):
    return diccionario_covarianza(diccionario1, diccionario2) / (diccionario_desviacion_estandar(diccionario1) * diccionario_desviacion_estandar(diccionario2))


def tupla_promedio(tupla):
    suma = 0
    for elemento in tupla:
        suma += elemento
    return suma / len(tupla)


def tupla_mediana(tupla):
    lista = list(tupla)
    lista.sort()
    n = len(lista)
    if n % 2 == 0:
        mediana = (lista[n // 2] + lista[n // 2 - 1]) / 2
    else:
        mediana = lista[n // 2]
    return mediana


def tupla_moda(tupla):
    frecuencias = {}
    for elemento in tupla:
        if elemento in frecuencias:
            frecuencias[elemento] += 1
        else:
            frecuencias[elemento] = 1
    maximo = max(frecuencias.values())
    moda = [key for key in frecuencias if frecuencias[key] == maximo]
    return moda


def tupla_varianza(tupla):
    suma = 0
    prom = tupla_promedio(tupla)
    for elemento in tupla:
        suma += (elemento - prom) ** 2
    return suma / len(tupla)


def tupla_desviacion_estandar(tupla):
    return tupla_varianza(tupla) ** 0.5
