from heap import HeapMin

class Graph:
    def __init__(self, dirigido=False):
        self.vertices = {}
        self.dirigido = dirigido

    def show_graph(self):
        print("\nNodos:")
        for vertice, datos in self.vertices.items():
            print(f"{vertice} ({datos['tipo']} - {datos['paises']})")
            print("    Aristas:")
            for arista, peso in datos['aristas'].items():
                print(f"    Destino: {arista} - Peso: {peso}")
        print()

    def insert_vertice(self, nombre, tipo, paises):
        if nombre not in self.vertices:
            self.vertices[nombre] = {
                'tipo': tipo,
                'paises': paises,
                'aristas': {}
            }

    def insert_arista(self, origen, destino, peso):
        if origen in self.vertices and destino in self.vertices:
            self.vertices[origen]['aristas'][destino] = peso
            if not self.dirigido:
                self.vertices[destino]['aristas'][origen] = peso

    def kruskal(self, tipo):
        def find_set(bosque, buscado):
            for index, arbol in enumerate(bosque):
                if buscado in arbol:
                    return index
            return None

        bosque = [[v] for v, datos in self.vertices.items() if datos['tipo'] == tipo]
        aristas = HeapMin()
        
        for vertice, datos in self.vertices.items():
            if datos['tipo'] == tipo:
                for adj, peso in datos['aristas'].items():
                    aristas.arrive((vertice, adj, peso), peso)

        arbol_minimo = []
        while len(bosque) > 1 and len(aristas.elements) > 0:
            _, (origen, destino, peso) = aristas.atention()
            pos_origen = find_set(bosque, origen)
            pos_destino = find_set(bosque, destino)
            if pos_origen is not None and pos_destino is not None and pos_origen != pos_destino:
                arbol_minimo.append((origen, destino, peso))
                bosque[pos_origen].extend(bosque.pop(pos_destino))
        return arbol_minimo

    def paises_con_maravillas_de_ambos_tipos(self):
        paises_arquitectonicos = set()
        paises_naturales = set()
        
        for vertice, datos in self.vertices.items():
            if datos['tipo'] == 'arquitectónica':
                paises_arquitectonicos.update(datos['paises'])
            elif datos['tipo'] == 'natural':
                paises_naturales.update(datos['paises'])

        return paises_arquitectonicos.intersection(paises_naturales)

    def paises_con_multiples_maravillas_del_mismo_tipo(self):
        maravillas_por_pais = {}
        
        for vertice, datos in self.vertices.items():
            for pais in datos['paises']:
                if pais not in maravillas_por_pais:
                    maravillas_por_pais[pais] = {'arquitectónica': 0, 'natural': 0}
                maravillas_por_pais[pais][datos['tipo']] += 1

        paises_multiples = {
            pais for pais, conteo in maravillas_por_pais.items()
            if conteo['arquitectónica'] > 1 or conteo['natural'] > 1
        }
        
        return paises_multiples

# Inicialización del grafo
grafo = Graph(dirigido=False)

# Maravillas arquitectónicas
maravillas_arquitectonicas = [
    ("Chichen Itza", "arquitectónica", ["México"]),
    ("Coliseo", "arquitectónica", ["Italia"]),
    ("Cristo Redentor", "arquitectónica", ["Brasil"]),
    ("Gran Muralla China", "arquitectónica", ["China"]),
    ("Machu Picchu", "arquitectónica", ["Perú"]),
    ("Petra", "arquitectónica", ["Jordania"]),
    ("Taj Mahal", "arquitectónica", ["India"])
]

# Maravillas naturales
maravillas_naturales = [
    ("Amazonia", "natural", ["Brasil", "Perú", "Colombia", "Venezuela", "Ecuador", "Bolivia"]),
    ("Bahía de Ha-Long", "natural", ["Vietnam"]),
    ("Cataratas del Iguazú", "natural", ["Argentina", "Brasil"]),
    ("Isla Jeju", "natural", ["Corea del Sur"]),
    ("Komodo", "natural", ["Indonesia"]),
    ("Montaña de la Mesa", "natural", ["Sudáfrica"]),
    ("Río subterráneo de Puerto Princesa", "natural", ["Filipinas"])
]

# Inserción de vértices en el grafo
for nombre, tipo, paises in maravillas_arquitectonicas + maravillas_naturales:
    grafo.insert_vertice(nombre, tipo, paises)

# Inserción de aristas para maravillas del mismo tipo (distancias ficticias)
for i in range(len(maravillas_arquitectonicas)):
    for j in range(i + 1, len(maravillas_arquitectonicas)):
        grafo.insert_arista(maravillas_arquitectonicas[i][0], maravillas_arquitectonicas[j][0], (i + j) * 100)

for i in range(len(maravillas_naturales)):
    for j in range(i + 1, len(maravillas_naturales)):
        grafo.insert_arista(maravillas_naturales[i][0], maravillas_naturales[j][0], (i + j) * 100)

# Mostrar el grafo
grafo.show_graph()

# Árbol de expansión mínimo para cada tipo
print("\nÁrbol de expansión mínimo para maravillas arquitectónicas:")
arbol_expansion_arquitectonico = grafo.kruskal('arquitectónica')
for origen, destino, peso in arbol_expansion_arquitectonico:
    print(f"origen: {origen} -> destino: {destino} peso: {peso}")

print("\nÁrbol de expansión mínimo para maravillas naturales:")
arbol_expansion_natural = grafo.kruskal('natural')
for origen, destino, peso in arbol_expansion_natural:
    print(f"origen: {origen} -> destino: {destino} peso: {peso}")

# Países con maravillas de ambos tipos
paises_ambas_maravillas = grafo.paises_con_maravillas_de_ambos_tipos()
print("\nPaíses con maravillas de ambos tipos:")
print(paises_ambas_maravillas)

# Países con múltiples maravillas del mismo tipo
paises_multiples_maravillas = grafo.paises_con_multiples_maravillas_del_mismo_tipo()
print("\nPaíses con múltiples maravillas del mismo tipo:")
print(paises_multiples_maravillas)
