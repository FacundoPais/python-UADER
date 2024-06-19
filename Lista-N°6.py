superheroes = [
    {'nombre': 'Linterna Verde', 'anio_aparicion': 1940, 'casa': 'DC', 'biografia': 'Posee un anillo de poder'},
    {'nombre': 'Wolverine', 'anio_aparicion': 1974, 'casa': 'Marvel', 'biografia': 'Tiene garras de adamantium'},
    {'nombre': 'Dr. Strange', 'anio_aparicion': 1963, 'casa': 'DC', 'biografia': 'Hechicero Supremo'},
    {'nombre': 'Capitana Marvel', 'anio_aparicion': 1967, 'casa': 'Marvel', 'biografia': 'Tiene poderes cósmicos'},
    {'nombre': 'Mujer Maravilla', 'anio_aparicion': 1941, 'casa': 'DC', 'biografia': 'Princesa Amazona'},
    {'nombre': 'Flash', 'anio_aparicion': 1940, 'casa': 'DC', 'biografia': 'El hombre más rápido del mundo'},
    {'nombre': 'Star-Lord', 'anio_aparicion': 1976, 'casa': 'Marvel', 'biografia': 'Líder de los Guardianes de la Galaxia'},
    {'nombre': 'Batman', 'anio_aparicion': 1939, 'casa': 'DC', 'biografia': 'El Caballero Oscuro'},
    {'nombre': 'Spider-Man', 'anio_aparicion': 1962, 'casa': 'Marvel', 'biografia': 'El Hombre Araña'},
    {'nombre': 'Iron Man', 'anio_aparicion': 1963, 'casa': 'Marvel', 'biografia': 'Hombre en armadura tecnológica'}
]

def eliminar(superheroes, nombre):
    nueva_lista = []
    for heroe in superheroes:
        if heroe['nombre'] != nombre:
            nueva_lista.append(heroe)
    return nueva_lista

def anio_aparicion(superheroes, nombre):
    for heroe in superheroes:
        if heroe['nombre'] == nombre:
            return heroe['anio_aparicion']
    return None

def cambiar_casa(superheroes, nombre, nueva_casa):
    for heroe in superheroes:
        if heroe['nombre'] == nombre:
            heroe['casa'] = nueva_casa
    return superheroes

def biografia(superheroes, palabras):
    resultado = []
    for heroe in superheroes:
        for palabra in palabras:
            if palabra in heroe['biografia']:
                resultado.append(heroe['nombre'])
                break
    return resultado

def antes_1963(superheroes, anio):
    resultado = []
    for heroe in superheroes:
        if heroe['anio_aparicion'] < anio:
            resultado.append((heroe['nombre'], heroe['casa']))
    return resultado

def casa_de_superheroe(superheroes, nombres):
    resultado = {}
    for heroe in superheroes:
        if heroe['nombre'] in nombres:
            resultado[heroe['nombre']] = heroe['casa']
    return resultado

def info_superheroes(superheroes, nombres):
    resultado = []
    for heroe in superheroes:
        if heroe['nombre'] in nombres:
            resultado.append(heroe)
    return resultado

def arrancan_con(superheroes, letras):
    resultado = []
    for heroe in superheroes:
        if heroe['nombre'][0] in letras:
            resultado.append(heroe['nombre'])
    return resultado

def contar_heroes(superheroes):
    contador = {}
    for heroe in superheroes:
        casa = heroe['casa']
        if casa in contador:
            contador[casa] += 1
        else:
            contador[casa] = 1
    return contador

# a
superheroes = eliminar(superheroes, 'Linterna Verde')

# b
anio_wolverine = anio_aparicion(superheroes, 'Wolverine')
print(f'Año de aparición de Wolverine: {anio_wolverine}')

# c
superheroes = cambiar_casa(superheroes, 'Dr. Strange', 'Marvel')

# d
heroes = biografia(superheroes, ['traje', 'armadura'])
print(f'Superhéroes con "traje" o "armadura" en su biografía: {heroes}')

# e
heroes2 = antes_1963(superheroes, 1963)
print(f'Superhéroes anteriores a 1963: {heroes2}')

# f
casas = casa_de_superheroe(superheroes, ['Capitana Marvel', 'Mujer Maravilla'])
print(f'Casas de Capitana Marvel y Mujer Maravilla: {casas}')

# g
informacion = info_superheroes(superheroes, ['Flash', 'Star-Lord'])
print(f'Información de Flash y Star-Lord: {informacion}')

# h
heroes3 = arrancan_con(superheroes, ['B', 'M', 'S'])
print(f'Superhéroes que comienzan con B, M y S: {heroes3}')

# i
conteo = contar_heroes(superheroes)
print(f'Cantidad de superhéroes por casa: {conteo}')
