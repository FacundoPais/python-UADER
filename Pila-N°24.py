#24. Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
#su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
#necesarias para resolver las siguientes actividades:

#a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posi-
#ción uno la cima de la pila;

#b. determinar los personajes que participaron en más de 5 películas de la saga, además indi-
#car la cantidad de películas en la que aparece;

#c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
#d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.
class Stack:
    def __init__(self):
        self.__elements = []

    def push(self, element):
        self.__elements.append(element)

    def pop(self):
        if len(self.__elements) > 0:
            return self.__elements.pop()
        else:
            return None

    def on_top(self):
        if len(self.__elements) > 0:
            return self.__elements[-1]
        else:
            return None

    def size(self):
        return len(self.__elements)

class Personaje:
    def __init__(self, nombre, cantidad_peliculas):
        self.nombre = nombre
        self.cantidad_peliculas = cantidad_peliculas

    def __str__(self):
        return f"{self.nombre} ({self.cantidad_peliculas} películas)"


pila_marvel = Stack()
pila_marvel.push(Personaje("Iron Man", 10))
pila_marvel.push(Personaje("Capitán América", 9))
pila_marvel.push(Personaje("Thor", 8))
pila_marvel.push(Personaje("Hulk", 7))
pila_marvel.push(Personaje("Viuda Negra", 7))
pila_marvel.push(Personaje("Ojo de Halcón", 5))
pila_marvel.push(Personaje("Groot", 4))
pila_marvel.push(Personaje("Rocket Raccoon", 5))
pila_marvel.push(Personaje("Spider-Man", 3))
pila_marvel.push(Personaje("Doctor Strange", 4))

# a. Determinar la posición de Rocket Raccoon y Groot
def encontrar_posicion(pila, nombre_personaje):
    pila_temporal = Stack()
    posicion = 1
    posicion_encontrada = -1
    
    
    while pila.size() > 0:
        personaje = pila.pop()
        pila_temporal.push(personaje)
        if personaje.nombre == nombre_personaje:
            posicion_encontrada = posicion
        posicion += 1
    
    
    while pila_temporal.size() > 0:
        pila.push(pila_temporal.pop())
    
    return posicion_encontrada

posicion_rocket = encontrar_posicion(pila_marvel, "Rocket Raccoon")
posicion_groot = encontrar_posicion(pila_marvel, "Groot")

print(f"Rocket Raccoon se encuentra en la posición: {posicion_rocket}")
print(f"Groot se encuentra en la posición: {posicion_groot}")

# b. Determinar los personajes que participaron en más de 5 películas
# c. Determinar en cuántas películas participó Viuda Negra
def personajes_mas_de_5_peliculas(pila):
    pila_temporal = Stack()
    resultado = []
    
    
    while pila.size() > 0:
        personaje = pila.pop()
        pila_temporal.push(personaje)
        if personaje.cantidad_peliculas > 5:
            resultado.append((personaje.nombre, personaje.cantidad_peliculas))
    
    
    while pila_temporal.size() > 0:
        pila.push(pila_temporal.pop())
    
    return resultado

personajes_mas_5 = personajes_mas_de_5_peliculas(pila_marvel)
print("Personajes que participaron en más de 5 películas:")
for nombre, cantidad in personajes_mas_5:
    print(f"{nombre} ({cantidad} películas)")


# d. Mostrar todos los personajes cuyos nombres empiezan con C, D y G
def personajes_que_empiezan_con(pila, iniciales):
    pila_temporal = Stack()
    resultado = []
    
    
    while pila.size() > 0:
        personaje = pila.pop()
        pila_temporal.push(personaje)
        if personaje.nombre[0] in iniciales:
            resultado.append(personaje.nombre)
    
    
    while pila_temporal.size() > 0:
        pila.push(pila_temporal.pop())
    
    return resultado

personajes_c_d_g = personajes_que_empiezan_con(pila_marvel, {'C', 'D', 'G'})
print("Personajes cuyos nombres empiezan con C, D y G:")
for nombre in personajes_c_d_g:
    print(nombre)