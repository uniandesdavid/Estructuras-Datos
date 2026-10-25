from . import list_node as list_node

def new_list():
    newlist = {
        "first": None,
        "last": None,
        "size": 0
    }
    return newlist

def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1

    return node["info"]

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1

    if not is_in_array:
        count = -1

    return count

def is_empty(my_list):
    """
    Verifica si la lista está vacía.

    Retorna True si la lista está vacía, en caso contrario retorna False.

    Parameters:
        my_list (single_linked_list) – Lista a verificar.
    
    Returns: True si la lista está vacía, False en caso contrario.
    Return type: bool
    """
    return size(my_list) == 0

def add_first(my_list, element):
    """
    Agrega un elemento al inicio de la lista.

    Agrega un nuevo nodo al inicio de la lista y aumenta el tamaño de la lista en 1. En caso de que la lista esté vacía, el primer y último nodo de la lista serán el nuevo nodo.

    Parameters:

            my_list (single_linked_list) – Lista a la cual se agregará el elemento.

            element (any) – Elemento a agregar.

    Returns: Lista con el elemento agregado al inicio.
    Return type: single_linked_list
    """
    # EST-3
    nodo = list_node.new_single_node(element)

    if (my_list["size"] == 0):
        my_list["first"] = nodo 
        my_list["last"] = nodo
    else:
        nodo["next"] = my_list["first"]
        my_list["first"] = nodo

    my_list["size"] += 1
    return my_list

def add_last(my_list, element):
    """
    Agrega un elemento al final de la lista.

    Agrega un nuevo nodo al final de la lista y aumenta el tamaño de la lista en 1. En caso de que la lista esté vacía, el primer y último nodo de la lista serán el nuevo nodo.

    Parameters:

        my_list (single_linked_list) – Lista a la cual se agregará el elemento.

        element (any) – Elemento a agregar.

    Returns: Lista con el elemento agregado al final.
    Return type: single_linked_list
    """
    # EST-3
    nodo = list_node.new_single_node(element)

    if (my_list["size"] == 0):
        my_list["first"] = nodo
        my_list["last"] = nodo
    else:
        my_list["last"]["next"] = nodo
        my_list["last"] = nodo

    my_list["size"] += 1
    return my_list

def size(my_list):
    """
    Retorna el tamaño de la lista.

    Parameters:
        my_list (single_linked_list) – Lista de la cual se obtendrá el tamaño.
    Returns: Tamaño de la lista.
    Return type: int
    """
    return my_list["size"]

def first_element(my_list):
    """
    Retorna el primer elemento de una lista no vacía.

    Retorna el primer elemento de la lista. 
    Si la lista está vacía, lanza un error IndexError: list index out of range. 
    Esta función no elimina el elemento de la lista

    Parameters:

        my_list (single_linked_list) – Lista de la cual se obtendrá el primer elemento.
    
    Returns: Primer elemento de la lista.
    Return type: any

    """
    # EST-3
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        return my_list["first"]
    
def last_element(my_list):
    """
    Retorna el último elemento de una lista no vacía.

    Retorna el último elemento de la lista. Si la lista está vacía, lanza un error IndexError: list index out of range. Esta función no elimina el elemento de la lista.
    
    Parameters:
        my_list (single_linked_list) – Lista de la cual se obtendrá el último elemento.

    Returns: Último elemento de la lista.
    Return type: any
    """
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        return my_list["last"]

def delete_element(my_list, pos):
    """
    Elimina un elemento en la posición dada.

    Elimina el elemento en la posición pos, la cual debe ser igual o mayor a cero y menor al tamaño de la lista. 0 <= pos < size(my_list) Si la posición no es válida, lanza un error IndexError: list index out of range.
    
    Parameters:
        my_list (single_linked_list) – Lista de la cual se eliminará el elemento.

        pos (int) – Posición del elemento a eliminar.

    Returns: Lista con el elemento eliminado.
    Return type: single_linked_list
    """
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')
    
    if (size(my_list) == 1):
        my_list["first"] = None
        my_list["last"] = None

        my_list["size"] -= 1
        return my_list
    
    if (pos == 0):
        remove_first(my_list)

    elif (pos == size(my_list) - 1):
        remove_last(my_list)

    else:
        indice = 0
        prev_nodo = my_list["first"]
        while indice < size(my_list) - 1:
            prev_nodo = prev_nodo["next"]
            indice += 1

        prev_nodo["next"] = prev_nodo["next"]["next"]

    return my_list



def remove_first(my_list):
    """
    Elimina el primer elemento de la lista.

    Elimina el primer elemento de la lista y disminuye el tamaño de la lista en 1. Si la lista está vacía, lanza un error IndexError: list index out of range.

    Parameters:
        my_list (single_linked_list) – Lista de la cual se eliminará el primer elemento.
    
    Returns: Element eliminado de la lista.
    Return type: any
    """
    if size(my_list) == 0:
        raise Exception("IndexError: list index out of range.")

    eliminado = my_list["first"]["info"]
    my_list["first"] = my_list["first"]["next"]
    my_list["size"] -= 1
    
    if size(my_list) < 1:
        my_list["last"] == None
    
    return eliminado
    

def remove_last(my_list):
    """
    Elimina el último elemento de la lista.

    Elimina el último elemento de la lista y disminuye el tamaño de la lista en 1. Si la lista está vacía, lanza un error IndexError: list index out of range.

    Parameters:
        my_list (single_linked_list) – Lista de la cual se eliminará el último elemento.
    
    Returns: Element eliminado de la lista.
    Return type: any
    """
    if size(my_list) == 0:
        raise Exception('IndexError: list index out of range')
    
    eliminado = my_list["last"]["info"]

    if (size(my_list) == 1):
        my_list["first"] == None
        my_list["last"] == None

        my_list["size"] -= 1
        return eliminado

    indice = 0
    nodo_prev = my_list["first"]
    while (indice < size(my_list) - 1):
        nodo_prev = nodo_prev["next"]
        indice += 1

    nodo_prev["next"] = None
    my_list["size"] -= 1

    return eliminado


def insert_element(my_list, element, pos):
    """
    Inserta un elemento en la posición dada.

    Inserta el elemento en la posición pos, la cual debe ser igual o mayor a cero y menor o igual al tamaño de la lista. 0 <= pos <= size(my_list). Se incrementa el tamaño de la lista en 1.
    
    Parameters:

        my_list (single_linked_list) – Lista en la cual se insertará el elemento.

        element (any) – Elemento a insertar.

        pos (int) – Posición en la cual se insertará el elemento.

    Returns: Lista con el elemento insertado.
    Return type: single_linked_list
    """
    nodo = list_node.new_single_node(element)

    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')

    if (pos == 0):
        return add_first(my_list, element)
        
    elif (pos == my_list["size"]):
        return add_last(my_list, element)

    else:
        prev_nodo = my_list["first"]
        
        indice = 0

        while indice < pos - 1:
            prev_nodo = prev_nodo["next"]
            indice += 1
        
        nodo["next"] = prev_nodo["next"]
        prev_nodo["next"] = nodo
        
        my_list["size"] += 1
        return my_list


def change_info(my_list, pos, new_info):
    """
    Cambia la información de un elemento en la posición dada.

    Cambia la información del elemento en la posición pos por la información new_info. Si la posición no es válida, lanza un error IndexError: list index out of range.

    Parameters:

        my_list (single_linked_list) – Lista en la cual se cambiará la información del elemento.

        pos (int) – Posición del elemento a cambiar.

        new_info (any) – Nueva información del elemento.

    Returns: Lista con la información del elemento cambiada.
    Return type: single_linked_list
    """
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')
    
    if (pos == size(my_list) - 1):
        my_list["last"]["info"] = new_info
        return my_list

    indice = 0
    actual_nodo = my_list["first"]

    while (indice < pos):
        actual_nodo = actual_nodo["next"]
        indice += 1

    actual_nodo["info"] = new_info

    return my_list
    
def exchange(my_list, pos_1, pos_2):
    """
    Intercambia la posición de dos elementos.

    Intercambia la posición de los elementos en las posiciones pos_1 y pos_2. Si alguna de las posiciones no es válida, lanza un error IndexError: list index out of range.

    Parameters:

        my_list (single_linked_list) – Lista en la cual se intercambiarán los elementos.

        pos_1 (int) – Posición del primer elemento a intercambiar.

        pos_2 (int) – Posición del segundo elemento a intercambiar.

    Returns: Lista con los elementos intercambiados.
    Return type: single_linked_list
    """
    if pos_1 < 0 or pos_1 >= size(my_list) or pos_2 < 0 or pos_2 >= size(my_list):
        raise Exception('IndexError: list index out of range')

    if (pos_1 == pos_2):
        return my_list

    if pos_1 > pos_2:
        pos_1, pos_2 = pos_2, pos_1

    nodo_1 = my_list["first"]
    for _ in range(pos_1):
        nodo_1 = nodo_1["next"]

    nodo_2 = nodo_1
    for _ in range(pos_2 - pos_1):
        nodo_2 = nodo_2["next"]

    nodo_1["info"], nodo_2["info"] = nodo_2["info"], nodo_1["info"]
    return my_list


def sub_list(my_list, pos, num_elements):
    """
    Retorna una sublista de la lista original.

    Retorna una sublista de la lista original que contiene num_elements elementos a partir de la posición pos. Si la posición no es válida, lanza un error IndexError: list index out of range.

    Parameters:

        my_list (single_linked_list) – Lista de la cual se obtendrá la sublista.

        pos (int) – Posición inicial de la sublista.

        num_elements (int) – Número de elementos de la sublista.

    Returns: Sublista de la lista original.
    Return type: single_linked_list
    """
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')
    
    nueva_lista = new_list()

    if num_elements <= 0:
        return nueva_lista

    indice = 0
    nodo = my_list["first"]

    while indice < pos:
        nodo = nodo["next"]
        indice += 1

    count = 0
    while nodo is not None and count < num_elements:
        add_last(nueva_lista, nodo["info"])
        nodo = nodo["next"]
        count += 1

    return nueva_lista

def default_sort_criteria(element1, element2):
    """
    Función de comparación por defecto para ordenar elementos.

    Compara dos elementos y retorna True si el primer elemento es menor que el segundo y False en caso contrario.
    
    Parameters:

        element_1 (any) – Primer elemento a comparar.

        element_2 (any) – Segundo elemento a comparar.

    Returns: True si el primer elemento es menor que el segundo, False en caso contrario.
    Return type: bool
    """
    if element1 < element2:
        return True
    else:
        return False

def selection_sort(my_list, sort_crit):
    """
    Ordena una lista utilizando el algoritmo de ordenamiento Selecion Sort.

    Se recorre la lista y se selecciona el elemento más pequeño y se intercambia con el primer elemento. Luego se selecciona el segundo elemento más pequeño y se intercambia con el segundo elemento, y así sucesivamente.
    
    Parameters:

        my_list (array_list o single_linked_list) – Lista a ordenar.

        sort_crit (function) – Función de comparación.

    Returns: Lista ordenada.
    Return type: array_list o single_linked_list
    """
    i = 0
    while i < size(my_list) - 1:
        j = i + 1
        pos_menor = i

        while j < size(my_list):
            if sort_crit(get_element(my_list, i), get_element(my_list, pos_menor)):
                pos_menor = j
            j += 1

        exchange(my_list, i, pos_menor)
        i += 1

    return my_list

def insertion_sort(my_list, sort_crit):
    """
    Ordena una lista utilizando el algoritmo de ordenamiento Insertion Sort.

    Se recorre la lista y se inserta cada elemento en su posición correcta.Se repite este proceso hasta que todos los elementos estén ordenados.

    Parameters:

        my_list (array_list o single_linked_list) – Lista a ordenar.

        sort_crit (function) – Función de comparación.

    Returns: Lista ordenada.
    Return type: array_list o single_linked_list
    """


    i = 0
    while i < size(my_list) - 1:
        j = i + 1
        ordenado = False

        while j > 0 and not ordenado:
            if sort_crit(get_element(my_list, j), get_element(my_list, j-1)):
                exchange(my_list, j, j-1)
                j -= 1
            else:
                ordenado = True
        i += 1

    return my_list


def shell_sort(my_list, sort_crit):
    """
    Ordena una lista utilizando el algoritmo de ordenamiento Shell Sort.

    Se recorre la lista y se ordena los elementos con un gap determinado. Se repite el proceso con un gap menor hasta que la lista esté ordenada.

    Si la lista es vacía o tiene un solo elemento, se retorna la lista original. 
    
    Parameters:

        my_list (array_list o single_linked_list) – Lista a ordenar.

        sort_crit (function) – Función de comparación.

    Returns: Lista ordenada.
    Return type: array_list o single_linked_list
    """
    if (size(my_list) < 2):
        return my_list
    
    brecha: int = 3*(int((size(my_list) - size(my_list)%3)//3)-1) + 1

    if (brecha < 1):
        brecha = 1

    while brecha > 0:
        i: int = 0
        while i < size(my_list) - brecha:
            no_ordenado = True
            j = i + brecha

            while j >= brecha and no_ordenado:
                if (sort_crit(get_element(my_list, j), get_element(my_list, j-brecha))):
                    exchange(my_list, j, j-brecha)
                else:
                    no_ordenado = False 

                j -= brecha
                
            i += 1

        if brecha == 1:
            brecha = 0
        else:
            brecha = (brecha - 1) // 3
            if brecha == 0:
                brecha = 1

    return my_list

def merge_sort(my_list, sort_crit):
    """
    Ordena una lista utilizando el algoritmo recursivo de ordenamiento Merge Sort.

    Se divide la lista en dos partes iguales* y se ordenan de forma recursiva. Luego se mezclan las dos partes ordenadas.

    Si la lista es vacía o tiene un solo elemento, se retorna la lista original.

    Parameters:

        my_list (array_list o single_linked_list) – Lista a ordenar.

        sort_crit (function) – Función de comparación.

    Returns: Lista ordenada.
    Return type: array_list o single_linked_list
    """

    # Si la lista es de un elemento, ya esta ordenada
    if (size(my_list) < 2):
        return my_list
    # Dividir lista en dos
    else:
        izquierda = merge_sort(sub_list(my_list, 0, (size(my_list))//2), sort_crit)
        derecha = merge_sort(sub_list(my_list, (size(my_list))//2, size(my_list)), sort_crit)
        
        merge(my_list, izquierda, derecha, sort_crit)

        return my_list

    

def merge(my_list, izquierda, derecha, sort_crit):
    indice_i = 0 # Iterador de lista izquierda
    indice_d = 0 # Iterador de lista derecha
    indice = 0 # Iterador de lista auxiliar (en este caso la misma lista my_list porque ya tenemos dos listas auxiliares de sublist)

    while (indice < size(my_list)):
        
        if (indice_i >= size(izquierda)):
            change_info(my_list, indice, get_element(derecha, indice_d))
            indice_d += 1
            indice += 1
        elif (indice_d >= size(derecha)):
            change_info(my_list, indice, get_element(izquierda, indice_i))
            indice_i += 1
            indice += 1
        else:
            elemento_i = get_element(izquierda, indice_i)
            elemento_d = get_element(derecha, indice_d)

            if sort_crit(elemento_i, elemento_d):
                change_info(my_list, indice, elemento_i)
                indice_i += 1
                indice += 1
            else:
                change_info(my_list, indice, elemento_d)
                indice_d += 1
                indice += 1

    return my_list

def quick_sort(my_list, sort_crit):
    """
    Ordena una lista utilizando el algoritmo recursivo de ordenamiento Quick Sort.

    Se selecciona un elemento como pivote y se colocan los elementos menores a la izquierda y los mayores a la derecha de este elemento pivote.

    Si la lista es vacía o tiene un solo elemento, se retorna la lista original.
    
    Parameters:

        my_list (array_list o single_linked_list) – Lista a ordenar.

        sort_crit (function) – Función de comparación.

    Returns: Lista ordenada.
    Return type: array_list o single_linked_list
    """
    if (size(my_list) < 2):
        return my_list    

    return quick_sort_recursive(my_list, 0, size(my_list)-1, sort_crit)

def quick_sort_recursive(my_list, inicial, final, sort_crit):
    if inicial < final:
        p = partition(my_list, inicial, final, sort_crit)
        quick_sort_recursive(my_list, inicial, p-1, sort_crit)
        quick_sort_recursive(my_list, p+1, final, sort_crit)
        return my_list
    else:
        return my_list

def partition(my_list, inicial, final, sort_crit):
    pivote = get_element(my_list, final)
    
    i = inicial
    peque = i - 1
    

    while i < final:
        if sort_crit(get_element(my_list, i), pivote):
            exchange(my_list, peque+1, i)
            peque += 1
        i += 1

    exchange(my_list, peque+1, i)
    peque += 1
    return peque
        