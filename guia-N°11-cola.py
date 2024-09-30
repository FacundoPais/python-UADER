class Queue:

    def __init__(self):
        self.__elements = []

    def arrive(self, element):
        self.__elements.append(element)

    def attention(self):
        if len(self.__elements) > 0:
            return self.__elements.pop(0)
        else:
            return None
    
    def size(self):
        return len(self.__elements)

    def on_front(self):
        if len(self.__elements) > 0:
            return self.__elements[0]
        else:
            return None
    
    def move_to_end(self):
        element = self.attention()
        if element is not None:
            self.arrive(element)


characters_queue = Queue()
characters_queue.arrive({'name': 'Luke Skywalker', 'planet': 'Tatooine'})
characters_queue.arrive({'name': 'Han Solo', 'planet': 'Corellia'})
characters_queue.arrive({'name': 'Leia Organa', 'planet': 'Alderaan'})
characters_queue.arrive({'name': 'Yoda', 'planet': 'Dagobah'})
characters_queue.arrive({'name': 'Darth Vader', 'planet': 'Tatooine'})
characters_queue.arrive({'name': 'Jar Jar Binks', 'planet': 'Naboo'})
characters_queue.arrive({'name': 'Chewbacca', 'planet': 'Kashyyyk'})
characters_queue.arrive({'name': 'Wicket W. Warrick', 'planet': 'Endor'})

# a
def show_characters_by_planet(queue, planets):
    temp_list = []
    result = []
    
    while queue.size() > 0:
        character = queue.attention()
        if character['planet'] in planets:
            result.append(character)
        temp_list.append(character)
    
    for character in temp_list:
        queue.arrive(character)
    
    print("Personajes de Alderaan, Endor y Tatooine:")
    for character in result:
        print(f"Nombre: {character['name']}, Planeta: {character['planet']}")

# b
def show_home_planet(queue, names):
    temp_list = []
    result = {}
    
    while queue.size() > 0:
        character = queue.attention()
        if character['name'] in names:
            result[character['name']] = character['planet']
        temp_list.append(character)
    
    for character in temp_list:
        queue.arrive(character)
    
    for name in names:
        print(f"{name} es de {result.get(name, 'desconocido')}")

# c
def insert_before_character(queue, new_character, before_name):
    temp_list = []
    inserted = False
    
    while queue.size() > 0:
        character = queue.attention()
        if character['name'] == before_name and not inserted:
            temp_list.append(new_character)
            inserted = True
        temp_list.append(character)
    
    for character in temp_list:
        queue.arrive(character)

# d
def remove_after_character(queue, after_name):
    temp_list = []
    remove_next = False
    
    while queue.size() > 0:
        character = queue.attention()
        if remove_next:
            remove_next = False
            continue
        temp_list.append(character)
        if character['name'] == after_name:
            remove_next = True
    
    for character in temp_list:
        queue.arrive(character)

def show_all_characters(queue):
    temp_list = []
    while queue.size() > 0:
        character = queue.attention()
        print(f"Nombre: {character['name']}, Planeta: {character['planet']}")
        temp_list.append(character)
    
    for character in temp_list:
        queue.arrive(character)


print("a. Personajes de Alderaan, Endor y Tatooine:")
show_characters_by_planet(characters_queue, ['Alderaan', 'Endor', 'Tatooine'])

print("\nb. Planetas natales de Luke Skywalker y Han Solo:")
show_home_planet(characters_queue, ['Luke Skywalker', 'Han Solo'])

print("\nc. Insertar a Ahsoka Tano antes de Yoda:")
insert_before_character(characters_queue, {'name': 'Ahsoka Tano', 'planet': 'Shili'}, 'Yoda')
show_all_characters(characters_queue)

print("\nd. Eliminar el personaje después de Jar Jar Binks:")
remove_after_character(characters_queue, 'Jar Jar Binks')
show_all_characters(characters_queue)
