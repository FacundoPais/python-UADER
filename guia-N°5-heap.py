class HeapMax():
    def __init__(self):
        self.elements = []
    
    def add(self, value, priority):
        self.elements.append((priority, value))
        self.float(len(self.elements) - 1)

    def remove(self):
        if len(self.elements) > 0:
            self.interchange(0, len(self.elements) - 1)
            value = self.elements.pop()
            self.sink(0)
            return value
        else:
            return None

    def interchange(self, index_1, index_2):
        self.elements[index_1], self.elements[index_2] = self.elements[index_2], self.elements[index_1]

    def float(self, index):
        father = (index - 1) // 2
        while index > 0 and self.elements[index][0] > self.elements[father][0]:
            self.interchange(index, father)
            index = father
            father = (index - 1) // 2

    def sink(self, index):
        left_child = (index * 2) + 1
        control = True
        while control and left_child < len(self.elements):
            right_child = (index * 2) + 2
            max = left_child
            if right_child < len(self.elements):
                if self.elements[right_child][0] > self.elements[left_child][0]:
                    max = right_child
            if self.elements[index][0] < self.elements[max][0]:
                self.interchange(index, max)
                index = max
                left_child = (index * 2) + 1
            else:
                control = False

class Stack():
    def __init__(self):
        self.elements = []
    
    def push(self, value):
        self.elements.append(value)
    
    def pop(self):
        if len(self.elements) > 0:
            return self.elements.pop()
        else:
            return None

    def top(self):
        if len(self.elements) > 0:
            return self.elements[-1]
        else:
            return None


def determine_priority(request):
    general = request['general']
    planet = request['planet']
    description = request['description']

    if general == "Gran Inquisidor" or planet == "Lothal" or "Hera Syndulla" in description:
        return 3  
    elif general == "Agente Kallus" or "Destructor Estelar" in description or "AT-AT" in description:
        return 2  
    else:
        return 1  


help_requests = HeapMax()


log_stack = Stack()


requests = [
    {'general': 'Gran Inquisidor', 'planet': 'Lothal', 'description': 'Ataque rebelde cercano'},
    {'general': 'Agente Kallus', 'planet': 'Coruscant', 'description': 'Despliegue de Destructor Estelar'},
    {'general': 'General Hux', 'planet': 'Endor', 'description': 'Defensa rebelde en el sistema'},
    {'general': 'General Veers', 'planet': 'Hoth', 'description': 'Movilización de AT-AT'},
    {'general': 'General Hux', 'planet': 'Jakku', 'description': 'Intervención rebelde'},
]

# 1
for request in requests:
    priority = determine_priority(request)
    help_requests.add(request, priority)

# 2
while help_requests.elements:
    attended_request = help_requests.remove()
    priority, request = attended_request
    print(f"Atendiendo pedido de {request['general']} en {request['planet']} - Prioridad: {priority}")
    
    log_stack.push(attended_request)

    new_request = {'general': 'Agente Kallus', 'planet': 'Scarif', 'description': 'Despliegue de Destructor Estelar'}
    priority = determine_priority(new_request)
    help_requests.add(new_request, priority)

# 3
print("\nPedidos atendidos (bitácora):")
while log_stack.elements:
    priority, request = log_stack.pop()
    print(f"General: {request['general']}, Planeta: {request['planet']}, Descripción: {request['description']}, Prioridad: {priority}")
