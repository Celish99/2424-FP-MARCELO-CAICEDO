# Definición de la matriz 3x3 con valores numéricos
matriz = [
    [5, 2, 9],
    [1, 4, 6],
    [8, 3, 7]
]

# Función para imprimir la matriz
def imprimir_matriz(matriz):
    for fila in matriz:
        print(" ".join(map(str, fila)))

# Función de Bubble Sort para ordenar una fila
def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        # Últimos i elementos ya están ordenados
        for j in range(0, n-i-1):
            if fila[j] > fila[j+1]:
                # Intercambiar si el elemento encontrado es mayor que el siguiente
                fila[j], fila[j+1] = fila[j+1], fila[j]

# Función para ordenar una fila específica de la matriz
def ordenar_fila(matriz, fila_index):
    if 0 <= fila_index < len(matriz):
        fila = matriz[fila_index]
        bubble_sort(fila)
    else:
        print(f"Índice de fila {fila_index} fuera de rango.")

# Definir el índice de la fila a ordenar
indice_fila_a_ordenar = 1

# Mostrar la matriz original
print("Matriz original:")
imprimir_matriz(matriz)

# Ordenar la fila específica
ordenar_fila(matriz, indice_fila_a_ordenar)

# Mostrar la matriz con la fila ordenada
print(f"\nMatriz con la fila {indice_fila_a_ordenar} ordenada:")
imprimir_matriz(matriz)
