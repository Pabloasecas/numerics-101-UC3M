import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import PchipInterpolator

y=[2,1,0,1,0,0,-1,-2,-3,-7,-5,-3,-2,0,0,1,0.5,0.5,3]
x= np.arange(0, 361, 20)

x = np.array(x)
y = np.array(y)

x_smooth = np.linspace(x.min(), x.max(), 300)
interp = PchipInterpolator(x, y)
y_smooth = interp(x_smooth)

fig, ax = plt.subplots(figsize=(10, 4.5))
ax.set_xticks(np.arange(0, 361, 20))

plt.xlabel("Rotation angle " r"$\phi$ (°)")
plt.ylabel("Vertical displacement " r"$\Delta y$ (mm)" )

plt.plot(x, y, "o", label="Datos originales")
plt.plot(x_smooth, y_smooth, "-", label="Curva suavizada")
plt.grid(True)
plt.show()

plt.rcParams.update({
    "figure.dpi": 120,
    "savefig.dpi": 300,
    "font.family": "serif",
    "mathtext.fontset": "dejavuserif",
})


fig.savefig("diagrama_desplazamiento_leva_seguidor_plano.svg", bbox_inches="tight")
plt.show()