import tkinter as tk

# Crée une instance de la fenêtre principale
fenetre = tk.Tk()

# Configure le titre de la fenêtre
fenetre.title("Sudoku")

# Définit les dimensions de la fenêtre (largeur x hauteur)
fenetre.geometry("900x1200")

canvas = tk.Canvas(fenetre, width=900, height=1000)
canvas.pack()

def tracer_ligne(x1, y1, x2, y2):
    # Coordonnées de début et de fin de la ligne
    canvas.create_line(x1, y1, x2, y2, fill="gray", width=0.8)

def tracer_ligne_principal(x1, y1, x2, y2):
    canvas.create_line(x1, y1, x2, y2, fill="black", width=0.9)

def tracer_grillage_verticale():
    x = 0
    while x <= 900:
        if x % 300 == 0 or x == 0:
            tracer_ligne_principal(x, 0, x, 900)
        else:
            tracer_ligne(x, 0, x, 900)
        x += 100

def tracer_grillage_horizontal():
    y = 0
    indice_large = 0
    while y <= 900 :
        if indice_large % 3 == 0 :
            tracer_ligne_principal(0, y, 900, y)
        else:
            tracer_ligne(0, y, 900, y)
        y += 90
        indice_large += 1

tracer_grillage_verticale()
tracer_grillage_horizontal()
canvas.create_line(2, 2, 2, 900, fill="black", width=2)
canvas.create_line(2, 2, 900, 1, fill="black", width=2)
canvas.create_line(2, 792, 900, 792, fill="black", width=2)



fenetre.mainloop()

fenetre.mainloop()
