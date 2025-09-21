import numpy as np
import matplotlib.pyplot as plt

# -------------------------
# Parámetros de la leva
# -------------------------
L = 1.0                   # Levantamiento total
beta = np.pi              # Duración de la subida en rad (β). Cambia a lo que necesites.

# Dominio de la subida: 0..β
theta = np.linspace(0, beta, 100)

# -------------------------
# Movimiento armónico simple (subida)
# y(θ) = L/2 * (1 - cos(πθ/β))
# Derivadas respecto a θ (no respecto al tiempo):
# y'(θ)  = (πL)/(2β) * sin(πθ/β)
# y''(θ) = (π^2 L)/(2β^2) * cos(πθ/β)
# y'''(θ)= -(π^3 L)/(2β^3) * sin(πθ/β)
# Nota: si quieres velocidad/aceleración en el tiempo, multiplica por ω, ω^2, ω^3.
# -------------------------
u = np.pi * theta / beta
y   = 0.5*L*(1 - np.cos(u))
y1  = 0.75*np.pi*L/beta * np.sin(u)
y2  = 0.5*(np.pi**2)*L/(beta**2) * np.cos(u)
y3  = -0.25*(np.pi**3)*L/(beta**3) * np.sin(u)


# Eje x en fracción de β (θ/β) para que vaya de 0 a 1
xb = theta / beta

# -------------------------
# Plot
# -------------------------
plt.rcParams.update({
    "figure.dpi": 120,
    "savefig.dpi": 300,
    "font.family": "serif",
    "mathtext.fontset": "dejavuserif",
})

fig, ax = plt.subplots(figsize=(10, 4.5))

# Curvas (no forzamos colores)
ax.plot(xb, y,  label=r"$y$")
ax.plot(xb, y1, label=r"$y'$")
ax.plot(xb, y2, label=r"$y''$")
ax.plot(xb, y3, label=r"$y'''$")

# Rejilla y leyenda
ax.grid(True, alpha=0.3)
ax.legend(loc="best")

# Ticks cada 0.1 en x (0..1)
ax.set_xticks([0, 0.5, 1.0])
ax.tick_params(axis='y', which='both', left=False, right=False, labelleft=False)
ax.set_xticklabels(["0", "0,5", "1"])

# Quitar bordes superior y derecho
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["left"].set_visible(False)


# Flechas en los ejes
ax.annotate("", xy=(1.02, 0), xycoords=("axes fraction","data"),
            xytext=(0, 0),   textcoords=("axes fraction","data"),
            arrowprops=dict(arrowstyle="->", lw=1.4))
ax.annotate("", xy=(0, 1.02), xycoords=("data","axes fraction"),
            xytext=(0, 0),   textcoords=("data","axes fraction"),
            arrowprops=dict(arrowstyle="-", lw=1.4))

# Nombre del eje x al final (θ/β)
# Derecha + media altura (horizontal)
ax.text(1.02, 0.35, r"$\theta/\beta$", transform=ax.transAxes, ha="left", va="center")

fig.tight_layout()
plt.show()
fig.tight_layout()
fig.savefig("diagrama_desplazamiento.png", dpi=300, bbox_inches="tight")