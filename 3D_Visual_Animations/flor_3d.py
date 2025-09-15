import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib import animation
import shutil  # Para verificar si ffmpeg está disponible


# ==============================
# FUNCIONES AUXILIARES
# ==============================
def generar_flor(n=800, petal_num=5):
    """Genera las coordenadas X, Y, Z de la flor 3D."""
    # Radio y ángulo
    r = np.linspace(0, 1, n)
    theta = np.linspace(0, 2*np.pi, n)
    R, THETA = np.meshgrid(r, theta, indexing='ij')

    # Cálculo para pétalos
    tmp = petal_num * THETA
    x = 1 - 0.5 * ((1.25 * (1 - (tmp % (2*np.pi)) / np.pi))**2 - 0.25)**2

    # Ángulo phi
    phi = (np.pi / 2) * np.exp(-0.25)

    # Coordenada auxiliar
    y = 1.95653 * (R**2) * (1.27689*R - 1)**2 * np.sin(phi)

    # Radio modificado
    R2 = x * (R*np.sin(phi) + y*np.cos(phi))

    # Coordenadas cartesianas
    X = R2 * np.sin(THETA)
    Y = R2 * np.cos(THETA)
    Z = x * (R*np.cos(phi) - y*np.sin(phi))

    return X, Y, Z


def crear_colormap():
    """Crea un mapa de colores degradado (violeta + dorado)."""
    map_size = 20
    blue_map = np.array([
        np.linspace(138, 75, map_size),
        np.linspace(43, 0, map_size),
        np.linspace(226, 130, map_size)
    ]).T

    gold_map = np.array([[255, 215, 0], [250, 210, 0]])
    violet_map = np.concatenate((gold_map, blue_map))
    return ListedColormap(violet_map / 255)


def animar(i, ax, fig):
    """Función que actualiza la animación de la flor."""
    if i <= 180:
        elev = 15.6 + 0.28 * i  # sube de 0° a 180°
    else:
        elev = 66 - 0.28 * (i - 180)  # baja de 180° a 360°
    ax.view_init(elev=elev, azim=i)
    return fig,


# ==============================
# FUNCIÓN PRINCIPAL
# ==============================
def main():
    # Generar flor
    X, Y, Z = generar_flor(n=800, petal_num=5)

    # Crear figura
    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(111, projection="3d")

    # Fondo negro y quitar paneles
    ax.set_facecolor("black")
    for axis in [ax.xaxis, ax.yaxis, ax.zaxis]:
        axis.pane.fill = False

    # Ángulo inicial
    ax.view_init(azim=-12, elev=66)

    # Graficar superficie
    colormap = crear_colormap()
    ax.plot_surface(X, Y, Z, cmap=colormap, linewidth=0, antialiased=False)

    # Animación
    anim = animation.FuncAnimation(
        fig,
        animar,
        frames=360,
        fargs=(ax, fig),
        interval=20,
        blit=True
    )

    # ==============================
    # Exportación (MP4 o GIF según disponibilidad)
    # ==============================
    if shutil.which("ffmpeg"):
        print("🎥 FFmpeg encontrado → Guardando en MP4...")
        from matplotlib.animation import FFMpegWriter
        writer = FFMpegWriter(fps=30, codec="libx264")
        anim.save("3D_purple_flower.mp4", writer=writer)
        print("✅ Animación guardada en '3D_purple_flower.mp4'")
    else:
        print("⚠️ FFmpeg no encontrado → Guardando en GIF con Pillow...")
        from matplotlib.animation import PillowWriter
        writer = PillowWriter(fps=20)
        anim.save("3D_purple_flower.gif", writer=writer)
        print("✅ Animación guardada en '3D_purple_flower.gif'")

    # Mostrar preview estática
    plt.show()


# ==============================
# EJECUCIÓN DEL SCRIPT
# ==============================
if __name__ == "__main__":
    main()
