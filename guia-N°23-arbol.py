class CreatureTree:

    class __Node:
        def __init__(self, name, defeated_by=None, description=None, captured_by=None):
            self.name = name
            self.defeated_by = defeated_by  
            self.description = description  
            self.captured_by = captured_by   
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert_node(self, name, defeated_by=None, description=None, captured_by=None):
        def __insert(root, name, defeated_by, description, captured_by):
            if root is None:
                return CreatureTree.__Node(name, defeated_by, description, captured_by)
            elif name < root.name:
                root.left = __insert(root.left, name, defeated_by, description, captured_by)
            else:
                root.right = __insert(root.right, name, defeated_by, description, captured_by)
            return root

        self.root = __insert(self.root, name, defeated_by, description, captured_by)

    def inorden(self):
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                print(f"Creature: {root.name}, Defeated by: {root.defeated_by}, Description: {root.description}, Captured by: {root.captured_by}")
                __inorden(root.right)

        __inorden(self.root)

    def search(self, name):
        def __search(root, name):
            if root is None:
                return None
            if root.name == name:
                return root
            elif name < root.name:
                return __search(root.left, name)
            else:
                return __search(root.right)

        return __search(self.root, name)

    def list_captured_by_heracles(self):
        def __list_captured_by_heracles(root):
            if root is not None:
                __list_captured_by_heracles(root.left)
                if root.captured_by == "Heracles":
                    print(root.name)
                __list_captured_by_heracles(root.right)

        __list_captured_by_heracles(self.root)

    def delete_node(self, name):
        def __replace(root):
            if root.right is None:
                return root.left, root
            else:
                root.right, replace_node = __replace(root.right)
                return root, replace_node

        def __delete(root, name):
            if root is None:
                return None
            if name < root.name:
                root.left = __delete(root.left, name)
            elif name > root.name:
                root.right = __delete(root.right, name)
            else:
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left
                else:
                    root.left, replace_node = __replace(root.left)
                    root.name = replace_node.name
                    root.defeated_by = replace_node.defeated_by
                    root.description = replace_node.description
                    root.captured_by = replace_node.captured_by
            return root

        self.root = __delete(self.root, name)

    def modify_creature(self, old_name, new_name, new_defeated_by=None):
        creature = self.search(old_name)
        if creature:
            creature.name = new_name
            if new_defeated_by:
                creature.defeated_by = new_defeated_by

    def list_defeated_by_heracles(self):
        def __list_defeated_by_heracles(root):
            if root is not None:
                __list_defeated_by_heracles(root.left)
                if root.defeated_by == "Heracles":
                    print(root.name)
                __list_defeated_by_heracles(root.right)

        __list_defeated_by_heracles(self.root)

    def search_by_partial(self, partial_name):
        results = []

        def __search_by_partial(root, partial_name):
            if root is not None:
                if partial_name in root.name:
                    results.append(root.name)
                __search_by_partial(root.left, partial_name)
                __search_by_partial(root.right, partial_name)

        __search_by_partial(self.root, partial_name)
        return results

    def get_top_defeaters(self, top_n=3):
        defeat_count = {}

        def __count_defeaters(root):
            if root is not None:
                if root.defeated_by:
                    if root.defeated_by in defeat_count:
                        defeat_count[root.defeated_by] += 1
                    else:
                        defeat_count[root.defeated_by] = 1
                __count_defeaters(root.left)
                __count_defeaters(root.right)

        __count_defeaters(self.root)
        sorted_defeaters = sorted(defeat_count.items(), key=lambda x: x[1], reverse=True)
        return sorted_defeaters[:top_n]


creature_tree = CreatureTree()

creature_tree.insert_node("Ceto", defeated_by="Teseo")
creature_tree.insert_node("Tifón", defeated_by="Zeus")
creature_tree.insert_node("Equidna", defeated_by=None)
creature_tree.insert_node("Cerda de Cromión", defeated_by="Teseo")
creature_tree.insert_node("Dino", defeated_by=None)
creature_tree.insert_node("Jabalí de Calidón", defeated_by="Atalanta")
creature_tree.insert_node("Enio", defeated_by="Heracles")
creature_tree.insert_node("Gerión", defeated_by="Heracles")
creature_tree.insert_node("Escila", defeated_by=None)
creature_tree.insert_node("Cloto", defeated_by=None)
creature_tree.insert_node("Caribdis", defeated_by=None)
creature_tree.insert_node("Euríale", defeated_by=None)
creature_tree.insert_node("Átropos", defeated_by=None)
creature_tree.insert_node("Esteno", defeated_by=None)
creature_tree.insert_node("Medusa", defeated_by="Perseo")
creature_tree.insert_node("Hidra de Lerna", defeated_by="Heracles")
creature_tree.insert_node("León de Nemea", defeated_by="Heracles")
creature_tree.insert_node("Esfinge", defeated_by="Edipo")
creature_tree.insert_node("Dragón de la Cólquida", defeated_by=None)
creature_tree.insert_node("Basilisco", defeated_by=None)
creature_tree.insert_node("Cerbero", defeated_by=None)
creature_tree.insert_node("Jabalí de Erimanto", defeated_by=None)
creature_tree.insert_node("Talos", defeated_by="Medea")
creature_tree.insert_node("Quimera", defeated_by="Belerofonte")
creature_tree.insert_node("Argos Panoptes", defeated_by="Hermes")
creature_tree.insert_node("Aves del Estínfalo", defeated_by=None)

# b) 
print("Listado inorden de las criaturas:")
creature_tree.inorden()

# c) 
talos_node = creature_tree.search("Talos")
if talos_node:
    talos_node.description = "Talos es un autómata de bronce que protege a Creta."

# d)
print("\nInformación de Talos:")
if talos_node:
    print(f"Creature: {talos_node.name}, Defeated by: {talos_node.defeated_by}, Description: {talos_node.description}")

# e) 
top_defeaters = creature_tree.get_top_defeaters()
print("\nTop 3 héroes o dioses que derrotaron mayor cantidad de criaturas:")
for name, count in top_defeaters:
    print(f"{name}: {count} criaturas derrotadas")

# f)
print("\nCriaturas derrotadas por Heracles:")
creature_tree.list_defeated_by_heracles()

# g) 
print("\nCriaturas que no han sido derrotadas:")
creature_tree.inorden()

# h) 
creature_tree.modify_creature("Cerbero", "Cerbero", captured_by="Heracles")
creature_tree.modify_creature("Toro de Creta", "Toro de Creta", captured_by="Heracles")
creature_tree.modify_creature("Cierva de Cerinea", "Cierva de Cerinea", captured_by="Heracles")
creature_tree.modify_creature("Jabalí de Erimanto", "Jabalí de Erimanto", captured_by="Heracles")

# i) 
print("\nCriaturas capturadas por Heracles:")
creature_tree.list_captured_by_heracles()

# j) 
creature_tree.delete_node("Basilisco")
creature_tree.delete_node("Sirenas")

# k) 
creature_tree.modify_creature("Aves del Estínfalo", "Aves del Estínfalo", defeated_by="Heracles")

# l) 
creature_tree.modify_creature("Ladón", "Dragón Ladón")

# m)
def list_by_level(root):
    if not root:
        return

    level = 0
    current_level_nodes = [root]
    while current_level_nodes:
        print(f"\nNivel {level}: ", end="")
        next_level_nodes = []
        for node in current_level_nodes:
            print(node.name, end=" ")
            if node.left:
                next_level_nodes.append(node.left)
            if node.right:
                next_level_nodes.append(node.right)
        current_level_nodes = next_level_nodes
        level += 1

list_by_level(creature_tree.root)

# n)
print("\nCriaturas capturadas por Heracles:")
creature_tree.list_captured_by_heracles()
