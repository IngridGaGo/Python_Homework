import re

frase = "Tengo 2 hijos que tienen 15 y 11 años"
patron = '[0-9]+' #Esta es una expresión regular
nuevo= re.findall(patron, frase)

print(nuevo)
print(type(nuevo))

