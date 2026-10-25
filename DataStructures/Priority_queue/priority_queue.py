from DataStructures.Priority_queue import pq_entry
from DataStructures.List import array_list


def new_heap(is_min_pq=True):
    """
    Crea un cola de prioridad indexada orientada a menor o mayor dependiendo del valor de is_min_pq

    Se crea una cola de prioridad con los siguientes atributos:

        elements: Lista de elementos. Se inicializa como una lista vacia de tipo array_list.

        size: Tamaño de la cola de prioridad. Se inicializa en 0.

        cmp_function: La funcion de comparacion. Si es una cola de prioridad orientada a menor is_min_pq = True, se inicializa con la funcion default_compare_lower_value. Si es una cola de prioridad orientada a mayor is_min_pq = False, se inicializa con la funcion default_compare_higher_value.

    Al crear la cola de prioridad, se agrega un elemento None en la posición 0 de la lista de elementos. Esto es útil para poder utilizar la propiedad de los heaps, donde el padre de un nodo en la posición i se encuentra en la posición i//2, y los hijos se encuentran en las posiciones 2*i y 2*i + 1.

    Parameters:

        is_min_pq (bool) – Indica si la cola de prioridad es orientada a menor o mayor. Por defecto es True.

    Returns: Una nueva cola de prioridad indexada
    Return type: priority_queue
    """
    elements = array_list.new_list()
    array_list.add_last(elements, None)

    cmp_function = default_compare_lower_value
    if not is_min_pq:
        cmp_function = default_compare_higher_value

    return {"elements": elements, "size": 0, "cmp_function": cmp_function}


def default_compare_higher_value(father_node, child_node):
    """
    Función de comparación por defecto para el heap orientado a mayor.

    Compara la prioridad priority de los nodos father_node y child_node. Si el nodo padre tiene mayor o igual prioridad que el nodo hijo, retorna True. En caso contrario, retorna False.

    Parameters:

        father_node (pq_entry) – El nodo padre

        child_node (pq_entry) – El nodo hijo

    Returns: True si el nodo padre tiene mayor prioridad que el nodo hijo. False en caso contrario.
    Return type: bool
    """
    return pq_entry.get_priority(father_node) >= pq_entry.get_priority(child_node)


def default_compare_lower_value(father_node, child_node):
    """
    Función de comparación por defecto para el heap orientado a menor.

    Compara la prioridad priority de los nodos father_node y child_node. Si el nodo padre tiene menor o igual prioridad que el nodo hijo, retorna True. En caso contrario, retorna False.

    Parameters:

            father_node (pq_entry) – El nodo padre

            child_node (pq_entry) – El nodo hijo

    Returns: True si el nodo padre tiene menor prioridad que el nodo hijo. False en caso contrario.
    Return type: bool
    """
    return pq_entry.get_priority(father_node) <= pq_entry.get_priority(child_node)


def priority(my_heap, parent, child):
    """
    Indica si el parent tiene mayor prioridad que child.

    Parameters:

        my_heap (priority_queue) – El heap a revisar

        parent (any) – El elemento padre

        child (any) – El elemento hijo a comparar

    Returns: True si el parent tiene mayor prioridad que el child. False en caso contrario.
    Return type: bool
    """

    return my_heap["cmp_function"](parent, child)


def insert(my_heap, priority, value):
    """
    Agrega una nueva entrada prioridad-valor al heap. Inserta la prioridad priority con valor value en el heap al final de la lista de elementos y luego se hace swim para dejar el elemento en la posición correcta.

    Importante

    Esta función usa la función swim() para dejar el elemento en la posición correcta.

    Parameters:

        my_heap (priority_queue) – El heap sobre el cual se realiza la operación

        priority (int) – La prioridad a insertar

        value (any) – El valor de la nueva entrada

    Returns: El heap con la nueva entrada insertada
    Return type: Priority_queue
    """
    nodo = pq_entry.new_pq_entry(priority, value)

    my_heap["elements"] = array_list.add_last(my_heap["elements"], nodo)
    my_heap["size"] = size(my_heap) + 1

    return swim(my_heap, size(my_heap))




def swim(my_heap, pos):
    """
    Deja en la posición correcta un elemento ubicado en la última posición del heap

    Se realiza un recorrido hacia arriba en el heap, comparando el elemento con su padre. Si el elemento tiene mayor prioridad que su padre, se intercambian los elementos y se continúa el recorrido hacia arriba.

    Nota

    Esta función es utilizada por la función insert() para dejar el elemento en la posición correcta.

    Parameters:

        my_heap (priority_queue) – El heap sobre el cual se realiza la operación

        pos (int) – La posición del elemento a revisar
    """
    position = pos

    while position > 1 and not priority(my_heap, array_list.get_element(my_heap["elements"], position//2), array_list.get_element(my_heap["elements"], position)):
        parent = position // 2
        array_list.exchange(my_heap["elements"], parent, position)

        position = parent

    return my_heap



def size(my_heap):
    """
    Obtiene el número de elementos en el heap.

    Parameters:

        my_heap (priority_queue) – El heap del cual se quiere saber la cantidad de elementos

    Returns: El número de elementos
    Return type: int
    """
    return my_heap["size"]




def is_empty(my_heap):
    """
    Verifica si la cola de prioridad está vacía.

    Retorna True si el heap está vacío, False en caso contrario. Si el heap tiene un tamaño de 0, se considera vacío.

    Parameters:

        my_heap (priority_queue) – El heap del cual se quiere saber si está vacío

    Returns: True si el heap está vacío, False en caso contrario.
    Return type: bool
    """
    return size(my_heap) == 0


def get_first_priority(my_heap):
    """
    Obtiene el elemento de mayor prioridad del heap sin eliminarlo.

    Retorna el primer elemento del heap, es decir el elemento con mayor prioridad sin eliminarlo.

    Parameters:

        my_heap (priority_queue) – El heap del cual se quiere obtener el primer elemento

    Returns: El value asociada elemento de mayor prioridad. Si el heap está vacío, retorna None.
    Return type: any
    """
    if is_empty(my_heap):
        return None
    
    return pq_entry.get_value(array_list.get_element(my_heap["elements"], 1))



def remove(my_heap):
    """
    Retorna el elemento del heap de mayor prioridad y lo elimina. Se reemplaza el primer elemento del heap por el último elemento y se hace sink para dejar el elemento en la posición correcta.

    Importante

    Esta función usa la función sink() para dejar el elemento en la posición correcta.

    Parameters:

        my_heap (priority_queue) – El heap a revisar

    Returns: value del elemento de mayor prioridad. Si el heap está vacío, retorna None.
    Return type: any
    """
    if is_empty(my_heap):
        return None
    
    my_heap["elements"] = array_list.exchange(my_heap["elements"], 1, size(my_heap))
    eliminado = array_list.remove_last(my_heap["elements"])
    my_heap["size"] = my_heap["size"] - 1

    sink(my_heap, 1)

    return pq_entry.get_value(eliminado)
    


def sink(my_heap, pos):
    """
    Deja en la posición correcta un elemento ubicado en la raíz del heap

    Se realiza un recorrido hacia abajo en el heap, comparando el elemento con sus hijos. Si el elemento tiene menor prioridad que alguno de sus hijos, se intercambian los elementos y se continúa el recorrido hacia abajo.

    Nota

    Esta función es utilizada por la función remove() para dejar el elemento en la posición correcta.

    Parameters:

        my_heap (priority_queue) – El heap sobre el cual se realiza la operación

        pos (int) – La posición del elemento a revisar
    """
    position = pos
    hijo_1 = 2*position
    hijo_2 = 2*position + 1

    puede_bajar = True

    while hijo_1 <= size(my_heap) and puede_bajar:
        maximo = hijo_1
        if(hijo_2 <= size(my_heap)):
            if (priority(my_heap, array_list.get_element(my_heap["elements"], hijo_2),array_list.get_element(my_heap["elements"], hijo_1))):
                maximo = hijo_2

        if (priority(my_heap, array_list.get_element(my_heap["elements"], position), array_list.get_element(my_heap["elements"], maximo))):
            puede_bajar = False
        else:
            my_heap["elements"] = array_list.exchange(my_heap["elements"], position, maximo)
            position = maximo
            hijo_1 = 2*position
            hijo_2 = 2*position + 1
        
    return my_heap


def is_present_value(my_heap, value):
    """
    Busca si ya existe una entrada en el heap cuyo valor sea el value. Si existe se retorna la posición de la entrada que contiene el value. Si No existe se retorna el valor -1.

    Parameters:

        my_heap (priority_queue) – El heap a revisar

        value (any) – La parte valor de la entrada del heap que se esta buscando

    Returns: Posición de la entrada si value está presente, -1 en caso contrario.
    Return type: int
    """
    pos = -1
    no_encontrado = True

    contador = 1
    while contador <= size(my_heap) and no_encontrado:
        if (value == pq_entry.get_value(array_list.get_element(my_heap["elements"], contador))):
            no_encontrado = False
            pos = contador

        contador += 1
    
    return pos
         


def contains(my_heap, value):
    """
    Busca si ya existe una entrada en el heap cuyo valor sea el value. Si existe se retorna True. En caso contrario, False.

    Parameters:

        my_heap (priority_queue) – El heap a revisar

        value (any) – La parte valor de la entrada del heap que se esta buscando

    Returns: True/False.
    Return type: bool
    """
    return is_present_value(my_heap, value) != -1



def improve_priority(my_heap, priority, value):
    """
    Mejorar la prioridad de la pq_entry que tenga el value dado. Funciona para MinPQ y MaxPQ.

    Parameters:

        my_heap (priority_queue) – El heap a revisar

        priority (int) – La nueva prioridad de la pq_entry del heap. Esta prioridad debe ser mejor que la actual.

        value (any) – El value de referencia de la pq_entry del heap que se quiere actualizar

    Returns: El heap con la nueva pq_entry actualizada
    Return type: priority_queue
    """
    pos = is_present_value(my_heap, value)

    if pos == -1:
        return my_heap
    
    pq_entry.set_priority(array_list.get_element(my_heap["elements"], pos), priority)

    return swim(my_heap, pos)
