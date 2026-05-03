import numpy as np # libreria para generar listas y arrays
import matplotlib.pyplot as plt # dibujar graficar y visualizar datos

t = np.linspace(0, 10, 100)
velocidad = 5
posicion = velocidad * t

plt.plot(t, posicion, color = 'blue', linewidth = 2)
plt.title("Primera Simulacion: Movimiento Constante")
plt.xlabel("tiempo (segundos") # eje x = Tiempo
plt.ylabel("Posicion (Metros)") # eje y = Posicion
plt.grid(True)
plt.show()
