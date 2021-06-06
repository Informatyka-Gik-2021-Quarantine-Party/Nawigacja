import osmnx as ox
import networkx as nx
import plotly.graph_objects as go
import numpy as np

# załadowanie pliku z drogami dla Warszawy i okolicy
G = ox.load_graphml('wwaroads.graphml')

# adres i współrzędne punktu początkowego i końcowego
a = 'Marszałkowska 1'
origin_point = ox.geocode(f'{a}, Warsaw, Poland')
b = 'Złotej Wilgi 10'
destination_point = ox.geocode(f'{b}, Warsaw, Poland')

# otrzymanie najbliższych punktów do drogi dla punktu początkowego i końcowego
origin_node = ox.nearest_nodes(G, origin_point[1], origin_point[0])
destination_node = ox.nearest_nodes(G, destination_point[1], destination_point[0])

# otrzymanie najkrótszej drogi
route = nx.shortest_path(G, origin_node, destination_node, weight='length')

# otrzymanie współrzędnych skrzyżowań
long = []
lat = []
for i in route:
    point = G.nodes[i]
    long.append(point['x'])
    lat.append(point['y'])


def plot_path(lat, long, origin_point, destination_point):
    """
    Funkcja pokazująca mapę z trasą dla danych punktu początkowego i końcowego
    oraz współrzędnych skrzyżowań

    INPUT:
    lat, long         : [list]  : długości i szerokości geograficzne w listach
    origin_point      : [tuple] : współrzędne punktu początkowego
    destination_point : [tuple] : współrzędne punktu końcowego

    OUTPUT:
    Pokazanie mapy w plotly
    """

    # dodanie linii łączących punkty
    fig = go.Figure(go.Scattermapbox(
        name="Path",
        mode="lines",
        lon=long,
        lat=lat,
        marker={'size': 10},
        line=dict(width=4.5, color='blue')))

    # tworzenie stylu dla punktu początkowego na mapie
    fig.add_trace(go.Scattermapbox(
        name="Source",
        mode="markers",
        lon=[origin_point[1]],
        lat=[origin_point[0]],
        marker={'size': 12, 'color': "red"}))

    # tworzenie stylu dla punktu końcowego na mapie
    fig.add_trace(go.Scattermapbox(
        name="Destination",
        mode="markers",
        lon=[destination_point[1]],
        lat=[destination_point[0]],
        marker={'size': 12, 'color': 'green'}))

    # otrzymanie współrzędnych dla środka trasy
    lat_center = np.mean(lat)
    long_center = np.mean(long)

    # tworzenie stylu mapy
    fig.update_layout(mapbox_style="open-street-map", mapbox_center_lat=30, mapbox_center_lon=-80)
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0},
                      mapbox={
                          'center': {'lat': lat_center, 'lon': long_center},
                          'zoom': 13})

    fig.show()


def node_list_to_path(G, node_list):
    """
    Funkcja wywołująca listę z liniami pokrywających się z drogą
    dla danych współrzędnych skrzyżowań

    INPUT:
    G         : [graphml] : plik z drogami
    node_list : [list]    : lista ze współrzędnymi skrzyżowań przy drodze

    OUTPUT:
    lines : [list] : lista współrzędnych punktów pokrywających się z drogą
                     w formacie ((x_start, y_start), (x_stop, y_stop))
    """
    edge_nodes = list(zip(node_list[:-1], node_list[1:]))
    lines = []
    for u, v in edge_nodes:
        data = min(G.get_edge_data(u, v).values(), key=lambda x: x['length'])

        if 'geometry' in data:
            xs, ys = data['geometry'].xy
            lines.append(list(zip(xs, ys)))
        else:
            x1 = G.nodes[u]['x']
            y1 = G.nodes[u]['y']
            x2 = G.nodes[v]['x']
            y2 = G.nodes[v]['y']
            line = [(x1, y1), (x2, y2)]
            lines.append(line)
    return lines


lines = node_list_to_path(G, route)


long2 = []
lat2 = []

for i in range(len(lines)):
    z = list(lines[i])
    l1 = list(list(zip(*z))[0])
    l2 = list(list(zip(*z))[1])
    for j in range(len(l1)):
        long2.append(l1[j])
        lat2.append(l2[j])


plot_path(lat2, long2, origin_point, destination_point)

#routeG = ox.geocode('Marszałkowska 1, Warsaw, Poland')
#print(routeG)