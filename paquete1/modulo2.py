class Auto:
    def __init__(self, modelo, año, color):
        self.modelo = modelo
        self.año = año
        self.color = color
        
    def __str__(self):
        return f"modelo: {self.modelo}, año: {self.año}, color: {self.color}"
