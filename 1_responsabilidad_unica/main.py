#Importar clase
from calculadora import CALCULADORA

#Instanciar clase
instance_calculate = CALCULADORA()

#Declaración de vriables
number1=1
number2=2

#Implementación de métodos
suma = instance_calculate.sumar(number1, number2)
resta = instance_calculate.restar(number1, number2)
multiplicacion = instance_calculate.multiplicar(number1, number2)
division = instance_calculate.dividir(number1, number2)

#Mostrar resultados
print('suma', suma)
print('Resta', resta)
print('Multiplicación', multiplicacion)
print('División', division)