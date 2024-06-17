# Árbol Parcial mínimo de Prim.  #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 3ER PARCIAL        #

#Tema: Simulador de  Árbol Parcial mínimo de Prim. - Aplicado en el mundo 
#El arbol parcial minimo de Prim es un algoritmo que se utiliza para encontrar el arbol de expansion minima en un grafo no dirigido y conectado.

import heapq                    #Se importa la librería heapq para la implementación de la cola de prioridad
import matplotlib.pyplot as plt #Se importa la librería matplotlib.pyplot para la visualización del grafo
import networkx as nx           #Se importa la librería networkx para la creación del grafo

def prim(graph):            #Se define la función prim que recibe como parámetro el grafo

    start_vertex = next(iter(graph))  # Tomar el primer vértice como inicio
    visited = set([start_vertex])       # Inicializar el conjunto de vértices visitados con el vértice de inicio
    edges = [(weight, start_vertex, to_vertex) for to_vertex, weight in graph[start_vertex].items()]    # Inicializar la cola de prioridad con las aristas del vértice de inicio
    heapq.heapify(edges)  # Convertir la lista de aristas en un montículo
    mst = []    # Inicializar el árbol de expansión mínima

    while edges:            # Mientras la cola de prioridad no esté vacía
        weight, from_vertex, to_vertex = heapq.heappop(edges)   # Extraer la arista con menor peso
        if to_vertex not in visited:    # Si el vértice de destino no ha sido visitado
            visited.add(to_vertex)      # Agregar el vértice de destino al conjunto de visitados
            mst.append((from_vertex, to_vertex, weight))    # Agregar la arista al árbol de expansión mínima

            for next_to_vertex, weight in graph[to_vertex].items(): # Para cada vértice adyacente al vértice de destino
                if next_to_vertex not in visited:                   # Si el vértice adyacente no ha sido visitado
                    heapq.heappush(edges, (weight, to_vertex, next_to_vertex))  # Agregar la arista a la cola de prioridad

    return mst              # Retornar el árbol de expansión mínima

# Creación del grafo con lugares visitados en el día a día
graph = {
    'Casa': {'Trabajo': 10, 'Gimnasio': 8},
    'Trabajo': {'Supermercado': 2, 'Cafetería': 5, 'Casa': 10},
    'Gimnasio': {'Cafetería': 3, 'Casa': 8},
    'Supermercado': {'Trabajo': 2},
    'Cafetería': {'Trabajo': 5, 'Gimnasio': 3}
}

# Aplicación del algoritmo de Prim para encontrar el árbol de expansión mínima
mst = prim(graph)   # Llamar a la función prim con el grafo como parámetro

# Visualización del árbol de expansión mínima (se omite el código de visualización)
print("Árbol de expansión mínima (MST):")   # Imprimir el árbol de expansión mínima
for edge in mst:    # Para cada arista en el árbol de expansión mínima
    print(edge)     # Imprimir la arista

# Crear un grafo vacío
G = nx.Graph()  

# Agregar aristas al grafo desde el MST
for from_vertex, to_vertex, weight in mst:  # Para cada arista en el árbol de expansión mínima
    G.add_edge(from_vertex, to_vertex, weight=weight)   # Agregar la arista al grafo con su peso

# Dibujar el grafo
pos = nx.spring_layout(G)  # Generar posiciones de nodos usando el algoritmo de Fruchterman-Reingold
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, edge_color='k', linewidths=1, font_size=15)      # Dibujar el grafo

# Dibujar los pesos de las aristas
edge_labels = nx.get_edge_attributes(G, 'weight')   # Obtener los pesos de las aristas
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)   # Dibujar los pesos de las aristas

plt.title("Árbol de Expansión Mínima (MST)")    # Establecer el título del gráfico
plt.axis('off')  # Ocultar los ejes para una mejor visualización
plt.show()          # Mostrar el gráfico