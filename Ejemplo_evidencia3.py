class Cuadrado:
    def __init__ (Self, Lado):
        Self.lado = 0
        Self.Area = 0
    
    def ingresar_datos (Self):
       self.lado = float(input("Ingresa el valor del lado"))
       
    def Calcular_area (Self):
        return self.Area ** 2
    def Resultado(Self):
        print(f"lado: {Self.lado}")
        print(f"Area: {Self.Area}")