
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 4

#Matriz 3D
temperaturas = [
    [  #Quito
        [25, 26, 24, 23, 22, 21, 20],  # Semana 1
        [24, 25, 23, 22, 21, 20, 19],  # Semana 2
        [23, 24, 22, 21, 20, 19, 18],  # Semana 3
        [22, 23, 21, 20, 19, 18, 17]   # Semana 4
    ],
    [  # Ibarra
        [30, 31, 32, 33, 34, 35, 36],  # Semana 1
        [29, 30, 31, 32, 33, 34, 35],  # Semana 2
        [28, 29, 30, 31, 32, 33, 34],  # Semana 3
        [27, 28, 29, 30, 31, 32, 33]   # Semana 4
    ],
    [  # Túlcan
        [20, 21, 22, 23, 24, 25, 26],  # Semana 1
        [19, 20, 21, 22, 23, 24, 25],  # Semana 2
        [18, 19, 20, 21, 22, 23, 24],  # Semana 3
        [17, 18, 19, 20, 21, 22, 23]   # Semana 4
    ]
]

# Calcular el promedio de temperaturas para cada ciudad y semana
ciudades = ["Quito", "Ibarra", "Túlcan"]
for i, ciudad in enumerate(ciudades):
    print(f"Promedios de temperatura para {ciudad}:")
    for semana in range(semanas):
        suma_temperaturas = sum(temperaturas[i][semana])
        promedio = suma_temperaturas / len(dias_semana)
        print(f"  Semana {semana + 1}: {promedio:.2f}°C")
