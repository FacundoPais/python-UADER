#16. Se tienen dos pilas con personajes de Star Wars, en una los del episodio V de “The empire
#strikes back” y la otra los del episodio VII “The force awakens”. Desarrollar un algoritmo que

#permita obtener la intersección de ambas pilas, es decir los personajes que aparecen en am-
#bos episodios.

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
    
episodio_V = Stack()
episodio_V.push('Luke Skywalker')
episodio_V.push('Darth Vader')
episodio_V.push('Leia Organa')
episodio_V.push('Yoda')
episodio_V.push('Han Solo')

episodio_VII = Stack()
episodio_VII.push('Luke Skywalker')
episodio_VII.push('Leia Organa')
episodio_VII.push('Han Solo')
episodio_VII.push('Rey')
episodio_VII.push('Finn')

def interseccion_pilas(pila1, pila2):
    elementos_pila1 = []
    elementos_pila2 = []
    
    
    while pila1.size() > 0:
        elementos_pila1.append(pila1.pop())
    
    
    for elemento in elementos_pila1:
        pila1.push(elemento)
    
    
    conjunto_pila1 = set(elementos_pila1)
    
    
    while pila2.size() > 0:
        elementos_pila2.append(pila2.pop())
    
    
    for elemento in elementos_pila2:
        pila2.push(elemento)
    
    interseccion = Stack()
    
    
    for personaje in elementos_pila2:
        if personaje in conjunto_pila1:
            interseccion.push(personaje)
    
    return interseccion


interseccion = interseccion_pilas(episodio_V, episodio_VII)


print("Los personajes en ambos episodios son:")
while interseccion.size() > 0:
    print(interseccion.pop())
