import DataStructures.List.single_linked_list as lt
# import DataStructures.List.array_list as lt


def new_stack():
    """
    Crea una pila vacía
    """
    return lt.new_list()

def is_empty(stack):
    """
    Indica si la pila está vacía
    """
    return lt.is_empty(stack)

def push(stack, element):
    """
    Agrega un elemento a la pila
    """
    return lt.add_first(stack, element)

def pop(stack):
    """
    Elimina y retorna el elemento en la cima de la pila
    """
    return lt.remove_first(stack)

def top(stack):
    """
    Retorna el elemento en la cima de la pila sin eliminarlo
    """
    
    return lt.get_element(stack, 0)

def size(stack):
    """
    Retorna el número de elementos en la pila
    """
    return lt.size(stack)