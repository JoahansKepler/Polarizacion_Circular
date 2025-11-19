import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# Parámetros de la onda
amplitud_x = 1
amplitud_y = 0
frecuencia_x = 1
frecuencia_y = 1
omega_x = 2 * np.pi * frecuencia_x  # frecuencia angular
omega_y = 2 * np.pi * frecuencia_y  # frecuencia angular
fase = 3 * np.pi / 4
m=-1
duracion = 8
fps = 30

# tiempo
t = np.linspace(0, duracion, duracion * fps)

# ondas en x y y
x = amplitud_x * np.sin(omega_x * t + fase*m)
y = amplitud_y * np.sin(omega_y * t)

# configuración de la figura
fig, ax = plt.subplots()
fig.patch.set_facecolor('white')

# ejes
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
ax.grid(True)
ax.set_xlabel('Campo eléctrico x')
ax.set_ylabel('Campo eléctrico y')
ax.set_title('Polarización circular de la luz')

# grind
ax.axhline(0, color='gray', lw=0.5)
ax.axvline(0, color='gray', lw=0.5)
ax.plot(0, 0, 'ko')  # punto en el origen

# elementos
punto, = ax.plot([], [], 'bo', markersize=8)  # punto azul
vector, = ax.plot([], [], color='red', lw=2)  # vector rojo
trayectoria, = ax.plot([], [], 'g--', lw=1)  # línea verde punteada

# trayectoria
x_hist, y_hist = [], []

# animación
def update(frame):
    x_hist.append(x[frame])
    y_hist.append(y[frame])
    punto.set_data([x[frame]], [y[frame]])
    vector.set_data([0, x[frame]], [0, y[frame]])
    trayectoria.set_data(x_hist, y_hist)
    return punto, vector, trayectoria


anim = FuncAnimation(fig, update, frames=len(t), interval=1000/fps, blit=True)

# GIF
anim.save('polarizacion_circular.gif', writer=PillowWriter(fps=fps))