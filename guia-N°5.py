#Desarrollar una función que permita convertir un número romano en un número decimal.


def convertir(num_romano):
    Numeros_romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50}
    
    if not num_romano:
        return 0
    
    valor = Numeros_romanos[num_romano[0]]
    
    if len(num_romano) > 1:
        valor_siguiente = Numeros_romanos[num_romano[1]]
        
        if valor < valor_siguiente:
            return valor_siguiente - valor + convertir(num_romano[2:])
        else:
            return valor + convertir(num_romano[1:])
    else:
        return valor
    
    
print(convertir("IV"))
print(convertir("IX"))
print(convertir("L"))




