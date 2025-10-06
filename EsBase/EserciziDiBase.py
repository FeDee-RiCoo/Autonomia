# Calcolare la divisione intera accettando come parametri dividendo e divisore
# utilizzando solo somme e sottrazioni. Il risultato deve essere una tupla con quoziente intero e resto

def QuozienteConResto (dividendo, divisore):
    if divisore == 0:
        return (None, None)
    # if divisore > dividendo:
    #    return (0, dividendo)
    quoziente = 0
    carrello = divisore
    while carrello <= dividendo:
        carrello = carrello + divisore
        quoziente += 1 # quoziente = quoziente + 1
        # print(f"quoziente: {quoziente}, carrello: {carrello}")
   
    resto = dividendo - (carrello - divisore)
    # print(f"quoziente: {quoziente}, resto: {resto}")
    return (quoziente, resto)


(q, r) = QuozienteConResto(31, 17)
print(f"quoziente: {q}, resto: {r}")