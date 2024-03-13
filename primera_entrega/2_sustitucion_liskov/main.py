#Importar clases
from figuras import Cuadrado, Rectangulo

#Implementación figura cuadrado
cuadrado = Cuadrado(5)
print("Área del cuadrado:", cuadrado.area())
print("Perímetro del cuadrado:", cuadrado.perimetro())

#Implementación figura rectángulo
rectangulo = Rectangulo(4, 6)
print("Área del rectángulo:", rectangulo.area())
print("Perímetro del rectángulo:", rectangulo.perimetro())