import numpy as np
import matplotlib.pyplot as plt

# Un satélite en el vacío del espacio se desplaza a una velocidad constante de 3000 m/s. Necesita recorrer una distancia total de 12000 km para alcanzar su órbita final.
# ¿Cuántos segundos tardará en completar este trayecto?
# Nota analítica: Las unidades deben ser consistentes.
# Debemos convertir los kilómetros a metros antes de operar.
# Datos: v = 3000m/s d = 12000km = 12000000m

v = 3000 #m/s
d = 12000 #km
d = (12000)*(1000) # conversion km a m

print(f"Distancia Satelite: {d} metros")
t = (d)/(v)
print(f"Tiempo Total: {t} Segundos")

tEje = np.linspace(0, t, 100) # arreglo para el tiempo
posicion = d*tEje # la distancia se  multiplicara por cada indice del arreglo del tiempo de 4000s

plt.plot(tEje, posicion, color = "Red",linewidth = 2)

plt.title("Distancia de Satelite")
plt.xlabel("Tiempo (Segundos)")
plt.ylabel("Distancia (Metros)")
plt.grid(True)
plt.show()


