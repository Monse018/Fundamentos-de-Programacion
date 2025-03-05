# Matriz Bidimencional
matriz = [
        [5, 12, 7],
        [9, 3, 8],
        [2, 11, 4]
    ]

def ordenar_fila(matriz, fila):
    # Ordenar la fila específica usando Bubble Sort
    n = len(matriz[fila])
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if matriz[fila][j] > matriz[fila][j + 1]:
                # Intercambiar elementos
                matriz[fila][j], matriz[fila][j + 1] = matriz[fila][j + 1], matriz[fila][j]

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
        print(fila)

    # Fila a ordenar
fila_a_ordenar = 1

# Ordenar la fila específica
ordenar_fila(matriz, fila_a_ordenar)

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz:
        print(fila)
