# Árbol Parcial mínimo de Prim.  #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 3ER PARCIAL        #

#Tema: Simulador de  Árbol Parcial mínimo de Prim. - Aplicado en el trabajo

#Prim es un algoritmo voraz que encuentra un árbol de expansión mínima para un grafo no dirigido y conexo.

import heapq            #Se importa la librería heapq para la implementación de la cola de prioridad
import networkx as nx   #Se importa la librería networkx para la creación del grafo
import matplotlib.pyplot as plt #Se importa la librería matplotlib.pyplot para la visualización del grafo

def prim(graph):    #Se define la función prim que recibe como parámetro el grafo
    n = len(graph)  #Se obtiene el número de nodos en el grafo
    visited = [False] * n   #Se crea una lista de booleanos para almacenar los nodos visitados
    min_heap = [(0, 0)]  # (cost, start_node)
    mst_cost = 0    #Se inicializa el costo total del árbol de expansión mínima
    mst_edges = []  #Se inicializa la lista de aristas en el árbol de expansión mínima

    while min_heap:                 #Mientras la cola de prioridad no esté vacía
        cost, u = heapq.heappop(min_heap)   #Se extrae el nodo con menor costo
        if visited[u]:              #Si el nodo ya ha sido visitado
            continue                #Se continúa con la siguiente iteración
        visited[u] = True           #Se marca el nodo como visitado
        mst_cost += cost            #Se suma el costo al costo total del árbol de expansión mínima
        if cost != 0:  # Evitamos agregar la arista inicial con costo 0
            mst_edges.append((u, cost)) #Se agrega la arista al árbol de expansión mínima

        for v, weight in enumerate(graph[u]):   #Para cada nodo adyacente al nodo actual
            if not visited[v] and weight < float('inf'):    #Si el nodo no ha sido visitado y el peso es finito
                heapq.heappush(min_heap, (weight, v))       #Se agrega el nodo a la cola de prioridad

    return mst_cost, mst_edges                      #Se retorna el costo total y las aristas del árbol de expansión mínima

# Creación del grafo con lugares de interés en la ciudad
inf = float('inf')  # Representación de infinito
graph = [        # Matriz de adyacencia del grafo
    [0, 10, inf, 30, 15, inf],  # Ayuntamiento
    [10, 0, 25, inf, inf, 20],  # Hospital
    [inf, 25, 0, 10, inf, 30],  # Estación de Bomberos
    [30, inf, 10, 0, 5, inf],   # Escuela
    [15, inf, inf, 5, 0, 10],   # Estación de Policía
    [inf, 20, 30, inf, 10, 0]   # Parque
]

mst_cost, mst_edges = prim(graph)   # Llamar a la función prim con el grafo como parámetro
print(f"Costo total del MST: {mst_cost}")   # Imprimir el costo total del árbol de expansión mínima
print("Aristas en el MST (Nodo, Costo):")   # Imprimir las aristas en el árbol de expansión mínima
for node, cost in mst_edges:                # Para cada nodo y costo en las aristas del árbol de expansión mínima
    print(f"Nodo {node} con costo {cost}")  # Imprimir el nodo y el costo

# Mapeo de índices a lugares para una mejor legibilidad
lugares = ["Ayuntamiento", "Hospital", "Estación de Bomberos", "Escuela", "Estación de Policía", "Parque"]  #Se crea una lista con los nombres de los lugares

print("Conexiones en el MST:")  # Imprimir las conexiones en el árbol de expansión mínima
for node, cost in mst_edges:    # Para cada nodo y costo en las aristas del árbol de expansión mínima
    print(f"Construcción con costo {cost} para conectar a {lugares[node]}") # Imprimir la conexión con el costo y el lugar

# Creación del grafo usando networkx
G = nx.Graph()

# Añadir nodos con etiquetas
for i, lugar in enumerate(lugares):
    G.add_node(i, label=lugar)

# Añadir aristas del grafo original
for i in range(len(graph)):             # Para cada nodo en el grafo
    for j in range(i + 1, len(graph)):  # Para cada nodo adyacente al nodo actual
        if graph[i][j] < float('inf'):  # Si el peso de la arista es finito
            G.add_edge(i, j, weight=graph[i][j])    # Se agrega la arista al grafo con su peso

# Extraer las aristas del MST para resaltarlas
mst_edges_tuples = [(0, node) for node, cost in mst_edges]

# Crear un mapeo de nombres de nodos
pos = nx.spring_layout(G)   #Se obtiene la posición de los nodos en un plano
labels = {i: lugares[i] for i in range(len(lugares))}   #Se crea un diccionario con los nombres de los nodos

plt.figure(figsize=(12, 8)) #Se establece el tamaño de la figura

# Dibujar el grafo original con etiquetas
nx.draw(G, pos, labels=labels, with_labels=True, node_size=500, node_color="lightblue", font_size=10, font_weight="bold")   #Se dibuja el grafo original con etiquetas
nx.draw_networkx_edge_labels(G, pos, edge_labels={(i, j): G[i][j]['weight'] for i, j in G.edges}, font_size=8)              #Se dibujan las etiquetas de los pesos de las aristas
nx.draw_networkx_edges(G, pos, edgelist=mst_edges_tuples, width=2, edge_color='r', style='dashed')                      #Se dibujan las aristas del árbol de expansión mínima

# Mostrar el gráfico
plt.title("Red de Distribución de Fibra Óptica y su Árbol Parcial Mínimo")  #Se establece el título del gráfico
plt.show()  #Se muestra el gráfico
