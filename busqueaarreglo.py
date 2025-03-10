#Matriz bidimensional
matriz = [
    [14, 8, 22],
    [42, 15, 6],
    [9, 31, 26]
]
def buscar_en_matriz(matriz, valor_buscar):
    # Recorrer la matriz para buscar el valor
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor_buscar:
                return True, (i, j)
    return None
#Valor a buscar
valor_buscar = 15
# Imprimir matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)
#Resultados
resultado, posicion = buscar_en_matriz(matriz, valor_buscar)

if resultado:
    print(f"El valor {valor_buscar} se encontró en la posición{posicion}.")
else:
    print(f"El valor {valor_buscar} no se encontró en la matriz")
