import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
from numpy import sqrt
from numpy import pi 
from numpy import cos 

J = 1
a = 1


kx,ky = np.meshgrid(np.arange(-pi, pi, 0.01*pi), np.arange(-pi, pi, 0.01*pi))
dispersion = 4*sqrt(3 + cos(sqrt(3)*ky*a) + 4*cos(sqrt(3)*ky*a/2)*cos(3*kx*a/2))
dispersion2 = 4*-sqrt(3 + cos(sqrt(3)*ky*a) + 4*cos(sqrt(3)*ky*a/2)*cos(3*kx*a/2))

levels = np.linspace(dispersion.min(), dispersion.max(), 20)
levels2 = np.linspace(dispersion2.min(), dispersion2.max(), 20)


f,ax=plt.subplots(figsize=(20,10))
ax = plt.axes(projection='3d')

ax.xaxis.set_major_formatter(tck.FormatStrFormatter('%g $\pi$'))
ax.xaxis.set_major_locator(tck.MultipleLocator(base=2))
ax.yaxis.set_major_formatter(tck.FormatStrFormatter('%g $\pi$'))
ax.yaxis.set_major_locator(tck.MultipleLocator(base=2))


ax.plot_surface(kx/pi, ky/pi, dispersion, rstride=5, cstride=5, cmap="gnuplot", edgecolor='black', linewidth = 0.5)
ax.plot_surface(kx/pi, ky/pi, dispersion2, rstride=5, cstride=5, cmap="gnuplot_r", edgecolor='black', linewidth = 0.5)
ax.view_init(8, 80)

plt.xlim(-1,1)
plt.ylim(-1,1)

plt.xlabel(r'$k_x (\frac{\pi}{a})$')
plt.ylabel(r'$k_y (\frac{\pi}{a})$')

plt.show()
