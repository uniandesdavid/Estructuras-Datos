import DataStructures.List.single_linked_list as lst
# import DataStructures.List.array_list as lst

def new_queue():
    """
    Crea una nueva cola vacía.

    Implementa una cola sobre alguna de las implementaciones de listas. Por ejemplo un array_list o una single_linked_list

    Returns: Una nueva cola vacía.
    Return type: queue
    """
    return lst.new_list()

def enqueue(my_queue, element):
    """
    Agrega un elemento al final de la cola.

    Parameters:

        my_queue (queue) – La cola a la que se le agregará el elemento.

        element (any) – El elemento que se agregará a la cola.

    Returns: La cola con el elemento agregado.
    Return type: queue
    """
    return lst.add_last(my_queue, element)

def dequeue(my_queue):
    """
    Elimina y retorna el primer elemento de la cola.

    Si la cola está vacía, lanza un error: EmptyStructureError: queue is empty.
    
    Parameters:
        my_queue (queue) – La cola de la que se eliminará el primer elemento.
    
    Returns: Elemento retirado de la cola.
    Return type: any
    """
    return lst.remove_first(my_queue)

def peek(my_queue):
    """
    Retorna el primer elemento de la cola sin eliminarlo.

    Si la cola está vacía, lanza un error: EmptyStructureError: queue is empty.

    Parameters:
        my_queue (queue) – La cola de la que se retornará el primer elemento.
    
    Returns: Primer elemento de la cola.
    Return type: any
    """
    return lst.get_element(my_queue, 0)

def is_empty(my_queue):
    """
    Verifica si la cola está vacía.

    Parameters:
        my_queue (queue) – La cola que se verificará si está vacía.
    
    Returns: True si la cola está vacía, de lo contrario False.
    Return type: bool
    """
    return lst.is_empty(my_queue)

def size(my_queue):
    """
    Retorna el tamaño de la cola.

    Parameters:
        my_queue (queue) – La cola de la que se retornará el tamaño.
    
    Returns: Tamaño de la cola.
    Return type: int
    """
    return lst.size(my_queue)