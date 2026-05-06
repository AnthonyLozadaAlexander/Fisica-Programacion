import numpy as np
import matplotlib.pyplot as plt

# Creamos el tiempo de nuestra simulacion
# 100 fps espaciados uniformemente entre 0 y 10 segundos
t = np.linspace(0, 10, 100)

posicion_inicial = 0
velocidad_inicial = 0
aceleracion = 2