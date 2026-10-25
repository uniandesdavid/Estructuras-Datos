from DataStructures.Tree import rbt_node
import DataStructures.List.single_linked_list as sl

def new_map():
    """
    Crea una tabla de simbolos ordenada basa en un árbol rojo-negro (RBT) vacia

    Se crea una tabla de simbolos ordenada con los siguientes atributos:

        root: Raíz del árbol. Inicializado en None

        type: Tipo de árbol. Inicializado en “RBT”

    Returns: La tabla de simbolos ordenada sin elementos
    Return type: red_black_tree
    """
    arbol = {"root": None, "type": "RBT"}
    return arbol

def put(my_rbt, key, value):
    """
    Ingresa una pareja llave,valor. Si la llave ya existe, se reemplaza el valor.

    Usa la funcion insert_node()

    Parameters:

            my_rbt (red_black_tree) – El RBT

            key (any) – La llave asociada a la pareja

            value (any) – El valor asociado a la pareja

    Returns: El arbol con la nueva pareja
    Return type: red_black_tree
    """
    my_rbt["root"] = insert_node(my_rbt["root"], key, value)
    my_rbt["root"]["color"] = rbt_node.BLACK

    return my_rbt

def insert_node(root, key, value):
    """
    Ingresa una pareja llave,valor. Si la llave ya existe, se reemplaza el valor.

    Es usada en la función insert()

    Parameters:

            root (rbt_node) – La raiz del arbol

            key (any) – La llave asociada a la pareja

            value (any) – El valor asociado a la pareja

    Returns: El arbol con la nueva pareja
    Return type: rbt_node
    """
    if root is None:
        return rbt_node.new_node(key, value)
    elif rbt_node.get_key(root) == key:
        root["value"] = value
        return root
    elif key < rbt_node.get_key(root):
        root["left"] = insert_node(root["left"], key, value)
    else:
        root["right"] = insert_node(root["right"], key, value)
    
    if is_red(root["right"]) and not is_red(root["left"]):
        root = rotate_left(root)
    if is_red(root["left"]):
        if is_red(root["left"]["left"]):
            root = rotate_right(root)
    if is_red(root["right"]) and is_red(root["left"]):
        root = flip_colors(root)

    root["size"] = size_tree(root)
    return root
    

def rotate_left(node_rbt):
    """
    Rota el hijo derecho de un nodo raíz:

    El hijo derecho queda como la nueva raíz, el nodo raíz original como hijo izquierdo de la nueva raíz y el nieto derecho-izquierdo original como el hijo derecho del nodo raíz original.

    Intercambia los colores entre el nodo raíz y su hijo derecho (originales).

    Parameters:

        node_rbt – Nodo raíz del árbol a rotar

    Returns: La nueva raíz (después de la rotación)
    Return type: rbt_node
    """
    # Variables temporales
    temp = node_rbt["right"]
    nieto = temp["left"]
    color_node_rbt = node_rbt["color"]

    # Intercambiar hijos
    node_rbt["right"] = nieto
    temp["left"] = node_rbt

    # Intercambiar colores
    node_rbt["color"] = temp["color"]
    temp["color"] = color_node_rbt

    node_rbt["size"] = size_tree(node_rbt)
    temp["size"] = size_tree(temp)

    return temp

def rotate_right(node_rbt):
    """
    Rota el hijo izquierdo de un nodo raíz:

    El hijo izquierdo queda como la nueva raíz, el nodo raíz original como hijo derecho de la nueva raíz y el nieto izquierdo-derecho original como el hijo izquierdo del nodo raíz original.

    Intercambia los colores entre el nodo raíz y su hijo izquierdo (originales).

    Parameters:

        node_rbt – Nodo raíz del árbol a rotar

    Returns: La nueva raíz (después de la rotación)
    Return type: rbt_node
    """
    # Variables temporales
    temp = node_rbt["left"]
    nieto = temp["right"]

    color_node_rbt = node_rbt["color"]

    # Intercambiar hijos
    node_rbt["left"] = nieto
    temp["right"] = node_rbt

    # Intercambiar colores
    node_rbt["color"] = temp["color"]  
    temp["color"] = color_node_rbt

    node_rbt["size"] = size_tree(node_rbt)
    temp["size"] = size_tree(temp)

    return temp

def flip_node_color(node_rbt):
    """
    Cambia el color de un nodo

    Parameters:

        node_rbt (rbt_node) – El nodo a cambiar

    Returns: El nodo con el color opuesto
    Return type: rbt_node
    """
    if node_rbt is not None:
        node_rbt["color"] = (node_rbt["color"]-1)%2

    return node_rbt


def flip_colors(node_rbt):
    """
    Cambia el color de un nodo y de sus dos hijos

    Parameters:

        node_rbt (rbt_node) – El nodo a cambiar

    Returns: El nodo con el color opuesto
    Return type: rbt_node
    """
    if node_rbt is not None:
        node_rbt = flip_node_color(node_rbt)
        node_rbt["right"] = flip_node_color(node_rbt["right"])
        node_rbt["left"] = flip_node_color(node_rbt["left"])

    return node_rbt

def is_red(node_rbt):
    """
    Indica si un nodo del árbol es rojo

    Un nodo es rojo si existe (diferente de None) y su color es RED

    Parameters:

        node_rbt (rbt_node) – El nodo a examinar

    Returns: True si el nodo es rojo, False de lo contrario
    Return type: bool
    """
    if node_rbt is not None:
        return node_rbt["color"] == rbt_node.RED
    
    return False

def size(my_rbt):
    """
    Retorna el número de entradas en la tabla de simbolos

    Usa la función size_tree() para contar el número de elementos

    Parameters:

        my_rbt (reb_black_tree) – El arbol de búsqueda

    Returns: El número de elementos en la tabla
    Return type: int
    """
    return size_tree(my_rbt["root"])



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

def default_compare(key, element):
    """
    Función de comparación por defecto. Compara una llave con la llave de un elemento llave-valor.

    Parameters:

        key (any) – Llave a comparar

        element (rbt_node) – entry a comparar

    Returns: 0 si son iguales, 1 si key > la llave del element, -1 si key < que la llave del element
    Return type: int
    """
    if key == rbt_node.get_key(element):
        return 0
    elif key > rbt_node.get_key(element):
        return 1
    return -1

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

        root (rbt_node) – La raiz del arbol a examinar

        key_list (single_linked_list) – La lista de respuesta

    Returns: Una lista con todos las llaves
    Return type: single_linked_list
    """
    if root != None:
        key_set_tree(root["left"], key_list)
        sl.add_last(key_list, rbt_node.get_key(root))
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

        root (rbt_node) – La raiz del arbol a examinar

        key_list (single_linked_list) – La lista de respuesta

    Returns: Una lista con todos las llaves
    Return type: single_linked_list
    """
    if root != None:
        value_set_tree(root["left"], value_list)
        sl.add_last(value_list, rbt_node.get_value(root))
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
    return rbt_node.get_key(get_min_node(my_bst["root"]))

def get_min_node(root):
    """
    Retorna la llave mas pequeña de la tabla de simbolos

    Es usada en la función get_min()

    Parameters:
        root (rbt_node) – La raiz del arbol a examinar
    
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
    return rbt_node.get_key(get_max_node(my_bst["root"]))

def get_max_node(root):
    """
    Retorna la llave mas grande de la tabla de simbolos

    Es usada en la función get_max()

    Parameters:

        root (rbt_node) – La raiz del arbol a examinar
    
    Returns: La llave más a la derecha
    Return type: any
    """
    if root is None:
        return None
    
    if root["right"] is None:
        return root
    
    return get_max_node(root["right"])

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

        root (rbt_node) – La raiz del arbol a examinar
    
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
    nodo = get_node(my_bst["root"], key)
    return rbt_node.get_value(nodo) if nodo is not None else None 

def get_node(root, key):
    """Busca un nodo en el árbol binario de búsqueda (BST) de manera recursiva.

    Esta función es llamada por la función get.

    Parameters:
        root (rbt_node) – raiz del árbol donde se quiere buscar el nodo

        key (any) – llave del nodo a buscar

    Returns: nodo encontrado o None si no se encuentra

    Return type: rbt_node"""
    if root is None: 
        return None 
    elif key == root["key"]:
        return root
    elif key < root["key"]:
        return get_node(root["left"], key)
    else: 
        return get_node(root["right"], key)

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
    keys_set_range = keys_range(my_bst["root"], key_initial, key_final, keys_set_range)

    return keys_set_range

def keys_range(root, key_initial, key_final, list_key):
    """
    Retorna todas las llaves del arbol que se encuentren entre [key_initial, key_final].

    Es usada en la función keys()

    Parameters:

        root (rbt_node) – La raiz del arbol a examinar

        key_initial (any) – limite inferior

        key_final (any) – limite superior

        list_key (single_linked_list) – La lista de respuesta

    Returns: Las llaves en el rago especificado
    Return type: single_linked_list
    """
    if root is not None:
        if (rbt_node.get_key(root) > key_initial):
            keys_range(root["left"], key_initial, key_final, list_key)
        if (rbt_node.get_key(root) >= key_initial and rbt_node.get_key(root) <= key_final):
            sl.add_last(list_key, rbt_node.get_key(root))
        if (rbt_node.get_key(root) < key_final):
            keys_range(root["right"], key_initial, key_final, list_key)

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
    values_set_range = sl.new_list()
    values_set_range = values_range(my_bst["root"], key_initial, key_final, values_set_range)

    return values_set_range


def values_range(root, key_initial, key_final, list_value):
    """
    Retorna todas los valores del arbol que se encuentren entre [key_initial, key_final]

    Es usada en la función values()
    Parameters:

        root (rbt_node) – La raiz del arbol a examinar

        key_lo (any) – limite inferior

        key_hi (any) – limite superior

        list_values (single_linked_list) – La lista de respuesta

    Returns: Las llaves en el rago especificado
    Return type: single_linked_list
    """
    if root is not None:
        if (rbt_node.get_key(root) > key_initial):
            values_range(root["left"], key_initial, key_final, list_value)
        if (rbt_node.get_key(root) >= key_initial and rbt_node.get_key(root) <= key_final):
            sl.add_last(list_value, rbt_node.get_value(root))
        if (rbt_node.get_key(root) < key_final):
            values_range(root["right"], key_initial, key_final, list_value)

    return list_value

def default_compare(key, element):
   """
   Función de comparación por defecto. Compara una llave con la llave de un elemento llave-valor.

    Parameters:

        key (any) – Llave a comparar

        element (rbt_node) – entry a comparar

    Returns: 0 si son iguales, 1 si key > la llave del element, -1 si key < que la llave del element
    Return type: int
   """
   if key == rbt_node.get_key(element):
      return 0
   elif key > rbt_node.get_key(element):
      return 1
   return -1


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
    return floor_key(my_bst["root"], key)

def floor_key(root, key):
    """
    Retorna la llave que precede a la llave key en la tabla de simbolos.

    Si la llave existe, retorna la misma llave. Si no existe, retorna la llave predecedente más cercana como si la llave key existiera en la tabla.

    Es usada en la función floor()

    Parameters:

        root (rbt_node) – La raiz del arbol a examinar

        key (any) – La llave de búsqueda

    Returns: La llave predecesora a key
    Return type: any
    """

    if root is None:
        return None
    
    if key == rbt_node.get_key(root):
        return key
    elif key < rbt_node.get_key(root):
        return floor_key(root["left"], key)
    else:
        nodo_key = floor_key(root["right"], key)

        if nodo_key is not None:
            return nodo_key
        
        return rbt_node.get_key(root)




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
    return ceiling_key(my_bst["root"], key)

def ceiling_key(root, key):
    """
    Retorna la llave que sucede a la llave key en la tabla de simbolos.

    Si la llave existe, retorna la misma llave. Si no existe, retorna la llave sucesora más cercana como si la llave key existiera en la tabla. Por ejemplo, si la tabla contiene las llaves [1, 3, 5, 7, 9] y se busca la llave 6, la función retornará 7.

    Es usada en la función ceiling()

    Parameters:

        root (rbt_node) – La raiz del arbol a examinar

        key (any) – La llave de búsqueda

    Returns: La llave sucesora a key
    Return type: any
    """
    if root is None:
        return None
    
    if key == rbt_node.get_key(root):
        return key
    elif key < rbt_node.get_key(root):
        nodo_key = ceiling_key(root["left"], key)

        if nodo_key is not None:
            return nodo_key
        
        return rbt_node.get_key(root)
    else:
        return ceiling_key(root["right"], key)
        

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
    
    return rbt_node.get_key(select_key(my_bst["root"], pos))

def select_key(root, key):
    """
    Retorna la siguiente llave a la k-esima llave de izquierda a derecha de la tabla de simbolos.

    Es usada en la función select()

    Parameters:

        root (rbt_node) – La raiz del arbol a examinar

        key (int) – la llave de búsqueda

    Returns: La llave en la posición pos
    Return type: rbt_node
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
    return int(rank_keys(my_bst["root"], key))

def rank_keys(root, key):
    """
    Retorna el número de llaves en la tabla que son estrictamente predecesoras a key Por ejemplo, si la tabla contiene las llaves [1, 3, 5, 7, 9] y se busca la llave 6, la función retornará 3.

    Es usada en la función rank()

    Parameters:

        root (rbt_node) – La raiz del arbol a examinar

        key (any) – la llave de busqueda

    Returns: El número de llaves
    Return type: int
    """
    if root is None:
        return 0
    
    if rbt_node.get_key(root) == key:
        return size_tree(root["left"])
    elif rbt_node.get_key(root) < key:
        return size_tree(root["left"]) + rank_keys(root["right"], key) + 1
    else:
        return rank_keys(root["left"], key)


