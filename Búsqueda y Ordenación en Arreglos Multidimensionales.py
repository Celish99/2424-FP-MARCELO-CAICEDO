# Crear una matriz bidimensional (3x3) para el ejemplo
# Definición de la matriz 3x3 con valores numéricos
matriz = [
    [3, 5, 9],
    [2, 8, 7],
    [4, 1, 6]
]

# Función para imprimir la matriz
def imprimir_matriz(matriz):
    for fila in matriz:
        print(" ".join(map(str, fila)))

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor_buscado):
    for i, fila in enumerate(matriz):
        if valor_buscado in fila:
            # Si el valor se encuentra en la fila, obtenemos la columna
            j = fila.index(valor_buscado)
            return (i, j)  # Devolvemos las coordenadas (fila, columna)
    return None  # Si no se encuentra el valor, devolvemos None

# Definir el valor a buscar
valor_a_buscar = 1

# Imprimir la matriz
print("Matriz:")
imprimir_matriz(matriz)

# Buscar el valor en la matriz
coordenadas = buscar_valor(matriz, valor_a_buscar)

# Mostrar el resultado de la búsqueda
if coordenadas:
    print(f"\nEl valor {valor_a_buscar} se encuentra en la posición (fila, columna): {coordenadas}")
else:
    print(f"\nEl valor {valor_a_buscar} no se encuentra en la matriz.")
