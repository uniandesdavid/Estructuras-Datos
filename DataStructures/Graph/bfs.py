from DataStructures.Map import map_linear_probing as linear_map
from DataStructures.Graph import digraph
from DataStructures.Queue import queue
from DataStructures.Stack import stack


def bfs(my_graph, source):
    """
    Inicia un recorrido Breath First Seacrh (BFS) sobre el grafo a partir de un vertice inicial. Crea un mapa de visitados y posteriormente llama a la funcion auxiliar bfs_vertex.

    Parameters:

            my_graph (digraph) – El grafo a recorrer

            source (any) – Llave del vertice de inicio del recorrido.

    Returns: Mapa con la información de los vertices conectados a source (padre y distancia)
    Return type: map
    """
    visited_map = linear_map.new_map(digraph.size(my_graph), 0.5)

    if digraph.get_vertex(my_graph, source) is None:
        raise Exception("Vertice no existe")
        
    linear_map.put(visited_map, source, {"marked": True, "edge_from": None, "distance": 0})

        
    return bfs_vertex(my_graph, source, visited_map)

def bfs_vertex(my_graph, source, visited_map):
    """
    Función auxiliar para calcular un recorrido BFS usada por la función bfs.

    Parameters:

            my_graph (digraph) – El grafo a recorrer

            source (any) – Vertice de inicio del recorrido.

            visited_map (map) – Mapa para almacenar el recorrido

    Returns: El mapa actualizado con los vertices alcanzables
    Return type: map
    """
    cola = queue.new_queue()
            
    queue.enqueue(cola, source)   

    while not queue.is_empty(cola):
        vertice = queue.dequeue(cola)

        for i in digraph.adjacents(my_graph, vertice)["elements"]:
            if linear_map.get(visited_map, i) is None:
                linear_map.put(visited_map, i, {"marked": True, "edge_from": vertice, "distance": linear_map.get(visited_map, vertice)["distance"] + 1})
                queue.enqueue(cola, i)

    return visited_map


def has_path_to(key_v, visited_map):
    """
    Indica si existe un camino entre el vertice source y el vertice vertex a partir del mapa de recorrido.

    Precondición: Se debe haber ejecutado previamente la funcion bfs.

    Parameters:

            key_v (any) – Llave del vertice destino

            visited_map (map) – Mapa resultante del recorrido BFS

    Returns: True si existe un camino entre source y vertex, False en caso contrario
    Return type: bool
    """
    return linear_map.get(visited_map, key_v) is not None

def path_to(key_v, visited_map):
    """
    Retorna el camino entre el vertices source y el vertice vertex a partir del mapa de recorrido.

    Precondición: Se debe haber ejecutado previamente la funcion bfs.

    Parameters:

            key_v (any) – Llave del vertice destino

            visited_map (map) – Mapa resultante del recorrido BFS

    Returns: Una pila con el camino entre source y vertex. Si no existe camino retorna None.
    Return type: stack
    """
    llave = key_v
    vertice = linear_map.get(visited_map, key_v)

    if vertice is None:
        return None

    camino = stack.new_stack()

    while vertice["edge_from"] is not None:
        stack.push(camino, llave)
        llave = vertice["edge_from"]
        vertice = linear_map.get(visited_map, llave)

    return camino













