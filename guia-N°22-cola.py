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


mcu_queue = Queue()
mcu_queue.arrive({'name': 'Tony Stark', 'superhero': 'Iron Man', 'gender': 'M'})
mcu_queue.arrive({'name': 'Steve Rogers', 'superhero': 'Capitán América', 'gender': 'M'})
mcu_queue.arrive({'name': 'Natasha Romanoff', 'superhero': 'Black Widow', 'gender': 'F'})
mcu_queue.arrive({'name': 'Carol Danvers', 'superhero': 'Capitana Marvel', 'gender': 'F'})
mcu_queue.arrive({'name': 'Scott Lang', 'superhero': 'Ant-Man', 'gender': 'M'})
mcu_queue.arrive({'name': 'Wanda Maximoff', 'superhero': 'Scarlet Witch', 'gender': 'F'})

# a
def find_character_by_superhero(queue, superhero_name):
    temp_list = []
    character_name = None
    
    while queue.size() > 0:
        character = queue.attention()
        if character['superhero'] == superhero_name:
            character_name = character['name']
        temp_list.append(character)
    
    for character in temp_list:
        queue.arrive(character)
    
    return character_name

# b
def show_female_superheroes(queue):
    temp_list = []
    female_heroes = []
    
    while queue.size() > 0:
        character = queue.attention()
        if character['gender'] == 'F':
            female_heroes.append(character['superhero'])
        temp_list.append(character)
    
    for character in temp_list:
        queue.arrive(character)
    
    print("Superhéroes femeninos:", ", ".join(female_heroes))

# c
def show_male_characters(queue):
    temp_list = []
    male_characters = []
    
    while queue.size() > 0:
        character = queue.attention()
        if character['gender'] == 'M':
            male_characters.append(character['name'])
        temp_list.append(character)
    
    for character in temp_list:
        queue.arrive(character)
    
    print("Personajes masculinos:", ", ".join(male_characters))

# d
def find_superhero_by_character(queue, character_name):
    temp_list = []
    superhero_name = None
    
    while queue.size() > 0:
        character = queue.attention()
        if character['name'] == character_name:
            superhero_name = character['superhero']
        temp_list.append(character)
    
    for character in temp_list:
        queue.arrive(character)
    
    return superhero_name

# e
def show_characters_starting_with_s(queue):
    temp_list = []
    result = []
    
    while queue.size() > 0:
        character = queue.attention()
        if character['name'].startswith('S') or character['superhero'].startswith('S'):
            result.append(character)
        temp_list.append(character)
    
    for character in temp_list:
        queue.arrive(character)
    
    print("Personajes o superhéroes que empiezan con S:")
    for character in result:
        print(f"Nombre: {character['name']}, Superhéroe: {character['superhero']}, Género: {character['gender']}")

# f
def find_superhero_of_carol_danvers(queue):
    temp_list = []
    superhero_name = None
    
    while queue.size() > 0:
        character = queue.attention()
        if character['name'] == 'Carol Danvers':
            superhero_name = character['superhero']
        temp_list.append(character)
    
    for character in temp_list:
        queue.arrive(character)
    
    return superhero_name



# a
print(f"a. El nombre del personaje de Capitana Marvel es: {find_character_by_superhero(mcu_queue, 'Capitana Marvel')}")

# b
print("\nb. Los superhéroes femeninos son:")
show_female_superheroes(mcu_queue)

# c
print("\nc. Los personajes masculinos son:")
show_male_characters(mcu_queue)

# d
print(f"\nd. El superhéroe de Scott Lang es: {find_superhero_by_character(mcu_queue, 'Scott Lang')}")

# e
print("\ne. Personajes o superhéroes cuyos nombres empiezan con 'S':")
show_characters_starting_with_s(mcu_queue)

# f
print(f"\nf. Carol Danvers es: {find_superhero_of_carol_danvers(mcu_queue)}")