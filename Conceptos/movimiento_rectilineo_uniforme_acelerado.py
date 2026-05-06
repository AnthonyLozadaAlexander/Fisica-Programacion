import numpy as np
import matplotlib.pyplot as plt

# Creamos el tiempo de nuestra simulacion
# 100 fps espaciados uniformemente entre 0 y 10 segundos
t = np.linspace(0, 10, 100)

posicion_inicial = 0
velocidad_inicial = 0
aceleracion = 2

posicion = posicion_inicial + (velocidad_inicial * t) + 1/2 * (aceleracion*(1**2))

plt.plot(t, color = "red", linewidth = 2)
plt.tittle("Simulacion MRUA: Aumento VVelerado")
plt.xlabel = "tiempo y segundos)")
plt.ylabel = "Posicion (Metros)")
plt.grid(Tr