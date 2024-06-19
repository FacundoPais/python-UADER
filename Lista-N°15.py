class Pokemon:
    def __init__(self, nombre, nivel, tipo, subtipo):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        return f"{self.nombre} (Nivel: {self.nivel}, Tipo: {self.tipo}, Subtipo: {self.subtipo})"

class Entrenador:
    def __init__(self, nombre, torneos_ganados, batallas_perdidas, batallas_ganadas):
        self.nombre = nombre
        self.torneos_ganados = torneos_ganados
        self.batallas_perdidas = batallas_perdidas
        self.batallas_ganadas = batallas_ganadas
        self.pokemons = []

    def agregar_pokemon(self, pokemon):
        self.pokemons.append(pokemon)

    def __str__(self):
        return f"{self.nombre} (Torneos ganados: {self.torneos_ganados}, Batallas ganadas: {self.batallas_ganadas}, Batallas perdidas: {self.batallas_perdidas})"


def cantidad_pokemons(entrenador):
    return len(entrenador.pokemons)


def mas_tres(lista_entrenadores):
    resultado = []
    for entrenador in lista_entrenadores:
        if entrenador.torneos_ganados > 3:
            resultado.append(entrenador)
    return resultado


def mayor_nivel_entrenador(lista_entrenadores):
    entrenador_campeon = None
    for entrenador in lista_entrenadores:
        if entrenador_campeon is None or entrenador.torneos_ganados > entrenador_campeon.torneos_ganados:
            entrenador_campeon = entrenador
    
    if entrenador_campeon is not None and entrenador_campeon.pokemons:
        pokemon_max_nivel = None
        for pokemon in entrenador_campeon.pokemons:
            if pokemon_max_nivel is None or pokemon.nivel > pokemon_max_nivel.nivel:
                pokemon_max_nivel = pokemon
        return pokemon_max_nivel
    
    return None


def datos_entrenador(entrenador):
    print(entrenador)
    for pokemon in entrenador.pokemons:
        print(pokemon)


def porcentaje_ganado(lista_entrenadores, porcentaje):
    resultado = []
    for entrenador in lista_entrenadores:
        total_batallas = entrenador.batallas_ganadas + entrenador.batallas_perdidas
        if total_batallas > 0:
            porcentaje_ganado = (entrenador.batallas_ganadas / total_batallas) * 100
            if porcentaje_ganado > porcentaje:
                resultado.append(entrenador)
    return resultado


def fuego_planta(lista_entrenadores):
    entrenadores = []
    for entrenador in lista_entrenadores:
        tiene_fuego_planta = False
        tiene_agua_volador = False
        for pokemon in entrenador.pokemons:
            if pokemon.tipo == "Fuego" and pokemon.subtipo == "Planta":
                tiene_fuego_planta = True
            if pokemon.tipo == "Agua" and pokemon.subtipo == "Volador":
                tiene_agua_volador = True
        if tiene_fuego_planta or tiene_agua_volador:
            entrenadores.append(entrenador)
    return entrenadores


def promedio_nivel_pokemons(entrenador):
    if not entrenador.pokemons:
        return 0
    suma_niveles = 0
    for pokemon in entrenador.pokemons:
        suma_niveles += pokemon.nivel
    return suma_niveles / len(entrenador.pokemons)


def entrenadores_con_pokemon(lista_entrenadores, nombre_pokemon):
    contador = 0
    for entrenador in lista_entrenadores:
        for pokemon in entrenador.pokemons:
            if pokemon.nombre == nombre_pokemon:
                contador += 1
    return contador


def pokemons_repetidos(lista_entrenadores):
    entrenadores = []
    for entrenador in lista_entrenadores:
        nombres_pokemons = []
        for pokemon in entrenador.pokemons:
            if pokemon.nombre in nombres_pokemons:
                entrenadores.append(entrenador)
                break
            nombres_pokemons.append(pokemon.nombre)
    return entrenadores


def pokemons_especificos(lista_entrenadores):
    pokemons_especificos = {"Tyrantrum", "Terrakion", "Wingull"}
    entrenadores = []
    for entrenador in lista_entrenadores:
        for pokemon in entrenador.pokemons:
            if pokemon.nombre in pokemons_especificos:
                entrenadores.append(entrenador)
                break
    return entrenadores


def entrenador_tiene_pokemon(lista_entrenadores, nombre_entrenador, nombre_pokemon):
    for entrenador in lista_entrenadores:
        if entrenador.nombre == nombre_entrenador:
            for pokemon in entrenador.pokemons:
                if pokemon.nombre == nombre_pokemon:
                    print(entrenador)
                    print(pokemon)
                    return True
    return False



entrenador1 = Entrenador("Ash", 5, 10, 40)
entrenador1.agregar_pokemon(Pokemon("Pikachu", 25, "Eléctrico", ""))
entrenador1.agregar_pokemon(Pokemon("Charizard", 36, "Fuego", "Volador"))
entrenador1.agregar_pokemon(Pokemon("Bulbasaur", 15, "Planta", "Veneno"))

entrenador2 = Entrenador("Misty", 3, 5, 30)
entrenador2.agregar_pokemon(Pokemon("Starmie", 28, "Agua", "Psíquico"))
entrenador2.agregar_pokemon(Pokemon("Gyarados", 40, "Agua", "Volador"))
entrenador2.agregar_pokemon(Pokemon("Psyduck", 20, "Agua", ""))

entrenador3 = Entrenador("Brock", 7, 3, 50)
entrenador3.agregar_pokemon(Pokemon("Onix", 35, "Roca", "Tierra"))
entrenador3.agregar_pokemon(Pokemon("Geodude", 22, "Roca", "Tierra"))
entrenador3.agregar_pokemon(Pokemon("Vulpix", 18, "Fuego", ""))

entrenador4 = Entrenador("Gary", 4, 4, 45)
entrenador4.agregar_pokemon(Pokemon("Eevee", 30, "Normal", ""))
entrenador4.agregar_pokemon(Pokemon("Blastoise", 42, "Agua", ""))
entrenador4.agregar_pokemon(Pokemon("Nidoking", 37, "Veneno", "Tierra"))

entrenador5 = Entrenador("Lance", 10, 2, 60)
entrenador5.agregar_pokemon(Pokemon("Dragonite", 55, "Dragón", "Volador"))
entrenador5.agregar_pokemon(Pokemon("Aerodactyl", 50, "Roca", "Volador"))
entrenador5.agregar_pokemon(Pokemon("Gyarados", 45, "Agua", "Volador"))

lista_entrenadores = [entrenador1, entrenador2, entrenador3, entrenador4, entrenador5]

# a
print(f"Ash tiene {cantidad_pokemons(entrenador1)} pokémons")

# b
print("Entrenadores con más de 3 torneos ganados:")
for entrenador in mas_tres(lista_entrenadores):
    print(entrenador)

# c
pokemon_max_nivel = mayor_nivel_entrenador(lista_entrenadores)
if pokemon_max_nivel:
    print(f"El Pokémon de mayor nivel del entrenador con más torneos ganados es {pokemon_max_nivel}")

# d
print("Datos de Ash y sus Pokémons:")
datos_entrenador(entrenador1)

# e
print("Entrenadores con porcentaje de batallas ganadas mayor al 79%:")
for entrenador in porcentaje_ganado(lista_entrenadores, 79):
    print(entrenador)

# f
print("Entrenadores con Pokémons de tipo fuego/planta o agua/volador:")
for entrenador in fuego_planta(lista_entrenadores):
    print(entrenador)

# g
print(f"Promedio de nivel de los Pokémons de Ash: {promedio_nivel_pokemons(entrenador1)}")

# h
print(f"Entrenadores que tienen a Gyarados: {entrenadores_con_pokemon(lista_entrenadores, 'Gyarados')}")

# i
print("Entrenadores con Pokémons repetidos:")
for entrenador in pokemons_repetidos(lista_entrenadores):
    print(entrenador)

# j
print("Entrenadores que tienen Tyrantrum, Terrakion o Wingull:")
for entrenador in pokemons_especificos(lista_entrenadores):
    print(entrenador)

# k
if entrenador_tiene_pokemon(lista_entrenadores, "Ash", "Charizard"):
    print("Ash tiene a Charizard")
else:
    print("Ash no tiene a Charizard")

