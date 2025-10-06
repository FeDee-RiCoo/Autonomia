# Disegnare un triangolo equilatero con la libreria turtle

# Importo libreria turtle

import turtle

# Imposta la finestra di disegno

screen = turtle.Screen()

# Creazione della tartaurga

t = turtle.Turtle()
t.shape("turtle")
t.speed(1)

# Disegna un triangolo equilatero

for i in range(3):

    t.forward(300)
    t.left(120)
    
turtle.done