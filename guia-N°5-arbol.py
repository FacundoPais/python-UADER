class BinaryTree:

    class __Node:
        def __init__(self, value, left=None, right=None, other_value=None):
            self.value = value
            self.left = left
            self.right = right
            self.other_value = other_value

    def __init__(self):
        self.root = None

    def insert_node(self, value, other_value=None):
        def __insert(root, value, other_value=None):
            if root is None:
                return BinaryTree.__Node(value, other_value=other_value)
            elif value < root.value:
                root.left = __insert(root.left, value, other_value)
            else:
                root.right = __insert(root.right, value, other_value)
            return root

        self.root = __insert(self.root, value, other_value)

    def search(self, key):
        def __search(root, key):
            if root is not None:
                if root.value == key:
                    return root
                elif key < root.value:
                    return __search(root.left, key)
                else:
                    return __search(root.right, key)
            return None
        return __search(self.root, key)

    def preorden(self):
        def __preorden(root):
            if root is not None:
                print(root.value)
                __preorden(root.left)
                __preorden(root.right)

        __preorden(self.root)

    def contar_super_heroes(self):
        def __contar_super_heroes(root):
            if root is None:
                return 0
            count = 1 if root.other_value.get('is_hero') else 0
            count += __contar_super_heroes(root.left)
            count += __contar_super_heroes(root.right)
            return count

        return __contar_super_heroes(self.root)

    def inorden(self):
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                print(root.value)
                __inorden(root.right)

        __inorden(self.root)

    def inorden_villanos(self):
        def __inorden_villanos(root):
            if root is not None:
                __inorden_villanos(root.left)
                if root.other_value.get('is_hero') is False:
                    print(root.value)
                __inorden_villanos(root.right)

        __inorden_villanos(self.root)

    def inorden_superheros_start_with(self, start):
        def __inorden_superheros_start_with(root, start):
            if root is not None:
                __inorden_superheros_start_with(root.left, start)
                if root.other_value.get('is_hero') is True and root.value.startswith(start):
                    print(root.value)
                __inorden_superheros_start_with(root.right, start)

        __inorden_superheros_start_with(self.root, start)

    def postorden(self):
        def __postorden(root):
            if root is not None:
                __postorden(root.right)
                print(root.value)
                __postorden(root.left)

        __postorden(self.root)

    def delete_node(self, value):
        def __replace(root):
            if root.right is None:
                return root.left, root
            else:
                root.right, replace_node = __replace(root.right)
                return root, replace_node

        def __delete(root, value):
            if root is not None:
                if root.value > value:
                    root.left, deleted_node = __delete(root.left, value)
                elif root.value < value:
                    root.right, deleted_node = __delete(root.right, value)
                else:
                    if root.left is None:
                        return root.right, root
                    elif root.right is None:
                        return root.left, root
                    else:
                        root.left, replace_node = __replace(root.left)
                        root.value = replace_node.value
                        return root, root
            return root, None

        self.root, deleted_value = __delete(self.root, value)
        return deleted_value

    def update_name(self, old_name, new_name):
        def __update_name(root):
            if root is not None:
                if root.value == old_name:
                    root.value = new_name
                __update_name(root.left)
                __update_name(root.right)

        __update_name(self.root)

    def create_hero_villain_forest(self):
        hero_tree = BinaryTree()
        villain_tree = BinaryTree()

        def __create_forest(root):
            if root is not None:
                if root.other_value.get('is_hero'):
                    hero_tree.insert_node(root.value, root.other_value)
                else:
                    villain_tree.insert_node(root.value, root.other_value)
                __create_forest(root.left)
                __create_forest(root.right)

        __create_forest(self.root)
        return hero_tree, villain_tree


mcu_tree = BinaryTree()

mcu_tree.insert_node("Iron Man", {'is_hero': True})
mcu_tree.insert_node("Doctor Strange", {'is_hero': True})
mcu_tree.insert_node("Hawkeye", {'is_hero': True})
mcu_tree.insert_node("Thanos", {'is_hero': False})
mcu_tree.insert_node("Loki", {'is_hero': False})
mcu_tree.insert_node("Hera Syndulla", {'is_hero': False})

# a) 
print("Villanos:")
mcu_tree.inorden_villanos()

# b) 
print("\nSuperhéroes que empiezan con 'C':")
mcu_tree.inorden_superheros_start_with('C')

# c)
count_heroes = mcu_tree.contar_super_heroes()
print(f"\nCantidad de superhéroes: {count_heroes}")

# d)
mcu_tree.update_name("Doctor Strange", "Doctor Strange (Revisado)")

# e)
print("\nSuperhéroes ordenados de manera descendente:")
mcu_tree.postorden()

# f) 
hero_tree, villain_tree = mcu_tree.create_hero_villain_forest()

# g)
print(f"\nCantidad de superhéroes en el bosque: {hero_tree.contar_super_heroes()}")
print("Superhéroes en orden alfabético:")
hero_tree.inorden()

print(f"\nCantidad de villanos en el bosque: {villain_tree.contar_super_heroes()}")
print("Villanos en orden alfabético:")
villain_tree.inorden()
