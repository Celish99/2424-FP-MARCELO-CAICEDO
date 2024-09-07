import numpy as np

# Definir las ciudades
ciudades = ["Ciudad A", "Ciudad B", "Ciudad C"]

# Definir las semanas
semanas = ["Semana 1", "Semana 2"]

# Definir los días de la semana
días = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]

# Mapa de nombres de días a temperaturas (por ejemplo)
temperaturas_dia = {
    "lunes": 18,
    "martes": 20,
    "miércoles": 22,
    "jueves": 24,
    "viernes": 26,
    "sábado": 28,
    "domingo": 30
}

# Definir las horas por día (esto no cambia, pero es para la estructura)
horas_por_día = 24

# Crear una matriz 4D con forma (n_ciudades, n_semanas, n_días, n_temperaturas_diarias)
# Cada celda es un array de 24 temperaturas diarias con nombres de días
temperaturas = np.array([
    # Ciudad A
    [
        # Semana 1
        [
            np.full(horas_por_día, temperaturas_dia["lunes"]),  # Lunes
            np.full(horas_por_día, temperaturas_dia["martes"]),  # Martes
            np.full(horas_por_día, temperaturas_dia["miércoles"]),  # Miércoles
            np.full(horas_por_día, temperaturas_dia["jueves"]),  # Jueves
            np.full(horas_por_día, temperaturas_dia["viernes"]),  # Viernes
            np.full(horas_por_día, temperaturas_dia["sábado"]),  # Sábado
            np.full(horas_por_día, temperaturas_dia["domingo"])  # Domingo
        ],
        # Semana 2
        [
            np.full(horas_por_día, temperaturas_dia["lunes"]),  # Lunes
            np.full(horas_por_día, temperaturas_dia["martes"]),  # Martes
            np.full(horas_por_día, temperaturas_dia["miércoles"]),  # Miércoles
            np.full(horas_por_día, temperaturas_dia["jueves"]),  # Jueves
            np.full(horas_por_día, temperaturas_dia["viernes"]),  # Viernes
            np.full(horas_por_día, temperaturas_dia["sábado"]),  # Sábado
            np.full(horas_por_día, temperaturas_dia["domingo"])  # Domingo
        ]
    ],
    # Ciudad B
    [
        # Semana 1
        [
            np.full(horas_por_día, temperaturas_dia["lunes"]),  # Lunes
            np.full(horas_por_día, temperaturas_dia["martes"]),  # Martes
            np.full(horas_por_día, temperaturas_dia["miércoles"]),  # Miércoles
            np.full(horas_por_día, temperaturas_dia["jueves"]),  # Jueves
            np.full(horas_por_día, temperaturas_dia["viernes"]),  # Viernes
            np.full(horas_por_día, temperaturas_dia["sábado"]),  # Sábado
            np.full(horas_por_día, temperaturas_dia["domingo"])  # Domingo
        ],
        # Semana 2
        [
            np.full(horas_por_día, temperaturas_dia["lunes"]),  # Lunes
            np.full(horas_por_día, temperaturas_dia["martes"]),  # Martes
            np.full(horas_por_día, temperaturas_dia["miércoles"]),  # Miércoles
            np.full(horas_por_día, temperaturas_dia["jueves"]),  # Jueves
            np.full(horas_por_día, temperaturas_dia["viernes"]),  # Viernes
            np.full(horas_por_día, temperaturas_dia["sábado"]),  # Sábado
            np.full(horas_por_día, temperaturas_dia["domingo"])  # Domingo
        ]
    ],
    # Ciudad C
    [
        # Semana 1
        [
            np.full(horas_por_día, temperaturas_dia["lunes"]),  # Lunes
            np.full(horas_por_día, temperaturas_dia["martes"]),  # Martes
            np.full(horas_por_día, temperaturas_dia["miércoles"]),  # Miércoles
            np.full(horas_por_día, temperaturas_dia["jueves"]),  # Jueves
            np.full(horas_por_día, temperaturas_dia["viernes"]),  # Viernes
            np.full(horas_por_día, temperaturas_dia["sábado"]),  # Sábado
            np.full(horas_por_día, temperaturas_dia["domingo"])  # Domingo
        ],
        # Semana 2
        [
            np.full(horas_por_día, temperaturas_dia["lunes"]),  # Lunes
            np.full(horas_por_día, temperaturas_dia["martes"]),  # Martes
            np.full(horas_por_día, temperaturas_dia["miércoles"]),  # Miércoles
            np.full(horas_por_día, temperaturas_dia["jueves"]),  # Jueves
            np.full(horas_por_día, temperaturas_dia["viernes"]),  # Viernes
            np.full(horas_por_día, temperaturas_dia["sábado"]),  # Sábado
            np.full(horas_por_día, temperaturas_dia["domingo"])  # Domingo
        ]
    ]
])

# Calcular el promedio de temperaturas para cada ciudad y semana
for i, ciudad in enumerate(ciudades):
    for k, semana in enumerate(semanas):
        suma_temperaturas = 0
        conteo_temperaturas = 0

        for j in range(len(días)):
            # Acceder al array de temperaturas diarias para el día j de la semana k de la ciudad i
            temperaturas_dia = temperaturas[i, k, j]
            # Sumar las temperaturas del día
            suma_temperaturas += np.sum(temperaturas_dia)
            conteo_temperaturas += len(temperaturas_dia)

        # Calcular el promedio para la ciudad i en la semana k
        promedio_semanal = suma_temperaturas / conteo_temperaturas
        print(f"Promedio semanal de temperaturas para {ciudad} en {semana}: {promedio_semanal:.2f} °C")
