UTN - MathLab

Desarrollar un menú de usuarios con las siguientes opciones:
Seleccionar figura y cargar valores: dará opción al usuario para  elegir: Circulo, Rectangulo y Triangulo. Según su elección, se le solicitará que ingrese los parámetros necesarios para calcular el área y el perímetro de la figura. Además se deberá seleccionar el color con el que se representará la figura (utilizar la función seleccionar_color). Para ello crearán un diccionario que guarde en distintas claves los valores necesarios.
Visualizar resultados: se realizan los cálculos (perímetro y área) llamando a las funciones correspondientes y haciendo uso adecuado de los datos del diccionario.

Salir


Especificaciones técnicas:

Diccionarios:
Los datos de una figura deberán estar representados en un diccionario, en el mismo se especificará: tipo de figura geométrica (string), dimensiones (tuple), posición inicial (tuple) y el color de la figura (tuple).

Módulos a completar:

Módulo main:
inicio_programa(): creará el menú de opciones, permitiendo interactuar con el usuario, solicitando los datos necesarios en función de la figura seleccionada. 




Módulo Gráfico:
seleccionar_color(mensaje): despliega en pantalla todos los colores del diccionario y le permite al usuario seleccionar uno. Retorna la tupla con el valor del color seleccionado.
calcular_figura(figura, ventana): dependiendo del tipo de figura llamara a una función para calcular el área y el perímetro. Luego dibujara la figura en una pantalla de pygame y escribirá los resultados en la misma (estas funciones ya se encuentran implementadas)

Módulo Funciones:
calcular_area_rectangulo(base, altura): calcula y retorna el área del rectángulo de base y altura determinada.
calcular_perimetro_rectangulo(base, altura): calcula y retorna el perímetro del rectángulo de base y altura determinada.
calcular_area_circulo(radio): calcula y retorna el área del círculo de radio determinado.
calcular_perimetro_circulo(radio): calcula y retorna el perímetro del círculo de radio determinado.
calcular_area_triangulo_rectangulo(base, altura): calcula y retorna el área del triángulo de base y altura determinada.
calcular_perimetro_triangulo_rectangulo(base, altura): calcula y retorna el perímetro del triángulo de base y altura determinada.

Repositorio 
