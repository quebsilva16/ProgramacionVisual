"""
Ejercicio de Python 4: VALIDACION DE EDAD
Nombre: Miguel del Angel Queb Silva
Materia: Programacion Visual
"""

edad = int(input("Ingresa tu edad: "))

if edad < 18:
	print("Eres menor de edad y no puedes votar")

else:
	print("Eres mayor de edad y puedes votar")