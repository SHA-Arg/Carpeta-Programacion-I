
def validar_dni(dni):
    return 5000000 <= dni <= 99999999


def validar_salario(salario):
    return salario >= 234315


def validar_puesto(puesto):
    return puesto in ["Gerente", "Supervisor", "Analista", "Encargado", "Asistente"]
