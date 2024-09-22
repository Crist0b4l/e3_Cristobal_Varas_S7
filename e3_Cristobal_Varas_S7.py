# •	Desarrolla un programa que permita declara y poblar una matriz 3X3 con números enteros.
# •	Muestra la sumatoria de sus elementos.
# •	El resultado final debe ser 21.
# •	Realiza una captura del programa. 


import numpy as np

# Matriz predefinida

matriz =  np.array([[0,1,2], [3,0,4], [5,6,0]])

print("Matriz 3x3")
print(matriz)

suma = np.sum(matriz)

if suma == 21:
    print(f"La sumatoria de los elementos de la matriz es: {suma}")
else: 
    print("La sumatoria es distinta de 21")

# Matriz ingresada por el usuario

matrizUsuario =  np.zeros((3,3), dtype= int)

print("Introduce los valores para llenar la matriz de 3x3: ")

for i in range(3):
    for j in range(3):
        matrizUsuario[i][j] = int(input(f"Ingrese el valor para la posición [{i}][{j}]: "))

print("Matriz 3x3")
print(matrizUsuario)

suma = np.sum(matrizUsuario)

if suma == 21:
    print(f"La sumatoria de los elementos de la matriz es: {suma}")
else:
    print("La sumatoria es distinta de 21")