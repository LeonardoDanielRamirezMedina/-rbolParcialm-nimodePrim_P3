# Árbol Parcial mínimo de Prim.  #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 3ER PARCIAL        #

#Tema: Simulador de  Árbol Parcial mínimo de Prim. - Aplicado en el mundo  

import heapq                        #Se importa la librería heapq para la implementación de la cola de prioridad
import matplotlib.pyplot as plt     #Se importa la librería matplotlib.pyplot para la visualización del grafo
import networkx as nx               #Se importa la librería networkx para la creación del grafo

def prim(graph):            #Se define la función prim que recibe como parámetro el gra
    start_vertex = list(graph.keys())[0]        #Se obtiene el primer vértice del grafo
    visited = set()                             #Se crea un conjunto vacío para almacenar los vértices visitados
    mst = []                                    #Se crea una lista vacía para almacenar el árbol de recubrimiento mínimo
    edges = [(0, start_vertex, start_vertex)]   #Se crea una lista con la tupla (0, vértice de inicio, vértice de inicio)
    
    while edges:                                    #Mientras la lista de bordes no esté vacía
        weight, from_vertex, to_vertex = heapq.heappop(edges)   #Se extrae el borde con menor peso
        
        if to_vertex not in visited:                        #Si el vértice de destino no ha sido visitado
            visited.add(to_vertex)                          #Se agrega el vértice de destino al conjunto de visitados
            mst.append((from_vertex, to_vertex, weight))            #Se agrega el borde al árbol de recubrimiento mínimo
            
            for next_vertex, next_weight in graph[to_vertex].items():   #Para cada vértice adyacente al vértice de destino
                if next_vertex not in visited:                          #Si el vértice adyacente no ha sido visitado
                    heapq.heappush(edges, (next_weight, to_vertex, next_vertex))    #Se agrega el borde a la cola de prioridad
    
    return mst      #Se retorna el árbol de recubrimiento mínimo

graph = {
    'Barrio 1': {'Barrio 2': 10, 'Barrio 3': 20},   #Se define el grafo como un diccionario de diccionarios
    'Barrio 2': {'Barrio 1': 10, 'Barrio 3': 5, 'Barrio 4': 15},
    'Barrio 3': {'Barrio 1': 20, 'Barrio 2': 5, 'Barrio 4': 10, 'Barrio 5': 25},
    'Barrio 4': {'Barrio 2': 15, 'Barrio 3': 10, 'Barrio 5': 30},
    'Barrio 5': {'Barrio 3': 25, 'Barrio 4': 30}
}

# Ejecución del algoritmo de Prim
mst = prim(graph)       #Se llama a la función prim con el grafo como parámetro

print("Árbol de Recubrimiento Mínimo (Tuberías de agua):")  #Se imprime el árbol de recubrimiento mínimo
for from_vertex, to_vertex, weight in mst[1:]:              #Para cada borde en el árbol de recubrimiento mínimo
    print(f"{from_vertex} - {to_vertex}: {weight} unidades de costo")   #Se imprime el borde con su peso

# Crear un grafo dirigido desde el diccionario
G = nx.Graph()                          #Se crea un grafo no dirigido
for start, edges in graph.items():      #Para cada vértice y sus bordes en el grafo
    for end, weight in edges.items():   #Para cada vértice adyacente y su peso
        G.add_edge(start, end, weight=weight)   #Se agrega un borde al grafo con su peso

# Posiciones de los nodos en un plano
pos = nx.spring_layout(G)           #Se obtiene la posición de los nodos en un plano

# Dibujar el grafo
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10, font_weight='bold')  

# Dibujar los bordes del MST con un color diferente
mst_edges = [(from_vertex, to_vertex) for from_vertex, to_vertex, weight in mst[1:]]    #Se obtienen los bordes del árbol de recubrimiento mínimo
nx.draw_networkx_edges(G, pos, edgelist=mst_edges, edge_color='red', width=2)       #Se dibujan los bordes del árbol de recubrimiento mínimo

# Etiquetas de peso en los bordes   
edge_labels = nx.get_edge_attributes(G, 'weight')               #Se obtienen los pesos de los bordes
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)   #Se dibujan las etiquetas de los pesos de los bordes

plt.title("Árbol de Recubrimiento Mínimo (Red de Tuberías de Agua)")    #Se agrega un título al grafo
plt.show()      #Se muestra el grafo
