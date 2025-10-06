# Disegnare il poligono in base al numero di lati inseriti

# Importo libreria turtle

import turtle

def disegnaFigura(nLati):
    
    sommaAngoli = (nLati-2)*180
    
    for i in range(nLati):
        t.forward(50)
        t.left(180-(sommaAngoli/nLati))
    
# Ricevere in input il numero dei lati del poligono

print("Inserire il numero dei lati del poligono")
nLati = int(input())
     
# Creazione della finestra

screen = turtle.Screen()



    

# Creazione della tartaruga

t = turtle.Turtle()
t.shape("turtle")
t.speed(1)

# Sollevo la penna per non far scrivere la tartaruga mentre la sposto
t.penup()

# Sposto la tartaruga
t.goto(-100,-250)

# Abbasso la penna cosi la tartaruga puo tracciare il percorso

t.pendown()


# Chiamata del metodo che disegna

disegnaFigura(nLati)

# Mantiene la finestra aperta fino al click
turtle.done

