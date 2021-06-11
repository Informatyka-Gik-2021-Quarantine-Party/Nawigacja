# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'probacombobox.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtWidgets

from PyQt5 import QtCore, QtWebEngineWidgets
import plotly.express as px

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nawigacja")
        self.resize(1165, 840)
        # Create a top-level layout
        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)
        # Create and connect the combo box to switch between pages
        self.pageCombo = QtWidgets.QComboBox()
        self.pageCombo.addItems(["Po adresie", "Po współrzędnych","Mapa"])
        self.pageCombo.activated.connect(self.switchPage)
        # Create the stacked layout
        self.stackedLayout = QtWidgets.QStackedLayout()
        # Create the first page
        self.page1 = QtWidgets.QWidget()
        self.page1Layout = QtWidgets.QFormLayout()
        self.page1Layout.addRow("Adres początkowy:", QtWidgets.QLineEdit())
        self.page1Layout.addRow("Adres końcowy:", QtWidgets.QLineEdit())
        self.page1.setLayout(self.page1Layout)
        self.stackedLayout.addWidget(self.page1)
        # Create the second page
        self.page2 = QtWidgets.QWidget()
        self.page2Layout = QtWidgets.QFormLayout()
        self.page2Layout.addRow("Fi", QtWidgets.QLineEdit())
        self.page2Layout.addRow("Lambda", QtWidgets.QLineEdit())
        self.page2.setLayout(self.page2Layout)
        self.stackedLayout.addWidget(self.page2)

        self.page3 = QtWidgets.QWidget()
        self.page3Layout = QtWidgets.QFormLayout()

        self.page3.setLayout(self.page3Layout)
        self.stackedLayout.addWidget(self.page3)


        self.frame = QtWidgets.QFrame()
        self.frame.setGeometry(QtCore.QRect(40, 100, 731, 451))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")


        # Add the combo box and the stacked layout to the top-level layout
        layout.addWidget(self.pageCombo)
        layout.addLayout(self.stackedLayout)


        self.button = QtWidgets.QPushButton('Szukaj trasy', self)
        self.button.setGeometry(QtCore.QRect(200, 100, 90, 40))
        self.browser = QtWebEngineWidgets.QWebEngineView(self)
        vlayout = QtWidgets.QVBoxLayout(self)
        vlayout.addWidget(self.button, alignment=QtCore.Qt.AlignHCenter)
        vlayout.addWidget(self.browser)

        self.button.clicked.connect(self.show_graph)

    def show_graph(self):
        df = px.data.tips()
        fig = px.box(df, x="day", y="total_bill", color="smoker")
        fig.update_traces(quartilemethod="exclusive") # or "inclusive", or "linear" by default
        self.browser.setHtml(fig.to_html(include_plotlyjs='cdn'))

    def switchPage(self):
        self.stackedLayout.setCurrentIndex(self.pageCombo.currentIndex())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())