class Clientes:
    def __init__(self, nombre, apellido, edad, mail):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.mail = mail
    def __str__(self):
        return f"nombre: {self.nombre}, apellido {self.apellido}, edad {self.edad}, mail {self.mail}"
    