class Personaje:

    # Atributos

    # nombre
    # usa_nanotecnologia
    # vuela
    # super_poder
    # poder_pelea

    # Constructor // iniciliza los atributos de la clase
    def __init__(self, nomb: str, nano: bool, vuela: bool, poder: str, pelea: int):
        self.nombre = nomb
        self.usa_nanotecnologia = nano
        self.puede_volar = vuela
        self.super_poder = poder
        self.poder_pelea = pelea

    # Metodos
    def presentarse(self):
        mensaje = f"{self.nombre} - {self.poder_pelea} - {self.super_poder}"
        if self.usa_nanotecnologia:
            mensaje += f" - Usa nanotecnologia"
        else:
            mensaje += f" - No usa nanotecnologia"

        return mensaje

    def volar(self, altura: float, velocidad: int):
        if self.puede_volar == True:
            print(f"Estoy volando a {
                  altura} mts de altura a una velocidad de {velocidad} km/h")
        else:
            print(f"{self.nombre} usted no puede volar")

    def atacar(self, enemigo: 'Personaje'):
        if self.poder_pelea > enemigo.poder_pelea:
            print(f"GANO {self.nombre}")
            self.poder_pelea -= enemigo.poder_pelea
            enemigo.poder_pelea = 0
        elif self.poder_pelea < enemigo.poder_pelea:
            print(f"GANO {self.nombre}")
            enemigo.poder_pelea -= self.poder_pelea
            self.poder_pelea = 0
        else:
            print("EMPATE")
