# Explicacion de los keyword arguments en Python

# Los keyword arguments en Python son una forma de pasar argumentos a una funcion utilizando el nombre del parametro al que se le va a asignar el valor. Esto nos permite especificar los valores de los parametros de una funcion en cualquier orden, lo que hace que el codigo sea mas legible y facil de entender.

# Por ejemplo:

def imprimir_nombre(primer_nombre, segundo_nombre, primer_apellido, segundo_apellido):
    print(f"Nombre completo: {primer_nombre} {segundo_nombre} {
          primer_apellido} {segundo_apellido}")

# Keyword arguments


imprimir_nombre(primer_nombre="Juan", segundo_nombre="Carlos",
                primer_apellido="Perez", segundo_apellido="Gomez")
# Output: Nombre completo: Juan Carlos Perez Gomez

imprimir_nombre(primer_apellido="Perez", segundo_apellido="Gomez",
                primer_nombre="Juan", segundo_nombre="Carlos")
# Output: Nombre completo: Juan Carlos Perez Gomez


# Otra ventaja de los keyword arguments es que nos permiten definir valores por defecto para los parametros de una funcion. Esto significa que si no se especifica un valor para un parametro al llamar a la funcion, se utilizara el valor por defecto.

# Por ejemplo:

# Keyword arguments con valores por defecto
def conectar_db(**kwargs):
    print(type(kwargs))
    print(kwargs)


conectar_db(host="localhost", puerto=3306, usuario="admin", contrasena="1234")


def conectar_db2(**kwargs):
    nombre = kwargs.get('nombre', 'default')
    user = kwargs['usuario']
    password = kwargs['password']
    port = kwargs['port']
    dir_db = kwargs['dir_db']
    print(f"Conectando a la base de datos {nombre} en {dir_db} en el puerto {
          port} con el usuario {user} y la contrasena {password}")


conectar_db2(usuario="admin", password="1234", port=3306,
             dir_db="localhost", query="SELECT * FROM users")
# Output: {'host': 'localhost', 'puerto': 3306, 'usuario': 'admin', 'contrasena': '1234'}

# En este caso, la funcion conectar_db recibe un numero variable de keyword arguments y los imprime en la consola. Cuando se llama a la funcion, se especifican los valores de los parametros utilizando el nombre del parametro correspondiente. Esto hace que el codigo sea mas legible y facil de entender, ya que no es necesario recordar el orden de los parametros. Ademas, la funcion conectar_db2 tiene un parametro con un valor por defecto (nombre='default'), lo que significa que si no se especifica un valor para ese parametro al llamar a la funcion, se utilizara el valor por defecto. Puede tener mas argumentos que los que se definieron en la funcion, pero no se usaran. En este caso, el argumento query no se usa en la funcion.

# Otro uso comun de los keyword arguments es en el desempaquetado de diccionarios. Esto nos permite pasar un diccionario como argumento a una funcion y desempaquetar sus elementos en los parametros de la funcion.

# Por ejemplo:

datos = {"host": "localhost", "puerto": 3306,
         "usuario": "admin", "contrasena": "1234"}

conectar_db(**datos)
# Output: {'host': 'localhost', 'puerto': 3306, 'usuario': 'admin', 'contrasena': '1234'}

# En resumen, los keyword arguments en Python son una forma de pasar argumentos a una funcion utilizando el nombre del parametro al que se le va a asignar el valor. Esto nos permite especificar los valores de los parametros de una funcion en cualquier orden, lo que hace que el codigo sea mas legible y facil de entender. Ademas, los keyword arguments nos permiten definir valores por defecto para los parametros de una funcion y desempaquetar diccionarios como argumentos de una funcion. Los keyword arguments son una herramienta poderosa que nos permite escribir codigo mas limpio, legible y facil de mantener.
