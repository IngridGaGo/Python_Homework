
# Suma
def suma():
    a = 5
    b = 7
    resultado = a + b
    print("Suma: ", resultado) 
suma()    


# Calcular promedio
def promedio(lista):
    suma = 0
    for numero in lista:
        suma += numero
    promedio = suma / len(lista)
    return promedio

resultado_promedio = promedio([2, 4, 6, 8])
print("Promedio: ", resultado_promedio) 


# Nombre completo
def generar_nombre_completo (nombre, apellido):
    espacio = ' '
    nombre_completo = nombre + espacio + apellido
    return nombre_completo
print('Nombre completo: ', generar_nombre_completo('Ingrid','Garay'))


# Numeros iguales
def encuentra_numeros_pares(n):
    pares = []
    for i in range(n + 1):
        if i % 2 == 0:
            pares.append(i)
    return pares
print("Numeros pares: ", encuentra_numeros_pares(10))

# Calcular edad
def calcular_edad (año_nacimiento,año_actual = 2023):
    edad = año_actual - año_nacimiento
    return edad
print('Edad: ', calcular_edad(1996))
