# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
import osmnx as ox
import networkx as nx
import plotly.graph_objects as go
import numpy as np
from geopy.distance import geodesic


def plot_path(lat, long, origin_point, destination_point, map_style):
    """
    Funkcja kreująca wykres z trasą dla danych punktu początkowego i końcowego
    oraz współrzędnych skrzyżowań

    INPUT:
    lat, long         : [list]  : długości i szerokości geograficzne w listach
    origin_point      : [tuple] : współrzędne punktu początkowego
    destination_point : [tuple] : współrzędne punktu końcowego

    OUTPUT:
    fig : [wykres]: wykres w Plotly
    """

    # dodanie linii łączących punkty
    fig = go.Figure(go.Scattermapbox(
        name="Trasa",
        mode="lines",
        lon=long,
        lat=lat,
        marker={'size': 10},
        line=dict(width=4.5, color='blue')))

    # tworzenie stylu dla punktu początkowego na mapie
    fig.add_trace(go.Scattermapbox(
        name="Początek",
        mode="markers",
        lon=[origin_point[1]],
        lat=[origin_point[0]],
        marker={'size': 12, 'color': "green"}))

    # tworzenie stylu dla punktu końcowego na mapie
    fig.add_trace(go.Scattermapbox(
        name="Koniec",
        mode="markers",
        lon=[destination_point[1]],
        lat=[destination_point[0]],
        marker={'size': 12, 'color': 'red'}))

    # otrzymanie współrzędnych dla środka trasy
    lat_center = np.mean(lat)
    long_center = np.mean(long)

    # tworzenie stylu mapy
    fig.update_layout(mapbox_style=map_style)
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0},
                      mapbox={
                          'center': {'lat': lat_center, 'lon': long_center},
                          'zoom': 11})

    return fig


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

def show_map(G, a, b, path_method, map_style):
    """
    Funkcja wprowadzająca dane do stworzenia mapy i obliczająca długość trasy

    INPUT:
    G           : [networkx.MultiDiGraph] : plik z drogami
    a           : [str]                   : adres lub nazwa miejsca pkt. początkowego
    b           : [str]                   : adres lub nazwa miejsca pkt. końcowego
    path_method : [str/bool]              : typ stylu drogi
    map_style   : [str]                   : typ mapy

    OUTPUT:
    fig  : [wykres] : wykres w Plotly
    dist : [float]  : długość drogi
    """
    origin_point = ox.geocode(f'{a}, Warsaw, Poland')
    destination_point = ox.geocode(f'{b}, Warsaw, Poland')

    # otrzymanie najbliższych punktów do drogi dla punktu początkowego i końcowego
    origin_node = ox.nearest_nodes(G, origin_point[1], origin_point[0])
    destination_node = ox.nearest_nodes(G, destination_point[1], destination_point[0])

    # otrzymanie najkrótszej drogi
    route = nx.shortest_path(G, origin_node, destination_node, weight=path_method)

    # otrzymanie współrzędnych skrzyżowań
    long = []
    lat = []
    for i in route:
        point = G.nodes[i]
        long.append(point['x'])
        lat.append(point['y'])

    lines = node_list_to_path(G, route)

    # otrzymanie współrzędnych dla każdego punktu załamania drogi
    long2 = []
    lat2 = []
    for i in range(len(lines)):
        z = list(lines[i])
        l1 = list(list(zip(*z))[0])
        l2 = list(list(zip(*z))[1])
        for j in range(len(l1)):
            long2.append(l1[j])
            lat2.append(l2[j])

    # stworzenie wykresu w Plotly
    fig = plot_path(lat2, long2, origin_point, destination_point, map_style)

    # obliczenie długości trasy
    dist = 0
    for i in range(len(long2) - 1):
        A = (lat2[i+1], long2[i+1])
        B = (lat2[i], long2[i])
        dist_one = geodesic(A, B).kilometers
        dist += dist_one

    return(fig, dist)


# załadowanie pliku z drogami dla Warszawy i okolicy
G = ox.load_graphml('wwaroads.graphml')


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1126, 647)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 30, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(150, 260, 231, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 310, 231, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 260, 111, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 310, 91, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(150, 360, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 420, 181, 16))
        self.label_4.setObjectName("label_4")
        self.widget = QtWebEngineWidgets.QWebEngineView(Dialog)
        self.widget.setGeometry(QtCore.QRect(410, 20, 691, 601))
        self.widget.setObjectName("widget")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(39, 130, 131, 101))
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(230, 129, 131, 101))
        self.groupBox_2.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(50, 160, 95, 20))
        self.radioButton.setObjectName("radioButton")

        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(50, 200, 95, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_3.setGeometry(QtCore.QRect(240, 160, 95, 20))
        self.radioButton_3.setObjectName("radioButton_3")

        self.radioButton_4 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_4.setGeometry(QtCore.QRect(240, 200, 95, 20))
        self.radioButton_4.setObjectName("radioButton_4")

        self.radioButton.setChecked(True)
        vbox = QtWidgets.QVBoxLayout(Dialog)
        vbox.addWidget(self.radioButton)
        vbox.addWidget(self.radioButton_2)
        self.groupBox.setLayout(vbox)

        self.radioButton_3.setChecked(True)
        vbox = QtWidgets.QVBoxLayout(Dialog)
        vbox.addWidget(self.radioButton_3)
        vbox.addWidget(self.radioButton_4)
        self.groupBox_2.setLayout(vbox)

        self.pushButton.clicked.connect(self.show_path)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def show_path(self):
        a = self.lineEdit.text()
        b = self.lineEdit_2.text()

        if self.radioButton.isChecked():
            path_method = 'length'
        elif self.radioButton_2.isChecked():
            path_method = None
        if self.radioButton_3.isChecked():
            map_style = "carto-positron"
        elif self.radioButton_4.isChecked():
            map_style = "stamen-terrain"

        if a == '' or b == '':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Proszę wpisać adres!')
            msg.setWindowTitle("Error")
            msg.exec_()
        elif a == b:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Proszę podać dwa różne adresy!')
            msg.setWindowTitle("Error")
            msg.exec_()
        else:
            try:
                # pokazanie wykresu w widżecie
                fig, dist = show_map(G, a, b, path_method, map_style)
                self.widget.setHtml(fig.to_html(include_plotlyjs='cdn'))
                self.label_4.setText(f"Długość: {dist:.2f} km")
            except ValueError:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText("Error")
                msg.setInformativeText('Zły adres! Spróbuj jeszcze raz.')
                msg.setWindowTitle("Error")
                msg.exec_()


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Nawigacja Warszawa"))
        self.label_2.setText(_translate("Dialog", "Punkt początkowy"))
        self.label_3.setText(_translate("Dialog", "Punkt końcowy"))
        self.pushButton.setText(_translate("Dialog", "Szukaj trasy"))
        self.label_4.setText(_translate("Dialog", "Długość:"))
        self.radioButton.setText(_translate("Dialog", "Najkrótsza"))
        self.radioButton_2.setText(_translate("Dialog", "Domyślna"))
        self.radioButton_3.setText(_translate("Dialog", "Ulice"))
        self.radioButton_4.setText(_translate("Dialog", "Teren"))
        self.groupBox.setTitle(_translate("Dialog", "Trasa"))
        self.groupBox_2.setTitle(_translate("Dialog", "Styl mapy"))


if __name__=='__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
