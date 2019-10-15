# EXAMEN PROGRAMACION VISUAL

# EJERCICIO 5: DICCIONARIO

# ALUMNO

"""
NOMBRE: Miguel del Angel QUeb Silva
MATERIA: Programacion Visual
"""
nombre = input('¿Cómo te llamas? ')
años = input('¿Cuántos años tienes? ')
dirección = input('¿Cuál es tu dirección? ')
teléfono = input('¿Cuál es tu número de teléfono? ')
persona = {'nombre': nombre, 'años': años, 'dirección': dirección, 'teléfono': teléfono}
print(persona['nombre'], 'tiene', persona['años'], 'años, vive en', persona['dirección'], 'y su número de teléfono es', persona['teléfono'])