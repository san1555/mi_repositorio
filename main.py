from paquete1.modulo1 import Clientes
from paquete1.modulo2 import Auto

class Main:
    for i in range(0,2):
        print ("Clientes")
        nombre= input ("ingresar nombre")
        apellido= input ("ingresar apellido")
        edad= int(input ("ingresar edad"))
        mail= input ("ingresar mail")
        print("Auto")
        modelo = input ("ingresar modelo")
        año = int(input("ingresar año"))
        color = input("ingresar color")
        clientes= Clientes(nombre, apellido, edad, mail)
        auto= Auto (modelo,año,color)
        print(clientes.__str__())
        print (auto.__str__())
        