from DataStructures.Graph import vertex
from DataStructures.Map import map_linear_probing as lp

def new_graph(order):
    """
    Crea un grafo dirigido vacio.

    Se crea un grafo con los siguientes atributos:

        vertices: Mapa con los vertices del grafo. Implementada como un mapa map_linear_probing con un tamaño inicial de order.

        num_edges: Numero de arcos del grafo. Inicializado en 0.

    Parameters:

        order (int) – Numero de vertices inicial del grafo.
    
    Returns: Grafo vacio (sin vertices ni arcos)
    Return type: digraph
    """
    orden = order
    if order < 1:
        return {"vertices": lp.new_map(1, 0.5), "num_edges": 0}
    return {"vertices": lp.new_map(orden, 0.5), "num_edges": 0}

def insert_vertex(my_graph, key_u, info_u):
    """
    Agrega un nuevo vertice al grafo my_graph.

    Se crea un nuevo vertice con la llave key_u, la informacion info_u y con los adyacentes vacio. Posteriomente, el vertice se agrega al mapa de vertices del grafo. Nota: Si el vertice existe, se reemplaza toda su informacion.

    Parameters:

            my_graph (digraph) – Grafo al que se le desea agregar el nuevo vertice

            key_u (any) – Llave del nuevo vertice

            info_u (any) – Informacion asociada al vertice

    Returns: El grafo con el nuevo vertice
    Return type: digraph
    """
    vertice = vertex.new_vertex(key_u, info_u)

    my_graph["vertices"] = lp.put(my_graph["vertices"], key_u, vertice)

    return my_graph

    

def add_edge(my_graph, key_u, key_v, weight=1.0):
    """
    Agrega un arco dirigido al grafo my_graph del vertice con llave key_u al vertice con llave key_v con peso weight.

    Se busca el vertice key_u en el grafo y se verifica si existe. Si no existe, se lanza una excepcion. Se busca el vertice key_v en el grafo y se verifica si existe. Si no existe, se lanza una excepcion. Si ambos vertices existen y el arco NO existe, se agrega el arco de key_u a key_v. Si el arco ya existe, se reemplaza el peso del arco (NO se aceptan arcos paralelos).

    Parameters:

            my_graph (digraph) – El grafo sobre el que se ejecuta la operacion

            key_u (any) – Llave del vertice de inicio

            key_v (any) – Llave del vertice destino

            weight (double) – Peso del arco, por defecto 1

    Returns: El grafo con el nuevo arco
    Return type: digraph
    """
    vertice_padre = lp.get(my_graph["vertices"], key_u)

    if vertice_padre is None:
        raise Exception("Vertice inicio no existe")

    vertice_hijo = lp.get(my_graph["vertices"], key_v)

    if vertice_hijo is None:
        raise Exception("Vertice destino no existe")
    
    adyacentes = vertex.get_adjacents(vertice_padre)
    ya_existe = lp.contains(adyacentes, key_v)

    vertice_padre = vertex.add_adjacent(vertice_padre, key_v, weight)
    
    if not ya_existe:
        my_graph["num_edges"] = size(my_graph) + 1

    return my_graph

def contains_vertex(my_graph, key_u):
    """
    Retorna si el vertice con llave ``key_u`` esta presente en el grafo.

    Parameters:

            my_graph (digraph) – El grafo sobre el cual consultar la existencia del vertice

            key_u (any) – Llave del vertice a buscar

    Returns: True si el vertice esta presente, False en caso contrario
    Return type: bool
    """
    return lp.contains(my_graph["vertices"], key_u)

def order(my_graph):
    """
    Retorna el orden del grafo, es decir, el numero de vertices del grafo my_graph.

    Parameters:

        my_graph (digraph) – El grafo sobre el que se ejecuta la operacion
    Returns: El numero de vertices del grafo
    Return type: int
    """
    return lp.size(my_graph["vertices"])

def size(my_graph):
    """
    Retorna el tamaño del grafo, es decir, el numero de arcos del grafo my_graph.

    Parameters:

        my_graph (digraph) – El grafo sobre el que se ejecuta la operacion
    Returns: El numero de arcos del grafo
    Return type: int
    """
    return my_graph["num_edges"]

def vertices(my_graph):
    """
    Retorna una lista con las llaves de todos los vertices del grafo my_graph.

    Parameters:

        my_graph (digraph) – El grafo sobre el que se ejecuta la operacion

    Returns: La lista con los vertices del grafo
    Return type: array_list
    """
    return lp.key_set(my_graph["vertices"])

def degree(my_graph, key_u):
    """
    Retorna el grado del vertice con llave key_u, es decir, el numero de arcos adyacentes al vertice.

    Si el vertice no existe, se lanza una excepcion.

    Parameters:

            my_graph (digraph) – El grafo sobre el que se ejecuta la operacion

            key_u (any) – Llave del vertice del que se desea conocer el grado

    Returns: El grado del vertice. Lanza una excepcion en caso de que el vertice no exista.
    Return type: int
    """
    vertice = lp.get(my_graph["vertices"], key_u)
    return vertex.degree(vertice)

def adjacents(my_graph, key_u):
    """
    Retorna una lista con las llaves de los vertices adyacentes al vertice vertex con llave key_u.

    Si el vertice no existe, se lanza una excepcion. Si el vertice existe, se retorna una lista con las llaves de los vertices adyacentes. Si el vertice no tiene vertices adyacentes, se retorna una lista vacia.

    Parameters:

            my_grph (digraph) – El grafo sobre el que se ejecuta la operacion

            key_u (any) – Llave del vertice del que se quiere la lista

    Returns: La lista de las llaves de sus vertices adyacentes (si tiene).
    Return type: array_list
    """
    vertice = lp.get(my_graph["vertices"], key_u)

    if vertice is None:
        raise Exception("El Vertice no existe")
    
    return lp.key_set(vertex.get_adjacents(vertice))

def edges_vertex(my_graph, key_u):
    """
    Retorna una lista con todos los arcos asociados a los vértices adyacentes del vertice con llave key_u.

    Si el vertice no existe, se lanza una excepcion. Si el vertice existe, se retorna una lista con los arcos asociados a los vertices adyacentes. Si el vertice no tiene arcos adyacentes, se retorna una lista vacia.

    Parameters:

            my_graph (digraph) – El grafo sobre el que se ejecuta la operacion

            key_u (any) – Llave del vértice del que se quiere la lista

    Returns: La lista de arcos adyacentes. Retorna una lista vacia en caso de que el vertice no exista.
    Return type: array_list
    """
    vertice = lp.get(my_graph["vertices"], key_u)

    if vertice is None:
        raise Exception("El Vertice no existe")
    
    return lp.value_set(vertex.get_adjacents(vertice))

def get_vertex(my_graph, key_u):
    """
    Retorna la informacion completa del vertice con llave key_u.

    Si el vertice no existe, se retorna None.

    Parameters:

            my_graph (digraph) – El grafo sobre el que se ejecuta la operacion

            key_u (any) – Llave del vertice del que se quiere la informacion completa

    Returns: El vertice buscado. Retorna None en caso de que el vertice no exista.
    Return type: vertex
    """

    return lp.get(my_graph["vertices"], key_u)
    


    

def update_vertex_info(my_graph, key_u, new_info_u):
    """
    Actualiza la información del vertice con llave key_u con la nueva información new_info_u.

    Se busca el vertice en el grafo y se actualiza su información. Si el vertice existe, se actualiza su información y se retorna el grafo actualizado. Si el vertice no existe, se retorna el grafo sin actualizar.

    Parameters:

            my_graph (digraph) – El grafo sobre el que se ejecuta la operacion

            key_u (any) – Llave del vertice que se desea actualizar

            new_info_u (any) – La nueva informacion asociada al vertice

    Returns: El grafo con la nueva informacion asociada al vertice (si existe)
    Return type: digraph
    """
    vertice = lp.get(my_graph["vertices"], key_u)

    if vertice is None:
        return my_graph
    
    vertice = vertex.set_value(vertice, new_info_u)

    return my_graph
    
    

def get_vertex_information(my_graph, key_u):
    """
    Retorna la informacion (value) asociada al vertice con llave key_u

    Si el vertice no existe, se lanza una excepcion.

    Parameters:

            my_graph (digraph) – El grafo sobre el que se ejecuta la operacion

            key_u (any) – Llave del vertice del que se quiere la informacion

    Returns: La informacion asociada al vertice.
    Return type: any
    """
    vertice = lp.get(my_graph["vertices"], key_u)

    if vertice is None:
        raise Exception("El Vertice no existe")
    
    return vertex.get_value(vertice)