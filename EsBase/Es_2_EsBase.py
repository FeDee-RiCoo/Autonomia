# Realizzare un conto alla rovescia accettando in ingresso il valore iniziale
#  (intero e positivo) e una funzione di attesa della libreria time.

# Importo la libreria time

import time

# Metodo che controlla se il numero inserito è positivo
def  controlloNumero(n):
    if n < 0:
        return False
    return True

# Inizio del programma


while True:
    
    print("Inserire valore di partenza del countdown")
    n = int(input())
    if controlloNumero(n) == True:
        break
    
while n > 0:
    
    print(n)  
    time.sleep(1)  
    n -= 1
    
print("Countdown finito!")
    

    




