import DataStructures.Tree.bst_node as bst_node
import DataStructures.List.single_linked_list as sl
import DataStructures.List.array_list as al

def new_map():
    """
    Crea una nueva tabla de simbolos (map) ordenada basada en un árbol binario de búsqueda (BST).

    La tabla de simbolos es creada con los siguientes atributos:

    root: raiz del árbol (inicialmente None)

    Returns: tabla de simbolos creada
    Return type: binary_search_tree
    """
    arbol = {"root": None, "cmp_function": default_compare}
    return arbol

def put(my_bst, key, value):
    """
    Agrega un nuevo nodo llave-valor a un árbol binario de búsqueda (BST). Si la llave ya existe, se actualiza el value del nodo.

    Esta función llama a la función insert_node para agregar el nodo en la posición correcta del árbol de manera recursiva.

    Parameters:

        my_bst (binary_search_tree) – árbol binario de búsqueda donde se quiere agregar el nodo

        key (any) – llave del nodo

        value (any) – valor del nodo

    Returns: árbol binario de búsqueda actualizado
    Return type: binary_search_tree
    """
    my_bst["root"] = insert_node(my_bst["root"], key, value, my_bst["cmp_function"])
    return my_bst
    

def insert_node(root, key, value, cmp_function):
    """
    Inserta un nuevo nodo llave-valor en el árbol binario de búsqueda (BST) de manera recursiva.

    Esta función es llamada por la función put.

    Parameters:

        root (bst_node) – raiz del árbol donde se quiere agregar el nodo

        key (any) – llave del nodo

        value (any) – valor del nodo

    Returns: raiz del árbol binario de búsqueda actualizado
    Return type: bst_node
    """

    if root is None:
        return bst_node.new_node(key, value)

    comparacion = cmp_function(key, root)

    if comparacion == 0:
        root["value"] = value
    elif comparacion == -1:
        root["left"] = insert_node(root["left"], key, value, cmp_function)
    else:
        root["right"] = insert_node(root["right"], key, value, cmp_function)

    root["size"] = size_tree(root)
    return root

def size(my_bst):
    """
    Retorna el número de entradas en la tabla de simbolos

    Usa la función size_tree() para contar el número de elementos

    Parameters:

        my_bst (binary_search_tree) – El arbol de búsqueda

    Returns: El número de elementos en la tabla
    Return type: int
    """
    return size_tree(my_bst["root"])



def size_tree(root):
    """
    Retornar el número de entradas en la a partir del nodo root

    Es usada en la función size()

    Parameters:

        root (rbt_node) – La raiz del arbol a examinar

    Returns: El número de elementos en la tabla
    Return type: int
    """
    if root is None:
        return 0
    
    return 1 + size_tree(root["left"]) + size_tree(root["right"])

def contains(my_bst, key):
    """
    Informa si la llave key se encuentra en la tabla de símbolos.

    Usa la función get() para buscar la llave en el arbol

    Parameters:

        my_bst (binary_search_tree) – El arbol de búsqueda

        key (any) – La llave a buscar

    Returns: True si la llave está presente, False en caso contrario
    Return type: bool
    """
    if get(my_bst, key) is None:
        return False
    else:
        return True


def is_empty(my_bst):
    """
    Informa si la tabla de simbolos se encuentra vacia.

    Parameters: 
        my_bst (binary_search_tree) – El arbol de búsqueda
    
    Returns: True si la tabla es vacía, False en caso contrario 
    Return type: bool
    """
    return size(my_bst) == 0

def key_set(my_bst):
    """
    Retorna una lista con todas las llaves de la tabla.

    Usa la función key_set_tree() para construir la lista de llaves

    Parameters:

        my_bst (binary_search_tree) – El arbol de búsqueda
    
    Returns: Una lista con todas las llaves de la tabla
    Return type: single_linked_list
    """
    key_set_list = sl.new_list()
    key_set_list = key_set_tree(my_bst["root"], key_set_list)
    return key_set_list
    

def key_set_tree(root, key_list):
    """
    Construye una lista con las llaves de la tabla. Se recorre el arbol en inorder

    Es usada en la función key_set()

    Si root no es None, se recorre el arbol en inorder, primero el hijo izquierdo, luego la raiz y finalmente el hijo derecho

    Parameters:

        root (bst_node) – La raiz del arbol a examinar

        key_list (single_linked_list) – La lista de respuesta

    Returns: Una lista con todos las llaves
    Return type: single_linked_list
    """
    if root != None:
        key_set_tree(root["left"], key_list)
        sl.add_last(key_list, bst_node.get_key(root))
        key_set_tree(root["right"], key_list)

    return key_list



def value_set(my_bst):
    """
    Retorna una lista con los valores de la tabla.

    Usa la función value_set_tree() para construir la lista de valores

    Parameters:

        my_bst (binary_search_tree) – El arbol de búsqueda
    
    Returns: Una lista con todos los valores de la tabla
    Return type: single_linked_list
    """
    value_set_list = sl.new_list()
    value_set_list = value_set_tree(my_bst["root"], value_set_list)
    return value_set_list
    

def value_set_tree(root, value_list):
    """
    Construye una lista con las llaves de la tabla. Se recorre el arbol en inorder

    Es usada en la función key_set()

    Si root no es None, se recorre el arbol en inorder, primero el hijo izquierdo, luego la raiz y finalmente el hijo derecho

    Parameters:

        root (bst_node) – La raiz del arbol a examinar

        key_list (single_linked_list) – La lista de respuesta

    Returns: Una lista con todos las llaves
    Return type: single_linked_list
    """
    if root != None:
        value_set_tree(root["left"], value_list)
        sl.add_last(value_list, bst_node.get_value(root))
        value_set_tree(root["right"], value_list)

    return value_list

def get_min(my_bst):
    """
    Retorna la llave mas pequeña de la tabla de simbolos

    Usa la función get_min_node() para encontrar la llave más a la izquierda

    Parameters:
        my_bst (binary_search_tree) – El arbol de búsqueda
    
    Returns: La llave más a la izquierda
    Return type: any
    """
    if my_bst["root"] is None:
        return None
    return bst_node.get_key(get_min_node(my_bst["root"]))

def get_min_node(root):
    """
    Retorna la llave mas pequeña de la tabla de simbolos

    Es usada en la función get_min()

    Parameters:
        root (bst_node) – La raiz del arbol a examinar
    
    Returns: La llave más a la izquierda
    Return type: any
    """
    if root is None:
        return None
    
    if root["left"] is None:
        return root
    
    return get_min_node(root["left"])

def get_max(my_bst):
    """
    Retorna la llave mas grande de la tabla de simbolos

    Usa la función get_max_node() para encontrar la llave más grande de del arbol

    Parameters:

        my_bst (binary_search_tree) – El arbol de búsqueda
    
    Returns: La llave más a la derecha
    Return type: any
    """
    if my_bst["root"] is None:
        return None
    return bst_node.get_key(get_max_node(my_bst["root"]))

def get_max_node(root):
    """
    Retorna la llave mas grande de la tabla de simbolos

    Es usada en la función get_max()

    Parameters:

        root (bst_node) – La raiz del arbol a examinar
    
    Returns: La llave más a la derecha
    Return type: any
    """
    if root is None:
        return None
    
    if root["right"] is None:
        return root
    
    return get_max_node(root["right"])


def delete_min(my_bst):
    """
    Encuentra y remueve la llave mas pequeña de la tabla de simbolos y su valor asociado.

    Usa la función delete_min_tree() para eliminar la llave más pequeña

    Parameters:

        my_bst (binary_search_tree) – El arbol de búsqueda

    Returns: El arbol de búsqueda sin la llave más pequeña
    Return type: binary_search_tree
    """
    my_bst["root"] = delete_min_tree(my_bst["root"])
    return my_bst

def delete_min_tree(root):
    """
    Encuentra y remueve la llave mas pequeña de la tabla de simbolos y su valor asociado

    Es usada en la función delete_min()

    Parameters:

        root (bst_node) – La raiz del arbol a examinar
    
    Returns: Retorna la raiz del arbol sin la llave más pequeña
    Return type: bst_node
    """
    if (root is None):
        return None
    
    if root["left"] is None:
        return root["right"]
    
    root["left"] = delete_min_tree(root["left"])
    root["size"] = size_tree(root)

    return root
        
def delete_max(my_bst):
    """
    Encuentra y remueve la llave mas grande de la tabla de simbolos y su valor asociado.

    Usa la función delete_max_tree() para eliminar la llave más grande

    Parameters:

        my_bst (binary_search_tree) – El arbol de búsqueda
    
    Returns: El arbol de búsqueda sin la llave más grande
    Return type: binary_search_tree
    """
    my_bst["root"] = delete_max_tree(my_bst["root"])
    return my_bst

def delete_max_tree(root):
    """
    Encuentra y remueve la llave mas grande de la tabla de simbolos y su valor asociado.

    Es usada en la función delete_max()

    Parameters:

        root (bst_node) – La raiz del arbol a examinar
    
    Returns: Retorna la raiz del arbol sin la llave más grande
    Return type: bst_node
    """
    if (root is None):
        return None
    
    if root["right"] is None:
        return root["left"]
    
    root["right"] = delete_max_tree(root["right"])
    root["size"] = size_tree(root)

    return root

def height(my_bst):
    """
    Retorna la altura del arbol de busqueda

    Usa la función height_tree() para encontrar la altura del arbol

    Parameters:

        my_bst (binary_search_tree) – El arbol de búsqueda
    
    Returns: La altura del arbol
    Return type: int
    """
    height = height_tree(my_bst["root"])

    if (height == -1):
        return 0
    
    return height

def height_tree(root):
    """
    Retorna la altura del arbol de busqueda

    Es usada en la función height() Usa la función height_tree() para encontrar la altura del arbol

    Parameters:

        root (bst_node) – La raiz del arbol a examinar
    
    Returns: La altura del arbol
    Return type: int
    """
    if (root is None):
        return -1
    
    return max(1 + height_tree(root["left"]), 1 + height_tree(root["right"]))

def get(my_bst, key):
    """Busca un nodo en el árbol binario de búsqueda (BST) y devuelve su valor.

    Esta función llama a la función get_node para buscar el nodo en el árbol de manera recursiva.

    Parameters:
        my_bst (binary_search_tree) – árbol binario de búsqueda donde se quiere buscar el nodo

        key (any) – llave del nodo a buscar

    Returns: valor del nodo encontrado o None si no se encuentra

    Return type: any
    """ 
    nodo = get_node(my_bst["root"], key, my_bst["cmp_function"])
    return bst_node.get_value(nodo) if nodo is not None else None 

def get_node(root, key, cmp_function):
    """Busca un nodo en el árbol binario de búsqueda (BST) de manera recursiva.

    Esta función es llamada por la función get.

    Parameters:
        root (bst_node) – raiz del árbol donde se quiere buscar el nodo

        key (any) – llave del nodo a buscar

    Returns: nodo encontrado o None si no se encuentra

    Return type: bst_node"""
    if root is None: 
        return None 
    
    comparacion = cmp_function(key, root)

    if comparacion == 0:
        return root
    elif comparacion == -1:
        return get_node(root["left"], key, cmp_function)
    else: 
        return get_node(root["right"], key, cmp_function)

def keys(my_bst, key_initial, key_final):
    """
    Retorna todas las llaves del arbol que se encuentren entre [key_initial, key_final].

    Usa la función keys_range() para encontrar las llaves en el rango especificado

    Parameters:

        my_bst (binary_search_tree) – La tabla de simbolos

        key_initial (any) – limite inferior

        key_final (any) – limite superior

    Returns: Las llaves en el rago especificado
    Return type: single_linked_list

    """
    keys_set_range = sl.new_list()
    keys_set_range = keys_range(my_bst["root"], key_initial, key_final, keys_set_range, my_bst["cmp_function"])

    return keys_set_range

def keys_range(root, key_initial, key_final, list_key, cmp_function):
    """
    Retorna todas las llaves del arbol que se encuentren entre [key_initial, key_final].

    Es usada en la función keys()

    Parameters:

        root (bst_node) – La raiz del arbol a examinar

        key_initial (any) – limite inferior

        key_final (any) – limite superior

        list_key (single_linked_list) – La lista de respuesta

    Returns: Las llaves en el rago especificado
    Return type: single_linked_list
    """
    if root is not None:
        comparacion_inicial = cmp_function(key_initial, root)
        comparacion_final = cmp_function(key_final, root)

        if (comparacion_inicial == -1):
            keys_range(root["left"], key_initial, key_final, list_key, cmp_function)
        if (comparacion_inicial <= 0 and comparacion_final >= 0):
            sl.add_last(list_key, bst_node.get_key(root))
        if (comparacion_final):
            keys_range(root["right"], key_initial, key_final, list_key, cmp_function)

    return list_key

def values(my_bst, key_initial, key_final):
    """
    Retorna todas los valores del arbol que se encuentren entre [key_initial, key_final]

    Usa la función values_range() para encontrar los valores en el rango especificado

    Parameters:

        my_bst (binary_search_tree) – La tabla de simbolos

        key_initial (any) – limite inferior

        key_final (any) – limite superior

    Returns: Las llaves en el rago especificado
    Return type: single_linked_list
    """
    values_set_range = al.new_list()
    values_set_range = values_range(my_bst["root"], key_initial, key_final, values_set_range, my_bst["cmp_function"])

    return values_set_range


def values_range(root, key_initial, key_final, list_value, cmp_function):
    """
    Retorna todas los valores del arbol que se encuentren entre [key_initial, key_final]

    Es usada en la función values()
    Parameters:

        root (bst_node) – La raiz del arbol a examinar

        key_lo (any) – limite inferior

        key_hi (any) – limite superior

        list_values (single_linked_list) – La lista de respuesta

    Returns: Las llaves en el rago especificado
    Return type: single_linked_list
    """
    if root is not None:
        comparacion_inicial = cmp_function(key_initial, root)
        comparacion_final = cmp_function(key_final, root)

        if (comparacion_inicial == -1):
            values_range(root["left"], key_initial, key_final, list_value, cmp_function)
        if (comparacion_inicial <= 0 and comparacion_final >= 0):
            al.add_last(list_value, bst_node.get_value(root))
        if (comparacion_final == 1):
            values_range(root["right"], key_initial, key_final, list_value, cmp_function)

    return list_value

def default_compare(key, element):
    """
    Función de comparación por defecto. Compara una llave con la llave de un elemento llave-valor.

        Parameters:

            key (any) – Llave a comparar

            element (bst_node) – entry a comparar

        Returns: 0 si son iguales, 1 si key > la llave del element, -1 si key < que la llave del element
        Return type: int
    """
    if key == bst_node.get_key(element):
        return 0
    elif key > bst_node.get_key(element):
        return 1
    return -1

def remove(my_bst, key):
    """
    Elimina la pareja llave-valor que coincida con``key``.

    Usa la función remove_node() para eliminar la pareja

    Parameters:

        my_bst (binary_search_tree) – El arbol de búsqueda

        key (any) – La llave asociada a la pareja a eliminar

    Returns: El arbol sin la pareja key-value
    Return type: binary_search_tree
    """
    my_bst["root"] = remove_node(my_bst["root"], key, my_bst["cmp_function"])
    return my_bst

def remove_node(root, key, cmp_function):
    """
    Elimina la pareja llave-valor que coincida con``key``.

    Es usada en la función remove()

    Parameters:

        root (bst_node) – La raiz del arbol a examinar

        key (any) – La llave asociada a la pareja a eliminar

    Returns: El arbol sin la pareja key-value
    Return type: bst_node
    """
    if root is None:
        return None
    
    comparacion = cmp_function(key, root)

    if comparacion == 0:
        if root["right"] is None:
            return root["left"]
        elif root["left"] is None:
            return root["right"]
        else:
            nodo = get_min_node(root["right"])
            root["right"] = delete_min_tree(root["right"])
            
            nodo["right"] = root["right"]
            nodo["left"] = root["left"]

            nodo["size"] = size_tree(nodo["right"]) + size_tree(nodo["left"]) + 1

            return nodo
    elif comparacion == 1:
        root["right"] = remove_node(root["right"], key, cmp_function)
    else:
        root["left"] = remove_node(root["left"], key, cmp_function)
    
    root["size"] = size_tree(root)
    return root

def floor(my_bst, key):
    """
    Retorna la llave que precede a la llave key en la tabla de simbolos.

    Si la llave existe, retorna la misma llave. Si no existe, retorna la llave predecedente más cercana como si la llave key existiera en la tabla. Por ejemplo, si la tabla contiene las llaves [1, 3, 5, 7, 9] y se busca la llave 6, la función retornará 5.

    Usa la función floor_key() para encontrar la llave predecesora a key

    Parameters:

        my_bst (binary_search_tree) – El arbol de búsqueda

        key (any) – La llave de búsqueda

    Returns: La llave predecesora a key
    Return type: any
    """
    return floor_key(my_bst["root"], key, my_bst["cmp_function"])

def floor_key(root, key, cmp_function):
    """
    Retorna la llave que precede a la llave key en la tabla de simbolos.

    Si la llave existe, retorna la misma llave. Si no existe, retorna la llave predecedente más cercana como si la llave key existiera en la tabla.

    Es usada en la función floor()

    Parameters:

        root (bst_node) – La raiz del arbol a examinar

        key (any) – La llave de búsqueda

    Returns: La llave predecesora a key
    Return type: any
    """

    if root is None:
        return None 
    
    comparacion = cmp_function(key, root)
    
    if comparacion == 0:
        return key
    elif comparacion == -1:
        return floor_key(root["left"], key, cmp_function)
    else:
        nodo_key = floor_key(root["right"], key, cmp_function)

        if nodo_key is not None:
            return nodo_key
        
        return bst_node.get_key(root)




def ceiling(my_bst, key):
    """
    Retorna la llave que sucede a la llave key en la tabla de simbolos.

    Si la llave existe, retorna la misma llave. Si no existe, retorna la llave sucesora más cercana como si la llave key existiera en la tabla. Por ejemplo, si la tabla contiene las llaves [1, 3, 5, 7, 9] y se busca la llave 6, la función retornará 7.

    Usa la función ceiling_key() para encontrar la llave sucesora a key

    Parameters:

        my_bst (binary_search_tree) – El arbol de búsqueda

        key (any) – La llave de búsqueda

    Returns: La llave sucesora a key
    Return type: any
    """
    return ceiling_key(my_bst["root"], key, my_bst["cmp_function"])

def ceiling_key(root, key, cmp_function):
    """
    Retorna la llave que sucede a la llave key en la tabla de simbolos.

    Si la llave existe, retorna la misma llave. Si no existe, retorna la llave sucesora más cercana como si la llave key existiera en la tabla. Por ejemplo, si la tabla contiene las llaves [1, 3, 5, 7, 9] y se busca la llave 6, la función retornará 7.

    Es usada en la función ceiling()

    Parameters:

        root (bst_node) – La raiz del arbol a examinar

        key (any) – La llave de búsqueda

    Returns: La llave sucesora a key
    Return type: any
    """
    if root is None:
        return None

    comparacion = cmp_function(key, root)
    
    if comparacion == 0:
        return key
    elif comparacion == -1:
        nodo_key = ceiling_key(root["left"], key, cmp_function)

        if nodo_key is not None:
            return nodo_key
        
        return bst_node.get_key(root)
    else:
        return ceiling_key(root["right"], key, cmp_function)
        

def select(my_bst, pos):
    """
    Retorna la siguiente llave a la k-esima llave de izquierda a derecha de la tabla de simbolos.

    Usa la función select_key() para encontrar la llave en la posición pos

    Parameters:

        my_bst (binary_search_tree) – El arbol de búsqueda

        pos (int) – la pos-esima llave de izquierda a derecha

    Returns: La llave en la posición pos
    Return type: any
    """
    if pos < 0 or pos >= size(my_bst):
        return None
    
    return bst_node.get_key(select_key(my_bst["root"], pos))

def select_key(root, key):
    """
    Retorna la siguiente llave a la k-esima llave de izquierda a derecha de la tabla de simbolos.

    Es usada en la función select()

    Parameters:

        root (bst_node) – La raiz del arbol a examinar

        key (int) – la llave de búsqueda

    Returns: La llave en la posición pos
    Return type: bst_node
    """
    if root is None:
        return None

    if size_tree(root["left"]) == key:
        return root
    elif size_tree(root["left"]) < key:
        if root["right"] is None:
            return root
        
        return select_key(root["right"], key - size_tree(root["left"]) - 1)
    else:
        return select_key(root["left"], key)
    

def rank(my_bst, key):
    """
    Retorna el número de llaves en la tabla que son estrictamente predecesoras a key Por ejemplo, si la tabla contiene las llaves [1, 3, 5, 7, 9] y se busca la llave 6, la función retornará 3.

    Usa la función rank_keys() para encontrar el número de llaves predecesoras a key

    Parameters:

        my_bst (binary_search_tree) – El arbol de búsqueda

        key (any) – la llave de busqueda

    Returns: El número de llaves
    Return type: int
    """
    return int(rank_keys(my_bst["root"], key, my_bst["cmp_function"]))

def rank_keys(root, key, cmp_function):
    """
    Retorna el número de llaves en la tabla que son estrictamente predecesoras a key Por ejemplo, si la tabla contiene las llaves [1, 3, 5, 7, 9] y se busca la llave 6, la función retornará 3.

    Es usada en la función rank()

    Parameters:

        root (bst_node) – La raiz del arbol a examinar

        key (any) – la llave de busqueda

    Returns: El número de llaves
    Return type: int
    """
    if root is None:
        return 0
    
    comparacion = cmp_function(key, root)
    
    if comparacion == 0:
        return size_tree(root["left"])
    elif comparacion == 1:
        return size_tree(root["left"]) + rank_keys(root["right"], key, cmp_function) + 1
    else:
        return rank_keys(root["left"], key, cmp_function)









