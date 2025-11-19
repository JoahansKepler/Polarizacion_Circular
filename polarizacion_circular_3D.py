import numpy as np  
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
import math
#### Aqui empieza lo mero bueno matematico y fisico
# Parámetros de la onda
k = 10 # Numero de onda
Amplitud_x = 1
Amplitud_y = 1
omega_x= 1
omega_y= 1
fase_x = 1
fase_y = 1
desfase = 3*math.pi/4
t = np.linspace(0, 6 * np.pi, 400)  # Tiempo

# Ecuaciones paramétricas de la onda
x = Amplitud_x * np.cos(omega_x * k - fase_x * t)
y = Amplitud_y * np.cos(omega_y * k - fase_y * t - desfase)
z = t          # propagación


################# A partir de aqui todo esto es para la grafica###########
# Configuración de la figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

line, = ax.plot([], [], [], linewidth=2)

# Límites y etiquetas
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.set_zlim(0, 30)
ax.set_xlabel("Campo electrico en X")
ax.set_ylabel("Campo electrico en Y")
ax.set_zlabel("Propagación (z)")
ax.set_title("Polarización con angulo de desfase = 3pi/4")


def update(frame):
    line.set_data(x[:frame], y[:frame])
    line.set_3d_properties(z[:frame])
    return line,

ani = FuncAnimation(fig, update, frames=len(t), interval=30, blit=True)

plt.show()

