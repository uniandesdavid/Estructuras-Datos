def new_list():
    newlist = {
        'elements': [],
        'size': 0
    }
    return newlist

def get_element(my_list, index):
    return my_list["elements"][index]

def is_present(my_list, element, cmp_function):
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1


def add_first(my_list, element):
    """
    Agrega un elemento al inicio de la lista.

    Inserta el elemento al inicio de la lista y actualiza el tamaño de la lista en 1.

    Parameters:
    my_list (array_list): Lista a la cual se le agregará el elemento.

    element (any) : Elemento a agregar.

    Returns:Lista con el elemento agregado al inicio.

    Return type:array_list
    """
    # EST-1
    if my_list["size"] == 0:
        my_list["elements"].append(element)
    else:
        my_list["elements"].insert(0, element)
    my_list["size"] += 1
    return my_list

def add_last(my_list, element):
    """
    Agrega un elemento al final de la lista.

    Inserta el elemento al final de la lista y aumenta el tamaño de la lista en 1.

    Parameters:
    my_list (array_list) – Lista a la cual se le agregará el elemento.
    element (any) – Elemento a agregar.

    Returns:
    Lista con el elemento agregado al final.

    Return type:
    array_list
    """
    my_list["elements"].append(element)
    my_list["size"] += 1
    # EST-1
    return my_list

def size(my_list)->int:
    """
    Retorna el tamaño de la lista.
    
    Args:
        my_list: lista la cual se le quiere conocer el tamaño 

    Returns:
        int: Tamaño de la lista
    """
    # EST-1
    return my_list["size"]

def first_element(my_list)->any:
    """
    Retorna el primer elemento de la lista. Si la lista está vacía, lanza un error IndexError: list index out of range. Esta función no elimina el elemento de la lista.

    Args:
        my_list: lista de la cual se quiere obtener el primer elemento

    Returns:
        any: Primer elemento de la lista
    """
    # EST-2
    return my_list["elements"][0]

def last_element(my_list)->any:
    """
    Retorna el último elemento de la lista. Si la lista está vacía, lanza un error IndexError: list index out of range. Esta función no elimina el elemento de la lista.

    Args:
        my_list: lista de la cual se quiere obtener el último elemento

    Returns:
        any: Último elemento de la lista
    """
    # EST-1
    return my_list["elements"][-1]

def is_empty(my_list)->bool:
    """
    Verifica si la lista está vacía.

    Args:
        my_list: lista la cual se quiere verificar

    Returns:
        bool: True si la lista está vacía, False en caso contrario
    """
    # EST-1
    return size(my_list) == 0
    
def remove_first(my_list)->any:
    """
    Elimina y retorna el primer elemento de la lista. Si la lista está vacía, lanza un error IndexError: list index out of range. Disminuye el tamaño de la lista en 1.

    Args:
        my_list: lista de la cual se quiere eliminar el primer elemento
    Returns:
        any: Primer elemento de la lista
    """
    # EST-1
    first_element = my_list["elements"].pop(0)
    my_list["size"] -= 1
    return first_element

def remove_last(my_list)->any:
    """
    Elimina y retorna el último elemento de la lista. Si la lista está vacía, lanza un error IndexError: list index out of range. Disminuye el tamaño de la lista en 1.

    Args:
        my_list: lista de la cual se quiere eliminar el último elemento
    Returns:
        any: Último elemento de la lista
    """
    # EST-1
    last_element = my_list["elements"].pop()
    my_list["size"] -= 1
    return last_element

def delete_element(my_list, index)->any:
    """
    Elimina y retorna el elemento en la posición dada. Si la lista está vacía, lanza un error IndexError: list index out of range. Disminuye el tamaño de la lista en 1. 
    Elimina el elemento en la posición index, la cual debe ser igual o mayor a cero y menor al tamaño de la lista. 0 <= index < size(my_list)

    Args:
        my_list: lista de la cual se quiere eliminar el elemento
        index: posición del elemento a eliminar

    Returns:
        any: Elemento eliminado de la lista
    """
    # EST-1
    element = my_list["elements"].pop(index)
    my_list["size"] -= 1
    return my_list

def insert_element(my_list, index, element):
    """
    Inserta un elemento en la posición dada. Si la posición es inválida, lanza un error IndexError: list index out of range. Aumenta el tamaño de la lista en 1. 
    La lista puede estar vacia o tener elementos.

    Args:
        my_list: lista a la cual se le quiere insertar el elemento
        index: posición donde se quiere insertar el elemento
        element: elemento a insertar

    Returns:
        array_list: Lista con el elemento insertado en la posición dada
    """
    # EST-1
    if (index == my_list["size"]):
        my_list["elements"].append(element)
    else:
        my_list["elements"].insert(index, element)
    my_list["size"] += 1
    return my_list
def change_info(my_list, index, element):
    """
    Cambia el elemento en la posición dada por el nuevo elemento. Si la posición es inválida, lanza un error IndexError: list index out of range. 
    Args:
        my_list: lista a la cual se le quiere cambiar el elemento
        index: posición del elemento a cambiar
        element: nueva información del elemento
    Returns:
        array_list: Lista con el elemento cambiado
    """
    # EST-1
    my_list["elements"][index] = element
    return my_list

def exchange(my_list, index1, index2):
    """
    Intercambia los elementos en las posiciones dadas. Si alguna de las posiciones es inválida, lanza un error IndexError: list index out of range. 

    Args:
        my_list: lista a la cual se le quiere intercambiar los elementos
        index1: posición del primer elemento a intercambiar
        index2: posición del segundo elemento a intercambiar
    Returns:
        array_list: Lista con los elementos intercambiados
    """
    # EST-1
    temp = my_list["elements"][index1]
    my_list["elements"][index1] = my_list["elements"][index2]
    my_list["elements"][index2] = temp
    return my_list  

def sub_list(my_list, start_index, num_elements):
    """
    Retorna una sublista de la lista dada. Si alguna de las posiciones es inválida, lanza un error IndexError: list index out of range. 
    La sublista incluye el elemento en la posición start_index y excluye el elemento en la posición end_index. 

    Args:
        my_list: lista de la cual se quiere obtener la sublista
        start_index: posición del primer elemento de la sublista
        num_elements: número de elementos a incluir en la sublista

    Returns:
        array_list: Sublista de la lista dada
    """
    # EST-1
    end_index = start_index + num_elements

    num_elements = end_index - start_index

    if (end_index > size(my_list) - 1):
        num_elements = size(my_list) - start_index
    
    if (start_index > size(my_list) - 1):
        num_elements = 0
    
    lista = new_list()
    lista["elements"] = my_list["elements"][start_index:end_index]
    lista["size"] = num_elements

    return lista



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
        
    
