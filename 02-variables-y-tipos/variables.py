"""
Una variable es un contener de información
que dentro guardará un dato, se pueden crear muchas
variables y que cada una tenga un dato distinto
"""

#crear variables y asignar un valor
texto = 'Master en Python'
numero= 31
decimal = 5.4

#mostrar valor de las variables
print(texto)
print(numero)
print(decimal)

#reasignar valor de las variables
numero = 109
decimal = 9.5
print(numero)
print(decimal)

print('-------------------------------')

#concatenación 

#unir variables 

nombre = "Miller Camilo"
apellidos = "Vega Diaz"
Nacionalidad = "Colombiano"

print( nombre + " " + apellidos + " es " + Nacionalidad)
print(f"{nombre} {apellidos} es {Nacionalidad}")
print( "Hola me llamo {} {} y mi nacionalidad es: {}".format(nombre, apellidos, Nacionalidad))
