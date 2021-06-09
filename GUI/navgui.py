# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'navgui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


import osmnx as ox
import networkx as nx
import plotly.graph_objects as go
import numpy as np
from math import sin, cos, sqrt, atan2, radians



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
    G         : [networkx.MultiDiGraph] : plik z drogami
    node_list : [list]                  : lista ze współrzędnymi skrzyżowań przy drodze

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

def show_map(G, a, b):
    origin_point = ox.geocode(f'{a}, Warsaw, Poland')
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

    # obliczenie długości trasy
    dist = 0
    R = 6373.0
    for i in range(len(long2) - 1):
        latA = radians(lat2[i])
        latB = radians(lat2[i + 1])
        lonA = radians(long2[i])
        lonB = radians(long2[i + 1])
        dlon = lonB - lonA
        dlat = latB - latA
        a = sin(dlat / 2) ** 2 + cos(latA) * cos(latB) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = R * c
        dist += distance


# załadowanie pliku z drogami dla Warszawy i okolicy
G = ox.load_graphml('wwaroads.graphml')


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(973, 562)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 30, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(160, 120, 121, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 170, 121, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 120, 111, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 170, 91, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(190, 220, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(50, 280, 181, 16))
        self.label_4.setObjectName("label_4")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(410, 20, 541, 521))
        self.widget.setObjectName("widget")

        self.pushButton.clicked.connect(self.show_path)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Nawigacja czy coś nwm"))
        self.label_2.setText(_translate("Dialog", "Punkt początkowy"))
        self.label_3.setText(_translate("Dialog", "Punkt końcowy"))
        self.pushButton.setText(_translate("Dialog", "Szukaj trasy..."))
        self.label_4.setText(_translate("Dialog", "Długość:"))

    def show_path(self):
        a = self.lineEdit_2.text()
        b = self.lineEdit.text()
        show_map(G, a, b)

if __name__=='__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
