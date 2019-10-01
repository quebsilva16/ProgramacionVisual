cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:

#print(car)

	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

respuesta = 17

if respuesta != 42:
	print('Esta respuesta no es correcta')

usuarios_baneados = ('pepe charly', 'jose', 'maria')

#py2.7 raw_input()
#p3.X input()

name = input('ingrese un nombre de usuario:')

if name not in usuarios_baneados:
	print(name.title() + " no esta baneado.")
else:
	print(name.title() + " si esta baneado.")
#validar si eres mayor de edad(18) puedes votar
edad = int(input("dame tu edad:"))

if edad >= 18:
	print('es mayor de edad:')
else:
	print('no es mayor de edad:')

"""
if-elif-else
la entrada para menores de 4 edad es gratuita
la entrada para cualquier persona entre las edades de 4 a 18 anos es de $50.
La entrada para cualquier persona mayor de 18 anos es de $ 100.
"""
age = int(input("dame tu edad:"))

if edad < 4:
	precio = 0
elif edad < 18:
	precio =50
else:
	precio = 100
print("Tu boleto cuesta " + str(precio))