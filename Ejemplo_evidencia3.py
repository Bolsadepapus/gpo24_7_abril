class Cuadrado:
    def __init__ (self, lado):
        self.lado = lado
        
    def area (self):
       return self.lado ** 2 
       
lado = int(input("Ingresa el valor del lado: "))

Cuadradoo = Cuadrado(lado)
print ("El area del Cuadrado es: ", Cuadrado.area())