from DataStructures.Map import map_linear_probing as linear_map
from DataStructures.Graph import digraph
from DataStructures.Stack import stack


def dfs(my_graph, source):
    """
    Inicia un recorrido Depth First Search (DFS) sobre el grafo my_graph a partir de un vertice inicial con llave source. Esta es la función máscara para iniciar el recorrido recursivo usando la funcion auxiliar dfs_vertex(…). Cada vertice alcanzable se agrega a un mapa con su llave y como valor un diccionarion con la informacion {“marked”, “edge_from”}.

    Parameters:

            my_graph (digraph) – El grafo a recorrer

            source (any) – Llave del vertice de inicio del recorrido.

    Returns: Una estructura para determinar los vertices conectados a source
    Return type: map
    """
    visited_map = linear_map.new_map(digraph.size(my_graph), 0.5)

    if digraph.get_vertex(my_graph, source) is None:
        raise Exception("Vertice no existe")
    
    linear_map.put(visited_map, source, {"marked": True, "edge_from": None})


    return dfs_vertex(my_graph, source, visited_map)


def dfs_vertex(my_graph, vertex, visited_map):
    """
    Funcion recursiva que permite obtener un recorrido DFS desde un vertice inicial. La funcion aplica a los vertices adyacentes del vertice inicial. Esta función es usada por la funcion depth_first_search. Cada vertice alcanzable se agrega a un mapa con su llave y como valor un diccionarion con la informacion {“marked”, “edge_from”}.

    Parameters:

            my_graph (digraph) – El grafo a recorrer

            vertex (any) – Llave del vertice de inicio del recorrido.

            visited_map (map) – Mapa que almacena las llaves de los vertices visitados.

    Returns: El mapa actualizado con los nuevos vertices visitados
    Return type: map
    """
    adyacentes = digraph.adjacents(my_graph, vertex)

    for adj in adyacentes["elements"]:
        if linear_map.get(visited_map, adj) is None:
             linear_map.put(visited_map, adj, {"marked": True, "edge_from": vertex})
             visited_map = dfs_vertex(my_graph, adj, visited_map)

    return visited_map
            

def has_path_to(key_v, visited_map):
    """
    Indica si existe un camino entre el vertice source y el vertice vertex a partir del mapa de recorrido.

    Precondición: Se debe haber ejecutado previamente la funcion dfs.

    Parameters:

            key_v (any) – Llave del vertice destino

            visited_map (map) – Mapa resultante del recorrido DFS

    Returns: True si existe un camino entre source y key_v, False en caso contrario
    Return type: bool
    """
    return linear_map.get(visited_map, key_v) is not None

def path_to(key_v, visited_map):
    """
    Retorna el camino entre los vertices con llaves source y key_v a partir del mapa de recorrido. Retorna None si No hay camino.

    Precondición

    Se debe haber ejecutado previamente la funcion dfs.

    Parameters:

            key_v (any) – Llave del vertice de destino

            visited_map (map) – Mapa resultante del recorrido DFS

    Returns: Una pila con el camino entre el vertices source y el vertice vertex
    Return type: stack
    """
    llave = key_v
    vertice = linear_map.get(visited_map, key_v)

    if vertice is None:
        return None

    camino = stack.new_stack()
    stack.push(camino, llave)

    while vertice["edge_from"] is not None:
        llave = vertice["edge_from"]
        stack.push(camino, llave)
        vertice = linear_map.get(visited_map, llave)

    return camino




