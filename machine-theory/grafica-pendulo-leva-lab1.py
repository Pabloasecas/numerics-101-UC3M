import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import PchipInterpolator

y=[0,1,3,4,3.5,4.5,4.5,5.5,5.5,6,6.5,7,6.5,7,6.5,6,4.5,4.5,4,3.5,4,3,2.5,2,0]
x=[0,20,30,40,60,80,100,120,140,160,170,180,190,200,220,240,260,280,300,320,330,335,340,350,360]

x = np.array(x)
y = np.array(y)

x_smooth = np.linspace(x.min(), x.max(), 300)
interp = PchipInterpolator(x, y)
y_smooth = interp(x_smooth)

fig, ax = plt.subplots(figsize=(10, 4.5))
ax.set_xticks(np.arange(0, 361, 20))

plt.xlabel("Rotation angle " r"$\phi$ (°)")
plt.ylabel("Pressure angle " r"$\alpha_p$" )
plt.title("Oscillating follower displacement diagram")

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


fig.savefig("diagrama_desplazamiento_leva_oscilante.svg", bbox_inches="tight")
plt.show()