import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import cm

nx = 100
ny = 100
nt = 1000

L = 10 #metres
c = 500 #metres per second
Tmax = 1 #seconds

x = np.linspace(0, L, nx)
y = np.linspace(0, L, ny)

dx = L/nx
dy = L/ny
dt = Tmax/nt

u_old = np.zeros([nx, ny])
u_now = np.zeros([nx, ny])
u_future = np.zeros([nx, ny])

#input initial conditions
u_old[int(nx/2),int(ny/2)] = 0.6

def display(output):
    fig, ax = plt.subplots(subplot_kw = {"projection":"3d"})
    a, b = np.meshgrid(x, y)
    ax.set_zlim(-0.5, 0.5)
    surf = ax.plot_surface(a, b, output, cmap = cm.viridis, linewidth = 0, antialiased = False)


for i in range(nt):
    u_future[1:nx-1, 1:ny-1] = (
            2*u_now[1:nx-1, 1:ny-1] - u_old[1:nx-1, 1:ny-1]
            + c*(dt**2)*(
                (u_now[2:nx, 1:ny-1] + u_now[0:nx-2, 1:ny-1] - 2*u_now[1:nx-1, 1:ny-1])/(dx**2) +
                (u_now[1:nx-1, 2:ny] + u_now[1:ny-1, 0:ny-2] - 2*u_now[1:nx-1, 1:ny-1])/(dy**2)
                )
            )
    u_old = u_now
    u_now = u_future

display(u_future)
