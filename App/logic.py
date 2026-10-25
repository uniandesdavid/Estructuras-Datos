import time
import csv
import os
from DataStructures.Graph import digraph
from DataStructures.Graph import bfs
from DataStructures.List import array_list
from DataStructures.Map import map_linear_probing as linear_map
from DataStructures.Priority_queue import priority_queue
from DataStructures.Queue import queue
from DataStructures.Stack import stack


data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data'
csv.field_size_limit(2147483647)


def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    #TODO: Llama a las funciónes de creación de las estructuras de datos
    redSocial = digraph.new_graph(1000)
    return redSocial


# Funciones para la carga de datos

def load_data(catalog):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    tiempoInicial = get_time()
    basic, premium, mayorCiudadNombre = cargar_perfiles(catalog)
    cargar_conecciones(catalog)

    tiempoFinal = get_time()
    tiempo = delta_time(tiempoInicial, tiempoFinal)
    return tiempo, digraph.order(catalog), digraph.size(catalog), basic, premium, digraph.size(catalog)/digraph.order(catalog), mayorCiudadNombre

def cargar_perfiles(catalog):
    perfilesfile = data_dir + '/users_info_large.csv' #TODO: Cambiar a users_info_large.csv
    input_file = list(csv.DictReader(open(perfilesfile, encoding='utf-8'), delimiter=";"))[:-1]

    basic = 0
    premium = 0
    ciudades = linear_map.new_map(100, 0.5)

    mayorCiudadNombre = ""
    mayorCiudadCantidad = 0

    for perfil in input_file:
        perfil["USER_ID"] = int(float(perfil["USER_ID"]))
        perfil["AGE"] = int(float(perfil["AGE"]))
        perfil["LONGITUDE"] = float(perfil["LONGITUDE"])
        perfil["LATITUDE"] = float(perfil["LATITUDE"])
        perfil["FOLLOWERS"] = 0
        perfil["FOLLOWING"] = 0
        perfil["FRIENDS"] = linear_map.new_map(10, 0.5)

        if (perfil["USER_TYPE"] == 'basic'):
            basic += 1
        else:
            premium += 1
        
        listaHobbies = str(perfil["HOBBIES"])[1:-1].split(", ")
        hobbies = array_list.new_list()

        ciudad = linear_map.get(ciudades, perfil["CITY"])

        if ciudad is None:
            valoresCiudad = array_list.new_list()
            array_list.add_last(valoresCiudad, perfil["CITY"])
            array_list.add_last(valoresCiudad, 0)
            linear_map.put(ciudades, perfil["CITY"], valoresCiudad)


        ciudad = linear_map.get(ciudades, perfil["CITY"])
        array_list.change_info(ciudad, 1, array_list.get_element(ciudad, 1) + 1)

        if (array_list.get_element(ciudad, 1) > mayorCiudadCantidad):
            mayorCiudadNombre = array_list.get_element(ciudad, 0)
            mayorCiudadCantidad = array_list.get_element(ciudad, 1)
        

        for hobby in listaHobbies:
            array_list.add_last(hobbies, hobby[1:-1])

        perfil["HOBBIES"] = hobbies

        digraph.insert_vertex(catalog, perfil["USER_ID"], perfil)

    return basic, premium, mayorCiudadNombre
    

def cargar_conecciones(catalog):
    relacionesfile = data_dir + '/relationships_large.csv' #TODO: Cambiar a relationships_large.csv
    input_file = csv.DictReader(open(relacionesfile, encoding='utf-8'),  delimiter=";")

    for coneccion in input_file:
        coneccion["FOLLOWER_ID"] = int(float(coneccion["FOLLOWER_ID"]))
        coneccion["FOLLOWED_ID"] = int(float(coneccion["FOLLOWED_ID"]))

        digraph.add_edge(catalog, coneccion["FOLLOWER_ID"], coneccion["FOLLOWED_ID"])


        followed_info = digraph.get_vertex_information(catalog, coneccion["FOLLOWED_ID"])
        followed_info["FOLLOWERS"] = followed_info["FOLLOWERS"] + 1

            

        follower_info = digraph.get_vertex_information(catalog, coneccion["FOLLOWER_ID"])
        follower_info["FOLLOWING"] = follower_info["FOLLOWING"] + 1

        coneccionesEdges = digraph.edges_vertex(catalog, coneccion["FOLLOWED_ID"])
        
        indice = 0
        no_encontrado = True
        while indice < array_list.size(coneccionesEdges) and no_encontrado:
            if (array_list.get_element(coneccionesEdges, indice)["to"] == coneccion["FOLLOWER_ID"]):
                linear_map.put(followed_info["FRIENDS"], coneccion["FOLLOWER_ID"], coneccion["START_DATE"])
                linear_map.put(follower_info["FRIENDS"], coneccion["FOLLOWED_ID"], coneccion["START_DATE"])
                no_encontrado = False

            indice += 1




# Funciones de consulta sobre el catálogo


def req_1(catalog, id_a, id_b):
    """
    Retorna el resultado del requerimiento 1

    Dadas dos personas A y B de tipo “basic” se requiere obtener el camino de menor extensión
    para conectarlos.
    
    Los parámetros de entrada de este requisito son:
        - Cuenta (id del usuario) origen desde donde se iniciará búsqueda.
        - Cuenta (id del usuario) destino de la búsqueda.
    
    La información que se espera como resultado debe incluir lo siguiente:
        - Tiempo de ejecución del requerimiento.
        - Cantidad de las personas en la secuencia de la red entre las dos cuentas.
        - Detalles de la secuencia completa de conexión, desglosada en:
            o Id, alias y tipo de usuario de la cuenta de origen desde la cual se inicia la
              búsqueda.
            o Secuencia de cuentas intermedias entre la cuenta de origen y la cuenta destino.
              Cada cuenta de usuario debe incluir Id, alias y tipo de usuario.
            o Id, alias y tipo de usuario de la cuenta de destino final.
    """
    # TODO: Modificar el requerimiento 1
    tiempo_inicial = get_time()

    # Obtener la información de los usuarios
    usuario_a = digraph.get_vertex_information(catalog, id_a)
    usuario_b = digraph.get_vertex_information(catalog, id_b)

    # Verificar que ambos existan
    if usuario_a is None or usuario_b is None:
        tiempo = delta_time(tiempo_inicial, get_time())
        return tiempo, 0, None, None, None

    # Verificar que ambos sean tipo basic
    if usuario_a["USER_TYPE"] != "basic" or usuario_b["USER_TYPE"] != "basic":
        tiempo = delta_time(tiempo_inicial, get_time())
        return tiempo, 0, None, usuario_a, usuario_b

    # Ejecutar BFS
    tabla_bfs = bfs.bfs(catalog, id_a)

    # Obtener el camino
    camino = bfs.path_to(id_b, tabla_bfs)

    # Verificar si existe camino
    if camino is None:
        tiempo = delta_time(tiempo_inicial, get_time())
        return tiempo, 0, None, usuario_a, usuario_b

    secuencia = array_list.new_list()

    # Recorrer la pila
    while not stack.is_empty(camino):

        id_usuario = stack.pop(camino)

        info = digraph.get_vertex_information(catalog, id_usuario)

        datos = array_list.new_list()
        array_list.add_last(datos, info["USER_ID"])
        array_list.add_last(datos, info["USER_NAME"])   
        array_list.add_last(datos, info["USER_TYPE"])

        array_list.add_last(secuencia, datos)

    cantidad_personas = array_list.size(secuencia)  + 2 

    tiempo = delta_time(tiempo_inicial, get_time())

    return tiempo, cantidad_personas, secuencia, usuario_a, usuario_b


def req_2(catalog, id_A):
    """
    Retorna el resultado del requerimiento 2

    Tenga en cuenta que no se debe considerar el tipo de cuenta para realizar esta búsqueda.
    
    Los parámetros de entrada de este requerimiento son:
        - Cuenta (id del usuario) desde donde se iniciará búsqueda.
      
    La respuesta esperada debe contener la siguiente información:
        - El tiempo en que se demora el algoritmo en encontrar la solución.
        - El amigo de A más popular según su cantidad de seguidores (incluyendo la cuenta de
          inicio de la búsqueda).
        - Cantidad total de los seguidores del amigo de A más popular
    """
    # TODO: Modificar el requerimiento 2
    
    tiempo_inicial = get_time()
    
    informacion_A = digraph.get_vertex_information(catalog, id_A)
    amigos_A = linear_map.key_set(informacion_A["FRIENDS"])
    usuario_mas_popular = informacion_A
    mayor_cantidad_seguidores = informacion_A["FOLLOWERS"]

    for id_amigo in amigos_A["elements"]:

        informacion_amigo = digraph.get_vertex_information(catalog,id_amigo)
        seguidores_amigo = informacion_amigo["FOLLOWERS"]

        if seguidores_amigo > mayor_cantidad_seguidores:
            
            usuario_mas_popular = informacion_amigo
            mayor_cantidad_seguidores = seguidores_amigo

    informacion_resultado = array_list.new_list()

    array_list.add_last(informacion_resultado,usuario_mas_popular["USER_ID"])
    array_list.add_last(informacion_resultado,usuario_mas_popular["USER_NAME"])
    array_list.add_last(informacion_resultado,usuario_mas_popular["USER_TYPE"])

    tiempo_final = get_time()
    tiempo = delta_time(tiempo_inicial, tiempo_final)

    return tiempo, informacion_resultado, mayor_cantidad_seguidores

def req_3(catalog, id_A, id_B):
    """
    Retorna el resultado del requerimiento 3

    Dado dos usuarios A y B, se requiere el listado de amigos en común, es decir los amigos de A
    que también son amigos de B.

    Los parámetros de entrada de este Requisito son:
        - Cuenta (id del usuario) A.
        - Cuenta (id del usuario) B.
    
    La respuesta esperada debe contener la siguiente información:
        - El tiempo en que se demora el algoritmo en encontrar la solución.
        - El listado de amigos en común, el cual debe contener la siguiente información: id del
          usuario, nombre del usuario y tipo de usuario.
    """
    # TODO: Modificar el requerimiento 3
    tiempo_inicial = get_time()

    id_A_info = digraph.get_vertex_information(catalog, id_A)
    id_B_info = digraph.get_vertex_information(catalog, id_B)

    id_A_amigos_lista = linear_map.key_set(id_A_info["FRIENDS"])

    id_B_amigos_mapa = id_B_info["FRIENDS"]

    amigos_comun = array_list.new_list()

    for amigoA in id_A_amigos_lista["elements"]:
        if linear_map.get(id_B_amigos_mapa, amigoA) is not None:
            amigo_compartido = digraph.get_vertex_information(catalog, amigoA)


            informacion_amigo_compartido = array_list.new_list()
            array_list.add_last(informacion_amigo_compartido, amigo_compartido["USER_ID"])
            array_list.add_last(informacion_amigo_compartido, amigo_compartido["USER_NAME"])
            array_list.add_last(informacion_amigo_compartido, amigo_compartido["USER_TYPE"])

            array_list.add_last(amigos_comun, informacion_amigo_compartido)

    tiempo_final = get_time()
    tiempo = delta_time(tiempo_inicial, tiempo_final)

    return tiempo, amigos_comun


def req_4(catalog, id, numero_amigos):
    """
    Retorna el resultado del requerimiento 4

    Dado un usuario A, se desea saber cuáles son las N amigos que siguen a más usuarios en la
    aplicación.
    
    Los parámetros de entrada de este requisito son:
        - El id del usuario que quiere consultar
        - El número de amigos que siguen a más personas. Este debe ser un número entero
          mayor o igual a 1.
    
    La respuesta esperada debe contener la siguiente información:
        - El tiempo que se demora el algoritmo en encontrar la solución.
        - Las N cuentas (detallando Id y nombre) amigos de A que siguen a más usuarios en la
          red. Cada cuenta de incluir la cantidad de seguidores
    """
    # TODO: Modificar el requerimiento 4
    tiempo_inicial = get_time()
    amigos = linear_map.key_set(digraph.get_vertex_information(catalog, id)["FRIENDS"])

    cola_prioridad = priority_queue.new_heap(is_min_pq=False)

    for amigo in amigos["elements"]:
        amigo_info = digraph.get_vertex_information(catalog, amigo)
        prioridad_por_seguidos = amigo_info["FOLLOWING"]

        amigo_info_lista = array_list.new_list()
        array_list.add_last(amigo_info_lista, amigo_info["USER_ID"])
        array_list.add_last(amigo_info_lista, amigo_info["USER_NAME"])
        array_list.add_last(amigo_info_lista, amigo_info["FOLLOWERS"])


        priority_queue.insert(cola_prioridad, prioridad_por_seguidos, amigo_info_lista)

    lista_amigos_que_mas_siguen = array_list.new_list()
    contador = 0
    while contador < numero_amigos and (not priority_queue.is_empty(cola_prioridad)):
        array_list.add_last(lista_amigos_que_mas_siguen, priority_queue.remove(cola_prioridad))
        contador += 1

    tiempo_final = get_time()
    tiempo = delta_time(tiempo_inicial, tiempo_final)

    return tiempo, lista_amigos_que_mas_siguen



def req_5(catalog, numero_populares):
    """
    Retorna el resultado del requerimiento 5

    Se desea obtener los N usuarios más populares (es decir, los que tienen más seguidores) y
    definir si existe un árbol que conecte a esos N usuarios.

    Los parámetros de entrada de este requerimiento son:
        - El número de usuarios más populares que se quiere consultar. Este será un número
          entero mayor o igual a dos.
    
    La respuesta esperada debe contener la siguiente información:
        - El tiempo que se demora el algoritmo en encontrar la solución.
        - Las N cuentas (detallando Id y nombre) más populares de la red. Cada cuenta debe
          incluir la cantidad de seguidores.
        - El árbol que conecte a esas N cuentas. La raı́z del árbol puede ser cualquier usuario de
          los N más populares.
    """
    # TODO: Modificar el requerimiento 5
    tiempo_inicial = get_time()

    usuarios = digraph.vertices(catalog)
    cola_popularidad = priority_queue.new_heap(is_min_pq=False)

    # Agregar todos los usuarios a la cola según sus seguidores
    for id_usuario in usuarios["elements"]:
        usuario_info = digraph.get_vertex_information(catalog,id_usuario)

        informacion_usuario = array_list.new_list()
        array_list.add_last(informacion_usuario,usuario_info["USER_ID"])
        array_list.add_last(informacion_usuario,usuario_info["USER_NAME"])
        array_list.add_last(informacion_usuario,usuario_info["FOLLOWERS"])

        priority_queue.insert(
            cola_popularidad,
            usuario_info["FOLLOWERS"],
            informacion_usuario
        )

    # Extraer los N usuarios con más seguidores
    usuarios_mas_populares = array_list.new_list()
    contador = 0

    while contador < numero_populares and not priority_queue.is_empty(cola_popularidad):
        usuario_popular = priority_queue.remove(cola_popularidad)
        array_list.add_last(usuarios_mas_populares,usuario_popular)

        contador += 1

    # Buscar uno de los usuarios populares que pueda alcanzar a todos
    existe_arbol = False
    raiz_arbol = None
    recorrido_raiz = None

    for candidato_raiz in usuarios_mas_populares["elements"]:
        if not existe_arbol:
            id_candidato = array_list.get_element(candidato_raiz,0)
            recorrido_candidato = bfs.bfs(catalog,id_candidato)

            conecta_a_todos = True

            for usuario_objetivo in usuarios_mas_populares["elements"]:
                id_objetivo = array_list.get_element(usuario_objetivo,0)

                if conecta_a_todos and not bfs.has_path_to(id_objetivo,recorrido_candidato):
                    conecta_a_todos = False

            if conecta_a_todos:
                existe_arbol = True
                raiz_arbol = candidato_raiz
                recorrido_raiz = recorrido_candidato

    # Lista que almacenará los arcos del árbol
    arbol_conexion = array_list.new_list()

    if existe_arbol:
        id_raiz = array_list.get_element(raiz_arbol,0)

        arcos_guardados = linear_map.new_map(array_list.size(usuarios_mas_populares) * 2, 0.5)

        # Construir el camino desde la raíz hacia cada usuario popular
        for usuario_destino in usuarios_mas_populares["elements"]:
            id_destino = array_list.get_element(usuario_destino,0)

            if id_destino != id_raiz:
                camino_inverso = array_list.new_list()
                id_actual = id_destino
                informacion_actual = linear_map.get(recorrido_raiz,id_actual)

                # Reconstruir el camino desde el destino hacia la raíz
                while informacion_actual["edge_from"] is not None:
                    array_list.add_last(camino_inverso,id_actual)

                    id_actual = informacion_actual["edge_from"]
                    informacion_actual = linear_map.get(recorrido_raiz,id_actual)

                id_padre = id_raiz

                # Recorrer el camino en el sentido raíz hacia destino
                for indice_camino in range(array_list.size(camino_inverso) - 1,-1,-1):
                    id_hijo = array_list.get_element(camino_inverso,indice_camino)

                    llave_arco = str(id_padre) + "->" + str(id_hijo)
                    arco_existente = linear_map.get(arcos_guardados,llave_arco)

                    if arco_existente is None:
                        informacion_padre = digraph.get_vertex_information(catalog,id_padre)
                        informacion_hijo = digraph.get_vertex_information(catalog,id_hijo)

                        informacion_arco = array_list.new_list()
                        array_list.add_last(informacion_arco,informacion_padre["USER_ID"])
                        array_list.add_last(informacion_arco,informacion_padre["USER_NAME"])
                        array_list.add_last(informacion_arco,informacion_hijo["USER_ID"])
                        array_list.add_last(informacion_arco,informacion_hijo["USER_NAME"])

                        array_list.add_last(arbol_conexion,informacion_arco)
                        linear_map.put(arcos_guardados,llave_arco,True)

                    id_padre = id_hijo

    tiempo_final = get_time()
    tiempo = delta_time(tiempo_inicial,tiempo_final)

    return tiempo, usuarios_mas_populares, existe_arbol, raiz_arbol, arbol_conexion, recorrido_raiz

def req_6(catalog, id, hobbies):
    """
    Retorna el resultado del requerimiento 6

    Se desea obtener una sub-red que conecte a los amigos de los amigos de un usuario A con
    intereses (hobbies) similares. En este caso la amistad también se considera implı́cita por
    transitividad, es decir, si A es amigo de B y B es amigo de C, A y C se consideran amigos
    implı́citos (sin necesidad de tener relación directa). A y B son amigos explı́citos a 1 arco de
    profundidad, B y C son amigos explı́citos a 1 arco de profundidad, A y C son amigos implı́citos
    a 2 arcos de profundidad.

    Los parámetros de entrada de este requisito son:
        - Cuenta (Id de usuario) de donde partirá la búsqueda.
        - El (los) hobbie(s) de interés para la búsqueda: array_list
    
    La respuesta esperada debe contener la siguiente información:
        - El tiempo que se demora el algoritmo en encontrar la solución.
        - La cantidad de amigos explı́citos e implı́citos de la cuenta A que se encontraron.
        - La siguiente información de cada uno de los amigos encontrados:
            o Nivel de profundidad (número de arcos de conexión a la cuenta A)
            o El(los) hobbie(s) en común con la cuenta A.
    """
    # TODO: Modificar el requerimiento 6
    tiempo_i = get_time()
    id_info = digraph.get_vertex_information(catalog, id)

    id_hobbies = id_info["HOBBIES"]


    # Crear la sub-red filtrada
    visited_map = bfs_amigos(catalog, id, hobbies)

    amigos_explicitos = 0
    amigos_implicitos = 0

    # Array list donode cada elemento tiene [id, profundidad, [hobbies en comun con A]]
    respuesta = array_list.new_list()

    keys = linear_map.key_set(visited_map)

    for key in keys["elements"]:
        hobbies_key = digraph.get_vertex_information(catalog, key)["HOBBIES"]

        hobbies_comun = array_list.new_list()

        for hobby in hobbies_key["elements"]:
            if hobby in id_hobbies["elements"]:
                array_list.add_last(hobbies_comun, hobby)

        profundidad = linear_map.get(visited_map, key)["distance"]

        if profundidad == 1:
            amigos_explicitos += 1
        elif profundidad == 2:
            amigos_implicitos += 1

        amigo_encontrado = array_list.new_list()

        array_list.add_last(amigo_encontrado, key)
        array_list.add_last(amigo_encontrado, profundidad)
        array_list.add_last(amigo_encontrado, hobbies_comun)

        array_list.add_last(respuesta, amigo_encontrado)

    tiempo_f = get_time()
    tiempo = delta_time(tiempo_i, tiempo_f)

    return tiempo, respuesta, amigos_explicitos, amigos_implicitos


    
    
    

def bfs_amigos(my_graph, source, hobbies):
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

        
    return bfs_vertex_amigos(my_graph, source, visited_map, hobbies)

def bfs_vertex_amigos(my_graph, source, visited_map, hobbies):
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
    distancia = 0

    while not queue.is_empty(cola) and distancia < 3:
        vertice = queue.dequeue(cola)

        amigos = linear_map.key_set(digraph.get_vertex_information(my_graph, vertice)["FRIENDS"])

        for i in amigos["elements"]:
            hobbies_i = digraph.get_vertex_information(my_graph, i)["HOBBIES"]
            if linear_map.get(visited_map, i) is None:
                if (linear_map.get(visited_map, vertice)["distance"] + 1 == 1):
                    linear_map.put(visited_map, i, {"marked": True, "edge_from": vertice, "distance": linear_map.get(visited_map, vertice)["distance"] + 1})
                    queue.enqueue(cola, i)
                else:
                    # Mirar si todos los hobbies se cumplen
                    cumpleHobbies = True

                    indice = 0
                    while indice < array_list.size(hobbies) and cumpleHobbies:
                        if array_list.get_element(hobbies, indice) not in hobbies_i["elements"]:
                            cumpleHobbies = False

                        indice += 1

                    if cumpleHobbies:
                        linear_map.put(visited_map, i, {"marked": True, "edge_from": vertice, "distance": linear_map.get(visited_map, vertice)["distance"] + 1})
                        queue.enqueue(cola, i)

        if not queue.is_empty(cola):
            distancia = linear_map.get(visited_map, queue.peek(cola))["distance"]

    linear_map.remove(visited_map, source)

    return visited_map
     


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
