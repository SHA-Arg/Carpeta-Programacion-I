# Ciclo while

# Inicializamos la variable
nombre = ''
correo = ''
mensaje = ''

condicion_salida = 'continuar'

while condicion_salida == 'continuar':
    nombre = input('Por favor ingrese su nombre: ')
    correo = input('Por favor ingrese su correo: ')
    mensaje = input('Por favor ingrese su mensaje: ')

    print(f"""
        Mensaje enviado por: {nombre}
        Correo: {correo}
        Mensaje: {mensaje}
        """)

    condicion_salida = input('Desea continuar? (continuar/salir): ')
