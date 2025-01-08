
# Opción 1: Mostrar fórmulas con Matplotlib en Tkinter
# Puedes integrar un gráfico de Matplotlib (que soporta LaTeX) dentro de una ventana de Tkinter usando FigureCanvasTkAgg.

# Código de ejemplo:
# Explicación:

# Figure de Matplotlib crea un espacio donde se dibuja la fórmula.
# FigureCanvasTkAgg inserta la figura en la ventana de Tkinter.
# La fórmula se representa en LaTeX usando r'$...$'.
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Crear la ventana principal de Tkinter
root = tk.Tk()
root.title("Fórmula Matemática en Tkinter")

# Crear una figura con Matplotlib
fig = Figure(figsize=(2, 1), dpi=100)
ax = fig.add_subplot(111)
#ax.text(0.1, 0.5, r'$f(x) = 100 \cdot e^{0.05 \cdot x}$', fontsize=20)
ax.text(0.1, 0.5, r'$f(x) = 100 \cdot e^{0.05 \cdot x}$')
ax.axis('off')  # Quitar los ejes porque se grafica de manera literal

# Insertar la figura en Tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack()

# Mostrar la ventana
root.mainloop()


