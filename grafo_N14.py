class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.aristas = {}  # Diccionario de aristas

    def agregar_arista(self, destino, peso):
        self.aristas[destino] = peso

class Grafo:
    def __init__(self):
        self.elementos = {}  # Diccionario de nodos

    def agregar_nodo(self, nombre):
        nuevo_nodo = Nodo(nombre)
        self.elementos[nombre] = nuevo_nodo

    def agregar_arista(self, origen, destino, peso):
        if origen in self.elementos and destino in self.elementos:
            self.elementos[origen].agregar_arista(destino, peso)
            self.elementos[destino].agregar_arista(origen, peso)  

    def obtener_nodos(self):
        return self.elementos.keys()

    def prim(self):
        nodos_visitados = set()
        arbol = []
        total_peso = 0
        nodos = list(self.elementos.keys())
        nodo_inicial = nodos[0]  
        nodos_visitados.add(nodo_inicial)

        while len(nodos_visitados) < len(nodos):
            arista_minima = (None, None, float('inf'))  # (origen, destino, peso)
            for nodo in nodos_visitados:
                for vecino, peso in self.elementos[nodo].aristas.items():
                    if vecino not in nodos_visitados and peso < arista_minima[2]:
                        arista_minima = (nodo, vecino, peso)

            if arista_minima[0] is not None:
                arbol.append(arista_minima)
                total_peso += arista_minima[2]
                nodos_visitados.add(arista_minima[1])

        return arbol, total_peso

    def dijkstra(self, start):
        distances = {node: float('infinity') for node in self.elementos}
        distances[start] = 0
        priority_queue = HeapMin()
        priority_queue.insert((0, start))
        visited = set()

        while not priority_queue.is_empty():
            current_distance, current_node = priority_queue.remove_min()

            if current_node in visited:
                continue

            visited.add(current_node)

            for neighbor, weight in self.elementos[current_node].aristas.items():
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    priority_queue.insert((distance, neighbor))

        return distances

class HeapMin:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        self.heap.append(item)
        self._bubble_up(len(self.heap) - 1)

    def remove_min(self):
        if not self.heap:
            return None
        min_item = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._bubble_down(0)
        return min_item

    def is_empty(self):
        return len(self.heap) == 0

    def _bubble_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index][0] < self.heap[parent_index][0]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def _bubble_down(self, index):
        length = len(self.heap)
        while True:
            left_index = 2 * index + 1
            right_index = 2 * index + 2
            smallest_index = index

            if left_index < length and self.heap[left_index][0] < self.heap[smallest_index][0]:
                smallest_index = left_index

            if right_index < length and self.heap[right_index][0] < self.heap[smallest_index][0]:
                smallest_index = right_index

            if smallest_index == index:
                break

            self.heap[index], self.heap[smallest_index] = self.heap[smallest_index], self.heap[index]
            index = smallest_index


grafo = Grafo()


nodos = ["cocina", "comedor", "cochera", "quincho", "baño 1", "baño 2", "habitación 1", "habitación 2", "sala de estar", "terraza", "patio"]
for nodo in nodos:
    grafo.agregar_nodo(nodo)


aristas = [
    
    ("cocina", "comedor", 5),
    ("cocina", "baño 1", 3),
    ("cocina", "cochera", 10),
    ("cocina", "sala de estar", 12),
    ("cocina", "habitación 1", 8),
    
    
    ("comedor", "habitación 1", 4),
    ("comedor", "quincho", 6),
    ("comedor", "terraza", 7),
    
    
    ("cochera", "patio", 11),
    ("cochera", "quincho", 15),
    ("cochera", "sala de estar", 14),
    ("cochera", "terraza", 9),
    ("cochera", "baño 2", 6),
    
    
    ("quincho", "terraza", 4),
    ("quincho", "baño 2", 5),
    ("quincho", "patio", 3),
    
    
    ("baño 1", "baño 2", 2),
    ("baño 1", "habitación 1", 4),
    ("baño 1", "sala de estar", 6),
    
    
    ("baño 2", "habitación 1", 5),
    ("baño 2", "habitación 2", 7),
    ("baño 2", "terraza", 8),
    
    
    ("habitación 1", "habitación 2", 7),
    ("habitación 1", "sala de estar", 10),
    ("habitación 1", "terraza", 6),
    
    
    ("habitación 2", "sala de estar", 9),
    ("habitación 2", "patio", 8),
    ("habitación 2", "terraza", 5),
    
    
    ("sala de estar", "patio", 8),
    ("sala de estar", "terraza", 6),
    ("sala de estar", "cocina", 12),
    
    
    ("terraza", "patio", 3),
    ("terraza", "quincho", 4),
    ("terraza", "comedor", 7),
    
    
    ("patio", "cochera", 11),
    ("patio", "quincho", 3),
    ("patio", "habitación 2", 8)
]

for origen, destino, peso in aristas:
    grafo.agregar_arista(origen, destino, peso)


print("Nodos")
for nodo in grafo.obtener_nodos():
    print(f"  {nodo}")
    print("    Aristas")
    for vecino, peso in grafo.elementos[nodo].aristas.items():
        print(f"    Destino {vecino} peso: {peso} metros")

# Árbol de expansión mínima y total de metros de cable necesarios
arbol_prim, total_peso = grafo.prim()
print("\nÁrbol de expansión mínima:")
for arista in arbol_prim:
    print(f"{arista[0]} - {arista[1]} - {arista[2]} metros")
print(f"Total de metros de cable necesarios: {total_peso} metros")

# desde "habitación 1" para encontrar el camino más corto a "sala de estar"
resultado_dijkstra = grafo.dijkstra("habitación 1")
print("\nCamino más corto desde 'habitación 1' hasta 'sala de estar':")
print(f"Distancia: {resultado_dijkstra['sala de estar']} metros")
