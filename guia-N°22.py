mochila = ["botella de agua", "comida en lata", "libro de entrenamiento","droga"]

def usar_la_fuerza(mochila, indice, num_objetos= -1, sable_encontrado=False ):
    if indice <= len(mochila):
        if not sable_encontrado:
            num_objetos += 1
            if mochila[indice] == "sable de luz":
                sable_encontrado = True
        usar_la_fuerza(mochila, indice + 1, num_objetos, sable_encontrado)
    else:
        if sable_encontrado == True:
            print(f"Se encontró un sable de luz después de revisar {str(num_objetos)} objetos.")
        else:
            print(f"No se encontró un sable de luz después de revisar {str(num_objetos)} objetos.")
        



usar_la_fuerza(mochila, 0)

print("PD: que buena saga la star wars")