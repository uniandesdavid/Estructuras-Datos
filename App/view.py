import sys
import App.logic as logic
from DataStructures.List import array_list
from DataStructures.List import array_list
from DataStructures.Graph import digraph
from DataStructures.Graph import bfs
from DataStructures.Map import map_linear_probing as linear_map

def new_logic():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función de la lógica donde se crean las estructuras de datos
    return logic.new_logic()

def print_menu():
    print("Bienvenido")
    print("0- Cargar información")
    print("1- Ejecutar Requerimiento 1")
    print("2- Ejecutar Requerimiento 2")
    print("3- Ejecutar Requerimiento 3")
    print("4- Ejecutar Requerimiento 4")
    print("5- Ejecutar Requerimiento 5")
    print("6- Ejecutar Requerimiento 6")
    print("7- Salir")

def load_data(control):
    """
    Carga los datos

    Al completar la carga de datos de las relaciones y los usuarios se debe reportar los siguiente:
        - Número total de usuarios en la red
        - Número de conexiones entre los usuarios
        - Número de usuarios según su tipo (basic o premium)
        - Número promedio de seguidores por usuario
        - Ciudad en la que se encuentran mayores usuarios de la red social
    """
    #TODO: Realizar la carga de datos
    tiempo, usuarios, conecciones, basic, premium, promedioSeguidores, mayorCiudadNombre = logic.load_data(control)

    print("Carga de datos ejecutada en: " + str(tiempo))
    print("Numero de Usuarios: " + str(usuarios))
    print("Numero de conexiones: " + str(conecciones))
    print("Numero de Usuarios Basic: " + str(basic))
    print("Numero de Usuarios Premium: " + str(premium))
    print("Promedio de Seguidores por Usuario: " + str(promedioSeguidores))
    print("Ciudad mas comun entre usuarios: " + str(mayorCiudadNombre))
    print("\n")


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    print("\nUSTED ESCOGIÓ EL REQUERIMIENTO 1\n")

    print("""Dadas dos personas A y B de tipo basic se obtiene el camino de
menor extensión para conectarlas.\n""")

    id_a = int(input("Ingrese el ID del usuario A: "))
    id_b = int(input("Ingrese el ID del usuario B: "))

    print("\nEjecutando requerimiento...\n")

    tiempo, cantidad, secuencia, usuario_a, usuario_b = logic.req_1(control, id_a, id_b)

    print("Tiempo de ejecución: " + str(tiempo) + " milisegundos")
    print("Cantidad de personas en la secuencia: " + str(cantidad))

    if secuencia is None:
        print("\nNo existe un camino entre los usuarios o alguno no es de tipo basic.\n")
        return

    print("\nUSUARIO ORIGEN\n")
    print("ID: " + str(usuario_a["USER_ID"]))
    print("Nombre: " + str(usuario_a["USER_NAME"]))  
    print("Tipo: " + str(usuario_a["USER_TYPE"]))

    print("\nCUENTAS INTERMEDIAS\n")

    indice = 0
    while indice < array_list.size(secuencia):

        usuario = array_list.get_element(secuencia, indice)

        print("<<< Usuario #" + str(indice + 1) + " >>>")
        print("ID: " + str(array_list.get_element(usuario, 0)))
        print("Nombre: " + str(array_list.get_element(usuario, 1)))
        print("Tipo: " + str(array_list.get_element(usuario, 2)))
        print()

        indice += 1

    print("\nUSUARIO DESTINO\n")
    print("ID: " + str(usuario_b["USER_ID"]))
    print("Nombre: " + str(usuario_b["USER_NAME"]))   
    print("Tipo: " + str(usuario_b["USER_TYPE"]))



def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    print("\nUSTED ESCOGIÓ EL REQUERIMIENTO 2\n")
    print("""Dado un usuario A, se desea identificar cuál de sus amigos tiene la mayor cantidad de seguidores en la aplicación. La cuenta inicial también será considerada dentro de la búsqueda.\n""")

    id_usuario = int(input("Ingrese el ID del usuario que desea consultar: "))

    print("\nEjecutando requerimiento...\n")

    tiempo_ejecucion, usuario_mas_popular, cantidad_seguidores = logic.req_2(control,id_usuario)

    id_popular = array_list.get_element(usuario_mas_popular,0)
    nombre_popular = array_list.get_element(usuario_mas_popular,1)
    tipo_usuario = array_list.get_element(usuario_mas_popular,2)

    print("Tiempo de ejecución: " + str(tiempo_ejecucion) + " milisegundos")
    print("ID del usuario consultado: " + str(id_usuario))
    print("\nAMIGO MÁS POPULAR\n")
    print("ID: " + str(id_popular))
    print("Nombre: " + str(nombre_popular))
    print("Tipo de usuario: " + str(tipo_usuario))
    print("Cantidad de seguidores: " + str(cantidad_seguidores))

    print()


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    print("\nUSTED ESCOGIÓ EL REQUERIMIENTO 3\n")

    print("""Dado dos usuarios A y B, se requiere encontrar el listado de amigos
que tienen en común. Para cada amigo compartido se mostrará su identificador,
nombre y tipo de cuenta.\n""")

    id_usuario_a = int(input("Ingrese el ID del usuario A: "))
    id_usuario_b = int(input("Ingrese el ID del usuario B: "))

    print("\nEjecutando requerimiento...\n")

    tiempo_ejecucion, amigos_compartidos = logic.req_3(control,id_usuario_a,id_usuario_b)

    cantidad_amigos = array_list.size(amigos_compartidos)

    print("Tiempo de ejecución: " + str(tiempo_ejecucion) + " milisegundos")
    print("Usuario A: " + str(id_usuario_a))
    print("Usuario B: " + str(id_usuario_b))
    print("Cantidad de amigos en común: " + str(cantidad_amigos))

    if cantidad_amigos == 0:
        print("\nLos usuarios no tienen amigos en común.\n")

    else:
        print("\nLISTADO DE AMIGOS EN COMÚN\n")

        indice = 0

        while indice < cantidad_amigos:

            amigo = array_list.get_element(amigos_compartidos,indice)
            id_amigo = array_list.get_element(amigo,0)
            nombre_amigo = array_list.get_element(amigo,1)
            tipo_cuenta = array_list.get_element(amigo,2)

            print("<<< Amigo en común #" + str(indice + 1) + " >>>")
            print("ID: " + str(id_amigo))
            print("Nombre: " + str(nombre_amigo))
            print("Tipo de usuario: " + str(tipo_cuenta))

            print("\n")

            indice += 1


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    print("\nUSTED ESCOGIÓ EL REQUERIMIENTO 4\n")
    print("""Dado un usuario A, se desea identificar cuáles son los N amigos que siguen a más usuarios dentro de la aplicación.\n""")
    
    id_usuario = int(input("Ingrese el ID del usuario que desea consultar: "))
    numero_amigos = int(input("Ingrese la cantidad de amigos que desea mostrar: "))

    print("\nEjecutando requerimiento...\n")
    
    tiempo_ejecucion, amigos_que_mas_siguen = logic.req_4(control,id_usuario,numero_amigos)
    cantidad_encontrada = array_list.size(amigos_que_mas_siguen)

    print("Tiempo de ejecución: " + str(tiempo_ejecucion) + " milisegundos")
    print("ID del usuario consultado: " + str(id_usuario))
    print("Cantidad solicitada: " + str(numero_amigos))
    print("Cantidad de amigos encontrados: " + str(cantidad_encontrada))

    if cantidad_encontrada == 0:
        print("\nNo se encontraron amigos para el usuario consultado.\n")

    else:
        print("\nAMIGOS QUE SIGUEN A MÁS USUARIOS\n")

        indice = 0

        while indice < cantidad_encontrada:

            amigo = array_list.get_element(amigos_que_mas_siguen,indice)
            id_amigo = array_list.get_element(amigo,0)
            nombre_amigo = array_list.get_element(amigo,1)
            cantidad_seguidores = array_list.get_element(amigo,2)
            
            print("<<< Amigo #" + str(indice + 1) + " >>>")
            print("ID: " + str(id_amigo))
            print("Nombre: " + str(nombre_amigo))
            print("Cantidad de seguidores: " + str(cantidad_seguidores))

            print()

            indice += 1


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    print("\nUSTED ESCOGIÓ EL REQUERIMIENTO 5\n")

    print("""Se desea obtener los N usuarios más populares de la red, es decir, aquellos que tienenmás seguidores, y determinar si existe un árbol que conecte a todos esos usuarios.\n""")

    numero_populares = int(input("Ingrese la cantidad de usuarios populares que desea consultar: "))

    while numero_populares < 2:
        print("\nLa cantidad de usuarios debe ser mayor o igual a 2.\n")
        numero_populares = int(input("Ingrese nuevamente la cantidad de usuarios: "))

    print("\nEjecutando requerimiento...\n")

    tiempo_ejecucion, usuarios_populares, existe_arbol, raiz_arbol, arbol_conexion, arbol = logic.req_5(control,numero_populares)

    cantidad_usuarios = array_list.size(usuarios_populares)

    print("Tiempo de ejecución: " + str(tiempo_ejecucion) + " milisegundos")
    print("Cantidad de usuarios solicitados: " + str(numero_populares))
    print("Cantidad de usuarios encontrados: " + str(cantidad_usuarios))

    print("\nUSUARIOS MÁS POPULARES\n")

    indice = 0

    while indice < cantidad_usuarios:
        usuario = array_list.get_element(usuarios_populares,indice)

        id_usuario = array_list.get_element(usuario,0)
        nombre_usuario = array_list.get_element(usuario,1)
        seguidores_usuario = array_list.get_element(usuario,2)

        print("<<< Usuario Popular #" + str(indice + 1) + " >>>")
        print("ID: " + str(id_usuario))
        print("Nombre: " + str(nombre_usuario))
        print("Cantidad de Seguidores: " + str(seguidores_usuario))
        print("\n")

        indice += 1

    print("\nRESULTADO DEL ÁRBOL DE CONEXIÓN\n")

    if existe_arbol:
        id_raiz = array_list.get_element(raiz_arbol,0)
        nombre_raiz = array_list.get_element(raiz_arbol,1)
        seguidores_raiz = array_list.get_element(raiz_arbol,2)

        print("Sí existe un árbol que conecta a los usuarios más populares.")

        print("\nRAÍZ DEL ÁRBOL\n")
        print("ID: " + str(id_raiz))
        print("Nombre: " + str(nombre_raiz))
        print("Cantidad de Seguidores: " + str(seguidores_raiz))

        cantidad_arcos = array_list.size(arbol_conexion)

        print("\nCantidad de conexiones del árbol: " + str(cantidad_arcos))
        print("\nCONEXIONES DEL ÁRBOL\n")

        indice = 0

        while indice < cantidad_arcos:
            arco = array_list.get_element(arbol_conexion,indice)

            id_padre = array_list.get_element(arco,0)
            nombre_padre = array_list.get_element(arco,1)
            id_hijo = array_list.get_element(arco,2)
            nombre_hijo = array_list.get_element(arco,3)

            print("<<< Conexión #" + str(indice + 1) + " >>>")
            print(
                str(nombre_padre) + " (" + str(id_padre) + ") -> "
                + str(nombre_hijo) + " (" + str(id_hijo) + ")"
            )
            print("\n")

            indice += 1

    else:
        print("No existe un árbol dirigido que conecte a todos los usuarios más populares.")
    print("\n")


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    print("\nUSTED ESCOGIÓ EL REQUERIMIENTO 6\n")

    print("""Se desea obtener una sub-red que conecte a los amigos de los amigos de un usuario A con
        intereses (hobbies) similares. En este caso la amistad también se considera implı́cita por
        transitividad, es decir, si A es amigo de B y B es amigo de C, A y C se consideran amigos
        implı́citos (sin necesidad de tener relación directa). A y B son amigos explı́citos a 1 arco de
        profundidad, B y C son amigos explı́citos a 1 arco de profundidad, A y C son amigos implı́citos
        a 2 arcos de profundidad.\n""")

    id_usuario_a = int(input("Ingrese el ID del usuario A: "))

    hobbies = array_list.new_list()

    continuar = True
    while continuar:
        hobby = input("Ingrese el Hobby a filtrar: ")
        continuar_pregunta = input("Desea agregar otro hobby de restriccion? Y/N: ")

        if continuar_pregunta != "Y" or continuar_pregunta != "y":
            continuar = False

        array_list.add_last(hobbies, hobby)

    



    print("\nEjecutando requerimiento...\n")

    tiempo, respuesta, amigos_explicitos, amigos_implicitos = logic.req_6(control, id_usuario_a, hobbies)

    print("Tiempo de ejecución: " + str(tiempo) + " milisegundos")
    print("Amigos Explicitos: " + str(amigos_explicitos))
    print("Amigos Implicitos: " + str(amigos_implicitos))

    # [id, profundidad, [hobbies en comun con A]]
    for i in respuesta["elements"]:
        print("<<< ID " + str(array_list.get_element(i, 0)) + " >>>")
        print("Profundidad: " + str(array_list.get_element(i, 1)))

        hobbies = array_list.get_element(i, 2)

        print("--- Hobbies que se comparten con A ---")
        for h in hobbies["elements"]:
            print("\t" + str(h))

        print("\n")

    print("\n")
            
# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 0:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
        elif int(inputs) == 1:
            print_req_1(control)

        elif int(inputs) == 2:
            print_req_2(control)

        elif int(inputs) == 3:
            print_req_3(control)

        elif int(inputs) == 4:
            print_req_4(control)

        elif int(inputs) == 5:
            print_req_5(control)

        elif int(inputs) == 6:
            print_req_6(control)

        elif int(inputs) == 7:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
