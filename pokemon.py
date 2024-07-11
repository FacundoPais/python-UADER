class Pokemon:
    def __init__(self, nombre, nivel, tipo, subtipo=None):
        self.nombre = nombre
        self.nivel = nivel
        self.tipos = [tipo]
        if subtipo:
            self.tipos.append(subtipo)
        self.entrenador = None

class Entrenador:
    def __init__(self, nombre, torneos_ganados, batallas_perdidas, batallas_ganadas):
        self.nombre = nombre
        self.torneos_ganados = torneos_ganados
        self.batallas_perdidas = batallas_perdidas
        self.batallas_ganadas = batallas_ganadas
        self.pokemons = []

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash(self, key):
        return key % self.size
    
    def insert(self, key, pokemon):
        hash_key = self._hash(key)
        self.table[hash_key].append(pokemon)
    
    def search(self, key):
        hash_key = self._hash(key)
        return self.table[hash_key]

    def display(self):
        for i in range(self.size):
            print(f"Index {i}: {self.table[i]}")

type_table = HashTable(20) 
number_table = HashTable(10)
level_table = HashTable(10)

def insert_pokemon(pokemon):
    for tipo in pokemon.tipos:
        type_key = hash(tipo)
        type_table.insert(type_key, pokemon)
    
    number_key = int(str(pokemon.nivel)[-1])
    number_table.insert(number_key, pokemon)
    
    level_key = pokemon.nivel % 10
    level_table.insert(level_key, pokemon)

pokemon_list = [
    {"nombre": "Pikachu", "nivel": 35, "tipo": "Eléctrico", "subtipo": None},
    {"nombre": "Charizard", "nivel": 40, "tipo": "Fuego", "subtipo": "Volador"},
    {"nombre": "Bulbasaur", "nivel": 30, "tipo": "Planta", "subtipo": "Veneno"},
    {"nombre": "Starmie", "nivel": 30, "tipo": "Agua", "subtipo": "Psíquico"},
    {"nombre": "Psyduck", "nivel": 25, "tipo": "Agua", "subtipo": None},
    {"nombre": "Gyarados", "nivel": 35, "tipo": "Agua", "subtipo": "Volador"},
    {"nombre": "Onix", "nivel": 38, "tipo": "Roca", "subtipo": "Tierra"},
    {"nombre": "Geodude", "nivel": 28, "tipo": "Roca", "subtipo": "Tierra"},
    {"nombre": "Vulpix", "nivel": 20, "tipo": "Fuego", "subtipo": None},
    {"nombre": "Blastoise", "nivel": 50, "tipo": "Agua", "subtipo": None},
    {"nombre": "Umbreon", "nivel": 45, "tipo": "Siniestro", "subtipo": None},
    {"nombre": "Nidoking", "nivel": 40, "tipo": "Veneno", "subtipo": "Tierra"}
]

entrenador_list = [
    {"nombre": "Ash Ketchum", "torneos_ganados": 7, "batallas_perdidas": 50, "batallas_ganadas": 120},
    {"nombre": "Goh", "torneos_ganados": 2, "batallas_perdidas": 10, "batallas_ganadas": 40},
    {"nombre": "Leon", "torneos_ganados": 10, "batallas_perdidas": 5, "batallas_ganadas": 100},
    {"nombre": "Chloe", "torneos_ganados": 1, "batallas_perdidas": 8, "batallas_ganadas": 30},
    {"nombre": "Raihan", "torneos_ganados": 4, "batallas_perdidas": 15, "batallas_ganadas": 60}
]

pokemons = [Pokemon(p["nombre"], p["nivel"], p["tipo"], p["subtipo"]) for p in pokemon_list]
entrenadores = [Entrenador(e["nombre"], e["torneos_ganados"], e["batallas_perdidas"], e["batallas_ganadas"]) for e in entrenador_list]


for i, entrenador in enumerate(entrenadores):
    entrenador.pokemons.append(pokemons[i])
    pokemons[i].entrenador = entrenador.nombre
    insert_pokemon(pokemons[i])

def mostrar_pokemon_por_numero():
    numeros_interes = [3, 7, 9]
    for num in numeros_interes:
        pokemons = number_table.search(num)
        for pokemon in pokemons:
            print(f"Número: {pokemon.nivel}, Nombre: {pokemon.nombre}, Entrenador: {pokemon.entrenador}")

print("Pokémon cuyos números terminan en 3, 7 y 9:")
mostrar_pokemon_por_numero()

def mostrar_pokemon_por_nivel():
    for nivel in range(10):
        if nivel % 2 == 0 or nivel % 5 == 0:
            pokemons = level_table.search(nivel)
            for pokemon in pokemons:
                print(f"Nivel: {pokemon.nivel}, Nombre: {pokemon.nombre}, Entrenador: {pokemon.entrenador}")

print("\nPokémon cuyos niveles son múltiplos de 2, 5 y 10:")
mostrar_pokemon_por_nivel()


def mostrar_pokemon_por_tipo():
    tipos_interes = ["Acero", "Fuego", "Eléctrico", "Hielo"]
    for tipo in tipos_interes:
        tipo_key = hash(tipo)
        pokemons = type_table.search(tipo_key)
        for pokemon in pokemons:
            print(f"Tipo: {tipo}, Nombre: {pokemon.nombre}, Entrenador: {pokemon.entrenador}")

print("\nPokémon de los tipos Acero, Fuego, Eléctrico, Hielo:")
mostrar_pokemon_por_tipo()

print("Pokémon cuyos números terminan en 3, 7 y 9:")
mostrar_pokemon_por_numero()

print("\nPokémon cuyos niveles son múltiplos de 2, 5 y 10:")
mostrar_pokemon_por_nivel()

print("\nPokémon de los tipos Acero, Fuego, Eléctrico, Hielo:")
mostrar_pokemon_por_tipo()


