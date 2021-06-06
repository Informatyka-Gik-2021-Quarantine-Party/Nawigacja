import osmnx as ox
import networkx as nx
import plotly.graph_objects as go
import numpy as np

# Defining the map boundaries
#north, east, south, west = 52.371, 21.279, 52.094, 20.831

# Downloading the map as a graph object
#G = ox.graph_from_bbox(north, south, east, west, network_type='drive')
G = ox.load_graphml('wwaroads.graphml')

# define origin and desination locations
origin_point = (52.109, 21.213)
destination_point = (52.298, 20.906)

# get the nearest nodes to the locations
origin_node = ox.nearest_nodes(G, origin_point[1], origin_point[0])
destination_node = ox.nearest_nodes(G, destination_point[1], destination_point[0])

route = nx.shortest_path(G, origin_node, destination_node, weight='length')

# getting coordinates of the nodes

# we will store the longitudes and latitudes in following list
long = []
lat = []

for i in route:
    point = G.nodes[i]
    long.append(point['x'])
    lat.append(point['y'])


def plot_path(lat, long, origin_point, destination_point):
    """
    Given a list of latitudes and longitudes, origin
    and destination point, plots a path on a map

    Parameters
    ----------
    lat, long: list of latitudes and longitudes
    origin_point, destination_point: co-ordinates of origin
    and destination
    Returns
    -------
    Nothing. Only shows the map.
    """

    # adding the lines joining the nodes
    fig = go.Figure(go.Scattermapbox(
        name="Path",
        mode="lines",
        lon=long,
        lat=lat,
        marker={'size': 10},
        line=dict(width=4.5, color='blue')))

    # adding source marker
    fig.add_trace(go.Scattermapbox(
        name="Source",
        mode="markers",
        lon=[origin_point[1]],
        lat=[origin_point[0]],
        marker={'size': 12, 'color': "red"}))

    # adding destination marker
    fig.add_trace(go.Scattermapbox(
        name="Destination",
        mode="markers",
        lon=[destination_point[1]],
        lat=[destination_point[0]],
        marker={'size': 12, 'color': 'green'}))

    # getting center for plots:
    lat_center = np.mean(lat)
    long_center = np.mean(long)

    # defining the layout using mapbox_style
    fig.update_layout(mapbox_style="open-street-map", mapbox_center_lat=30, mapbox_center_lon=-80)
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0},
                      mapbox={
                          'center': {'lat': lat_center, 'lon': long_center},
                          'zoom': 13})

    fig.show()

def node_list_to_path(G, node_list):
    """
    Given a list of nodes, return a list of lines that together follow the path
    defined by the list of nodes.
    Parameters
    ----------
    G : networkx multidigraph
    route : list
        the route as a list of nodes
    Returns
    -------
    lines : list of lines given as pairs ( (x_start, y_start), (x_stop, y_stop) )
    """
    edge_nodes = list(zip(node_list[:-1], node_list[1:]))
    lines = []
    for u, v in edge_nodes:
        # if there are parallel edges, select the shortest in length
        data = min(G.get_edge_data(u, v).values(), key=lambda x: x['length'])

        # if it has a geometry attribute (ie, a list of line segments)
        if 'geometry' in data:
            # add them to the list of lines to plot
            xs, ys = data['geometry'].xy
            lines.append(list(zip(xs, ys)))
        else:
            # if it doesn't have a geometry attribute, the edge is a straight
            # line from node to node
            x1 = G.nodes[u]['x']
            y1 = G.nodes[u]['y']
            x2 = G.nodes[v]['x']
            y2 = G.nodes[v]['y']
            line = [(x1, y1), (x2, y2)]
            lines.append(line)
    return lines

# getting the list of coordinates from the path (which is a list of nodes)
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

# podobno czas podróży
# ox.add_edge_travel_times(G)
