import numpy as np
import matplotlib.pyplot as plt

# Ejercicio 1: Cálculo de Distancia (Nivel Básico)
# Un tren de carga viaja en línea recta manteniendo una velocidad constante de 85 km/h. ¿Qué distancia exacta, expresada en kilómetros, habrá recorrido después de 3 horas de viaje continuo?
# Datos:
# v = 85,
# t = 3

t = np.linspace(0, 3, 100) # Tiempo desde 0 hasta 3 horas
v = 85
d = v*t
posicion = v * t

plt.plot(t, posicion, color = "blue", linewidth = 2) # linediwth es

plt.title("Simulacion de Posicion")
plt.xlabel("tiempo (Horas)")
plt.ylabel("Posicion (Kilometros)")
plt.grid(True)
plt.show()

print(f"La distancia recorrida es de: {d[-1]}") # accede al ultimo elemento del arreglo que almacena la distancia total


