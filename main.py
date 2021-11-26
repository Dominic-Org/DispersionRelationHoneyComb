import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
from numpy import sqrt
from numpy import pi
from numpy import cos
from mpl_toolkits.mplot3d import axes3d
J = 1
a = 1


kx, ky = np.meshgrid(np.arange(-pi, pi, 0.01 * pi), np.arange(-pi, pi, 0.01 * pi))
dispersion = 4 * sqrt(
    3 + cos(sqrt(3) * ky * a) + 4 * cos(sqrt(3) * ky * a / 2) * cos(3 * kx * a / 2)
)
dispersion2 = 4 * -sqrt(
    3 + cos(sqrt(3) * ky * a) + 4 * cos(sqrt(3) * ky * a / 2) * cos(3 * kx * a / 2)
)

levels = np.linspace(dispersion.min(), dispersion.max(), 20)
levels2 = np.linspace(dispersion2.min(), dispersion2.max(), 20)

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

ax.xaxis.set_major_formatter(tck.FormatStrFormatter("%g $\pi$"))
ax.xaxis.set_major_locator(tck.MultipleLocator(base=2))
ax.yaxis.set_major_formatter(tck.FormatStrFormatter("%g $\pi$"))
ax.yaxis.set_major_locator(tck.MultipleLocator(base=2))

plt.xlim(-1, 1)
plt.ylim(-1, 1)

X = kx / pi
Y = ky / pi

# ax.contourf(kx/pi, ky/pi, dispersion, levels = levels, normalize = True)
# ax.plot_wireframe(X, Y, dispersion, rstride=10, cstride=10, linewidth=0.5)
ax.plot_surface(X, Y, dispersion, rstride=5, cstride=5, cmap="gnuplot", edgecolor='none', color="black")
ax.plot_surface(X, Y, dispersion2, rstride=5, cstride=5, cmap="gnuplot", edgecolor='none', color="black")
ax.view_init(8, 80)

plt.show()
