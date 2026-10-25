from DataStructures.Graph import dijsktra_structure
from DataStructures.Map import map_linear_probing as mp
from DataStructures.Priority_queue import priority_queue as pq
from DataStructures.Priority_queue import pq_entry
from DataStructures.List import array_list as lt
from DataStructures.Stack import stack
from DataStructures.Graph import dijsktra_structure
import DataStructures.Graph.digraph as gr
from DataStructures.Graph import vertex as vs

def dijkstra(my_graph, source):
    """
    Implementa el algoritmo de Dijkstra para encontrar los caminos mas baratos desde el vertice source hasta todos sus vertices alcanzables (a los que se pueda llegar).

    Parameters:

            my_graph (digraph) – El grafo de busqueda

            source (any) – La llave del vertice de inicio

            
    Solución:
        1. Iniciar la estructura Dijkstra para el Algoritmo de Dijkstra desde el vértice source
        2. Si el vértice source pertenece al grafo
        2.1 Agregar el vértice source en la TH ‘visited’ con las propiedades: marked False,
        dist_to 0.0 y con edge_from None
        2.2 Agregar el vértice source a la Min_PQ ‘pq’ con la prioridad 0.0
        2.3 Mientras la cola de prioridad No este vacía
        2.3.1 Obtener el vertice v con “mayor” prioridad de la MinPQ ‘pq’
        2.3.2 Marcar el vertice v (propiedad ‘marked’) en la TH ‘visited’
        2.3.3 Revisar cada adyacente w NO marcado de v:
        2.3.3.1 Si el costo hasta v + el arco al adyacente w es menor al costo actual a w:
        2.3.3.1.1 Actualizar el ‘Edge_from’ y el ‘dist_to’ del vertice w en la TH ‘visited’
        2.3.3.1.2 Agregar (si no existe) o Revisar si mejora (si existe) la prioridad del vertice w en la MinPQ ‘pq’
        3. Retornar la estructura Dijkstra con el resultado final

    Returns: Estructura resultante con la información para llegar a cada vertice alcanzable desde el vertice source aplicando Dijkstra
    Return type: dijsktra_structure
    """
    if not gr.contains_vertex(my_graph, source):
        raise Exception("Source vertex does not exist in graph")

    structure = dijsktra_structure.new_dijsktra_structure(
        source, gr.order(my_graph)
    )

    initial_info = {"dist": 0.0, "prev": None}
    mp.put(structure["visited"], source, initial_info)

    pq.insert(structure["pq"], 0.0, source)

    while not pq.is_empty(structure["pq"]):
        u = pq.remove(structure["pq"])

        u_info = mp.get(structure["visited"], u)
        dist_u = u_info["dist"]

        adjacents = gr.adjacents(my_graph, u)
        num_adj = lt.size(adjacents)

        for i in range(num_adj):
            v = lt.get_element(adjacents, i)

            u_vertex_obj = vs.get_key(gr.get_vertex(my_graph, u))  
            edge_obj = vs.get_edge(gr.get_vertex(my_graph, u), v)

            if edge_obj is None:
                continue  

            weight = edge_obj["weight"]
            new_dist = dist_u + weight

            v_already_in = mp.contains(structure["visited"], v)

            if v_already_in:
                v_info = mp.get(structure["visited"], v)
                old_dist = v_info["dist"]

                if new_dist < old_dist:
                    v_info["dist"] = new_dist
                    v_info["prev"] = u
                    mp.put(structure["visited"], v, v_info)

                    if pq.contains(structure["pq"], v):
                        pq.improve_priority(structure["pq"], new_dist, v)
                    else:
                        pq.insert(structure["pq"], new_dist, v)
            else:
                v_info = {"dist": new_dist, "prev": u}
                mp.put(structure["visited"], v, v_info)
                pq.insert(structure["pq"], new_dist, v)

    return structure

def dist_to(key_v, aux_structure):
    """
    Retorna el costo del camino para llegar del vertice source al vertice key_v.

    Parameters:

            key_v (any) – La llave del vertice destino

            aux_structure (dijsktra_structure) – La estructura de busqueda resultante de Dijkstra

    Returns: El costo total para llegar de source a vertex. Infinito si no existe camino
    Return type: float
    """
    if mp.contains(aux_structure["visited"], key_v):
        info = mp.get(aux_structure["visited"], key_v)
        return info["dist"]
    return 


def has_path_to(key_v, aux_structure):
    """
    Indica si hay camino entre source y key_v.

    Parameters:

            key_v (any) – La llave del vertice de destino

            aux_structure (dijsktra_structure) – La estructura de busqueda resultante de Dijkstra

    Returns: True si existe camino, False de lo contrario
    Return type: bool
    """
    return mp.contains(aux_structure["visited"], key_v)

def path_to(key_v, aux_structure):
    """
    Retorna el camino entre source y key_v en una pila.

    Parameters:

            key_v (any) – La llave del vertice de destino

            aux_structure (dijsktra_structure) – La estructura de busqueda resultante de Dijkstra

    Returns: Una pila con los vertices del camino entre source y vertex. None si no hay camino.
    Return type: stack
    """
    if not mp.contains(aux_structure["visited"], key_v):
        return None

    path = stack.new_stack()
    current = key_v
    while current is not None:
        stack.push(path, current)
        info = mp.get(aux_structure["visited"], current)
        current = info["prev"]

    return path



