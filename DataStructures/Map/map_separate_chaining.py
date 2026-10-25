from DataStructures.List import array_list as lt
from DataStructures.List import single_linked_list as sl
from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf
import random as rd

def new_map(num_elements, load_factor, prime=109345121): 
    """
    Crea una nueva tabla de simbolos (map) sin elementos.


    Args:
        num_elements (int) – Número de elementos que se espera almacenar en la tabla.

        load_factor (float) – Factor de carga límite de la tabla antes de hacer un rehash.

        prime (int) – Número primo usado para calcular el hash. Por defecto es 109345121.
    """
    capacity = mf.next_prime(num_elements//load_factor)
    scale = rd.randint(1, prime-1)
    shift = rd.randint(0, prime-1)
    hash_table = {
        'prime': prime,
        'capacity': capacity,
        'scale': scale,
        'shift': shift,
        'table': lt.new_list(),
        'size': 0,
        'limit_factor': load_factor,
        'current_factor': 0
    }
    for _ in range(capacity):
        bucket = sl.new_list()
        lt.add_last(hash_table['table'], bucket)
    return hash_table

def put(my_map, key, value): 
    """
    Agrega una nueva entrada llave-valor a la tabla. Si la llave ya existe en la tabla, se actualiza el value de la entrada.

    Para agregar una nueva entrada se debe seguir los siguientes pasos:

        1. Calcular el hash de la llave, usando la función hash_value.
        2. Se busca la lista en la posición del hash en la tabla.
        3. Si la llave ya existe en la lista, se actualiza el valor de la entrada.
        4. Si la llave no existe en la lista, se agrega una nueva entrada al final de la lista.
        5. Se actualiza el current_factor de la tabla si se agrega una nueva entrada.
        6. Si el current_factor supera el limit_factor, se realiza un rehash de la tabla.

    Se retorna la tabla con la nueva entrada.

    Parameters:
        my_map (map_separate_chaining) – Tabla de simbolos a la cual se desea agregar un nuevo elemento.
        key (any) – Llave del nuevo elemento.
        value (any) – Valor del nuevo elemento.

    Returns: Tabla de simbolos con el nuevo elemento agregado.

    Return type: map_separate_chaining
    """
    # Calcular hash de la llave
    hash_key = mf.hash_value(my_map, key)

    # Crear map entry
    elemento = me.new_map_entry(key, value)

    # Variable Bool si llave existe
    llave_existe = False

    # Buscar la lista en la posicion del hash key
    bucket = lt.get_element(my_map["table"], hash_key)

    # Buscar si la key esta en el bucket
    current_nodo = bucket["first"]
    while current_nodo != None and not llave_existe:
        if (default_compare(key, current_nodo["info"]) == 0):
            llave_existe = True
        else:
            current_nodo = current_nodo["next"]

    # Si la llave ya existe en la lista, se actualiza el valor de la entrada.
    if (llave_existe):
        current_nodo["info"] = elemento
    # Si la llave no existe en la lista, se agrega una nueva entrada al final de la lista.
    else:
        sl.add_last(bucket, elemento)
        my_map["size"] += 1
    
    # Se actualiza el current_factor de la tabla si se agrega una nueva entrada.
    my_map["current_factor"] = my_map["size"]/my_map["capacity"]

    if (my_map["current_factor"] > my_map["limit_factor"]):
        rehash(my_map)
    
    return my_map

def default_compare(key, entry):
    """
    Funcion de comparacion por defecto. Compara la llave key con la llave de una entry dada
    
    Parameters:
        key (any) : Llave con la que se desea comparar.

        entry (map_entry) : Entrada de la tabla de simbolos con la que se desea comparar.

    Returns: 0 si son iguales, 1 si key > la llave del entry, -1 si key < que la llave del entry
    Return type: int
    """
    if (key == me.get_key(entry)):
        return 0
    elif (key > me.get_key(entry)):
        return 1
    return -1

def contains(my_map, key): 
    """
    Verifica si una llave se encuentra en la tabla de simbolos.

    Parameters: 
        my_map (map_separate_chaining) – Tabla de simbolos en la cual se desea verificar si la llave se encuentra.

        key (any) – Llave que se desea verificar si se encuentra en la tabla.

    Returns: True si la llave se encuentra en la tabla, False en caso contrario.
    Return type: bool

    Args:
        my_map (_type_): _description_
        key (_type_): _description_
    """
    # Variable Bool si llave existe
    llave_existe = False

    # Calcular hash de la llave
    hash_key = mf.hash_value(my_map, key)

    # Buscar la lista en la posicion del hash key
    bucket = lt.get_element(my_map["table"], hash_key)

    # Buscar si la key esta en el bucket
    current_nodo = bucket["first"]
    while current_nodo != None and not llave_existe:
        if (default_compare(key, current_nodo["info"]) == 0):
            llave_existe = True
        else:
            current_nodo = current_nodo["next"]

    return llave_existe



def remove(my_map, key):
    """
    Elimina una entrada de la tabla de simbolos asociada a una llave dada.

    Parameters:
        my_map (map_separate_chaining) – Tabla de simbolos de la cual se desea eliminar una entrada.

        key (any) – Llave de la entrada que se desea eliminar.

    Returns: Tabla de simbolos con la entrada eliminada.
    Return type: map_separate_chaining
    """
    # Variable Bool si llave existe
    llave_existe = False

    # Calcular hash de la llave
    hash_key = mf.hash_value(my_map, key)

    # Buscar la lista en la posicion del hash key
    bucket = lt.get_element(my_map["table"], hash_key)

    # Buscar si la key esta en el bucket
    current_nodo = bucket["first"]

    if (current_nodo == None):
        pass
    elif (default_compare(key, current_nodo["info"]) == 0):
        sl.remove_first(bucket)
        my_map["size"] -= 1
    else:
        while current_nodo["next"] != None and not llave_existe:
            if (default_compare(key, current_nodo["next"]["info"]) == 0):
                llave_existe = True
            else:
                current_nodo = current_nodo["next"]

        if llave_existe:
            current_nodo["next"] = current_nodo["next"]["next"]
            my_map["size"] -= 1

    # Se actualiza el current_factor de la tabla si se agrega una nueva entrada.
    my_map["current_factor"] = my_map["size"]/my_map["capacity"]

    return my_map

def get(my_map, key):
    """
    Obtiene el valor asociado a una llave en la tabla de simbolos.

    Parameters:
        my_map (map_separate_chaining) – Tabla de simbolos de la cual se desea obtener el valor asociado a una llave.

        key (any) – Llave de la cual se desea obtener el valor asociado.

    Returns: Valor asociado a la llave en la tabla de simbolos.
    Return type: any
    """
    # Variable Bool si llave existe
    llave_existe = False

    # Calcular hash de la llave
    hash_key = mf.hash_value(my_map, key)

    # Buscar la lista en la posicion del hash key
    bucket = lt.get_element(my_map["table"], hash_key)

    # Buscar si la key esta en el bucket
    current_nodo = bucket["first"]
    while current_nodo != None and not llave_existe:
        if (default_compare(key, current_nodo["info"]) == 0):
            llave_existe = True
        else:
            current_nodo = current_nodo["next"]

    if (llave_existe):
        return me.get_value(current_nodo["info"])
    else:
        return None

def size(my_map):
    """
    Obtiene la cantidad de elementos en la tabla de simbolos.

    Parameters:
        my_map (map_separate_chaining) – Tabla de simbolos de la cual se desea obtener la cantidad de elementos.

    Returns: Cantidad de elementos en la tabla de simbolos.
    Return type: int
    """
    return my_map["size"]

def is_empty(my_map):
    """
    Verifica si la tabla de simbolos se encuentra vacia.

    Parameters:
        my_map (map_separate_chaining) – Tabla de simbolos de la cual se desea verificar si se encuentra vacia.

    Returns: True si la tabla se encuentra vacia, False en caso contrario.
    Return type: bool
    """
    return my_map["size"] < 1

def key_set(my_map):
    """
    Obtiene la lista de llaves de la tabla de simbolos.

    Parameters:
        my_map (map_separate_chaining) – Tabla de simbolos de la cual se desea obtener el conjunto de llaves.

    Returns: Lista de llaves de la tabla de simbolos.
    Return type:array_list
    """
    # Crear lista de keys
    lista_keys = lt.new_list()

    # Recorrer my_map["table"] y reinsertar elementos a nueva_tabla
    indice_map = 0
    while indice_map < my_map["capacity"]:
        bucket = lt.get_element(my_map["table"], indice_map)
        nodo = bucket["first"]

        while nodo != None:
            lt.add_last(lista_keys, me.get_key(nodo["info"]))
            nodo = nodo["next"]

        indice_map += 1

    return lista_keys

def value_set(my_map):
    """
    Obtiene la lista de valores de la tabla de simbolos.

    Parameters:
        my_map (map_separate_chaining) – Tabla de simbolos de la cual se desea obtener el conjunto de valores.

    Returns: Lista de valores de la tabla de simbolos.
    Return type: array_list
    """
     # Crear lista de values
    lista_values = lt.new_list()

    # Recorrer my_map["table"] y reinsertar elementos a nueva_tabla
    indice_map = 0
    while indice_map < my_map["capacity"]:
        bucket = lt.get_element(my_map["table"], indice_map)
        nodo = bucket["first"]

        while nodo != None:
            lt.add_last(lista_values, me.get_value(nodo["info"]))
            nodo = nodo["next"]

        indice_map += 1

    return lista_values

def rehash(my_map):
    """
    Realiza un rehashing de la tabla de simbolos.

    Para realizar un rehash se debe seguir los siguientes pasos:

        1. Crear una nueva tabla map_separate_chaining con capacity que sea el siguiente primo al doble del capacity actual.
        2. Recorrer la tabla actual y reinsertar cada elemento en la nueva tabla.
        3. Asignar la nueva tabla como la tabla actual.
        4. Retornar la tabla nueva.

    Parameters:
        my_map (map_separate_chaining) – Tabla de simbolos a la cual se le desea realizar un rehashing.

    Returns: Tabla de simbolos con un nuevo tamaño.
    Return type: map_separate_chaining
    """
    # Calcular siguiente primo y num_keys
    num_keys = 2*my_map["size"]

    # Crear una nueva tabla
    map_separate_chaining = new_map(num_keys, my_map["limit_factor"], my_map["prime"])

    # Recorrer my_map["table"] y reinsertar elementos a nueva_tabla
    for i in range(my_map["capacity"]):
        bucket = lt.get_element(my_map["table"], i)
        nodo = bucket["first"]

        while nodo != None:
            put(map_separate_chaining, me.get_key(nodo["info"]), me.get_value(nodo["info"]))
            nodo = nodo["next"]

    # Asignar la nueva tabla como la tabla actual
    for i in my_map:
        my_map[i] = map_separate_chaining[i]

    # Retornar la tabla nueva
    return my_map
