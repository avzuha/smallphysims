import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(0, 4*np.pi, 200)
k = 1.0   
omega = 1.0  

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

line_E, = ax.plot([], [], [], 'r-', lw=2, label='E field')
line_B, = ax.plot([], [], [], 'b-', lw=2, label='B field')

ax.set_xlim(0, 4*np.pi)
ax.set_ylim(-1.5, 1.5)
ax.set_zlim(-1.5, 1.5)

ax.grid(False)
ax.xaxis.pane.set_alpha(0)
ax.yaxis.pane.set_alpha(0)
ax.zaxis.pane.set_alpha(0)
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

ax.plot([0, 4*np.pi], [0, 0], [0, 0], 'k-', lw=1) 
ax.plot([0, 0], [-1.5, 1.5], [0, 0], 'k-', lw=1)  
ax.plot([0, 0], [0, 0], [-1.5, 1.5], 'k-', lw=1)  

ax.text(4*np.pi, 0, 0, 'x (Propagation)', color='k')
ax.text(0, 1.5, 0, 'y (E field)', color='r')
ax.text(0, 0, 1.5, 'z (B field)', color='b')

ax.set_title("Electromagnetic Wave in 3D")

def init():
    line_E.set_data([], [])
    line_E.set_3d_properties([])
    line_B.set_data([], [])
    line_B.set_3d_properties([])
    return line_E, line_B

def animate(t):
    y_E = np.sin(k*x - omega*t)   
    z_B = np.sin(k*x - omega*t)   

    line_E.set_data(x, y_E)
    line_E.set_3d_properties(np.zeros_like(x))  

    line_B.set_data(x, np.zeros_like(x))
    line_B.set_3d_properties(z_B)  

    return line_E, line_B

ani = animation.FuncAnimation(fig, animate, frames=200,
                              init_func=init, interval=90, blit=True)

plt.show()
