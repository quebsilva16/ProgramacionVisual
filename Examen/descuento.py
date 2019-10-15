# EXAMEN PROGRAMACION VISUAL

# EJERCICIO 7: DESCUENTO

# ALUMNO

"""
NOMBRE: Miguel del Angel QUeb Silva
MATERIA: Programacion Visual
"""

desc = int(input("Ingresa el porcentaje de descuento: "))

importe = float(input("Ingresa el importe del producto: "))

def descuento(desc, importe):

	dicc = {
	
	"Descuento": desc,
	"Importe": importe

	}

	descuentos = importe * desc / 100 

	resultado = importe - descuentos

	print("El importe del producto es: $" + str(dicc["Importe"]) + " y su descuento es de: " + str(dicc["Descuento"]) + "%")

	print("El costo del producto despues del descuento es de: $", resultado)

descuento(desc, importe)