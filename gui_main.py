import sys
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QApplication, QPushButton, QWidget, QAction, QFormLayout, QGroupBox, QLabel, QTabWidget,QVBoxLayout,QLineEdit,QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from MariaDBintegration import *


class GUI(QMainWindow):
#GUI for MariaDBintegration
    def __init__(self):
        super().__init__()
        self.title = 'MariaDB (games)'
        self.left = 200
        self.top = 200
        self.width = 1000
        self.hight = 200
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.hight)

        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)

        self.show()

class MyTableWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        #initialize tabs
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()
        self.tab6 = QWidget()
        self.tabs.resize(1000,200)

        #add tabs
        self.tabs.addTab(self.tab1, "Insert Game")
        self.tabs.addTab(self.tab2, "Delete Game")
        self.tabs.addTab(self.tab3, "Show games table")
        self.tabs.addTab(self.tab4, "Insert Book")
        self.tabs.addTab(self.tab5, "Delete Book")
        self.tabs.addTab(self.tab6, "Show books table")


        #Create 1 Tab
        self.tab1.layout = QGridLayout(self)
        self.insertButton = QPushButton("Insert")
        self.nameField_game = QLineEdit(self)
        self.namelabel_game = QLabel("Name:")
        self.jahrField_game = QLineEdit(self)
        self.jahrlabel_game = QLabel("Jahr:")
        self.gerneField_game = QLineEdit(self)
        self.gernelabel_game = QLabel("Gerne:")
        self.consoleField_game = QLineEdit(self)
        self.consolelabel_game = QLabel("Console:")
        self.tab1.layout.addWidget(self.namelabel_game,1 ,0)
        self.tab1.layout.addWidget(self.nameField_game,1 ,1)
        self.tab1.layout.addWidget(self.jahrlabel_game,2 ,0)
        self.tab1.layout.addWidget(self.jahrField_game,2 ,1)
        self.tab1.layout.addWidget(self.gernelabel_game,3 ,0)
        self.tab1.layout.addWidget(self.gerneField_game,3 ,1)
        self.tab1.layout.addWidget(self.consolelabel_game,4 ,0)
        self.tab1.layout.addWidget(self.consoleField_game,4 ,1)
        self.tab1.layout.addWidget(self.insertButton,5 ,0)
        self.tab1.setLayout(self.tab1.layout)

        #Create 2 Tab
        self.tab2.layout = QGridLayout(self)
        self.deleteButton = QPushButton("Delete")
        self.idFelddel_game = QLineEdit(self)
        self.iddellabel_gane = QLabel("Id:")
        self.nameFielddel_game = QLineEdit(self)
        self.namelabeldel_game = QLabel("Name:")
        self.tab2.layout.addWidget(self.iddellabel_gane,1 ,0)
        self.tab2.layout.addWidget(self.idFelddel_game,1 ,1)
        self.tab2.layout.addWidget(self.namelabel_game,2 ,0)
        self.tab2.layout.addWidget(self.nameFielddel_game,2 ,1)
        self.tab2.layout.addWidget(self.deleteButton,3 ,0)
        self.tab2.setLayout(self.tab2.layout)

        #add tabs to Widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

        #buttons clicked
        self.insertButton.clicked.connect(self.insertclick)
        self.deleteButton.clicked.connect(self.deleteclick)

    @pyqtSlot()
    def insertclick(self):
        name = self.nameField_game.text()
        jahr = self.jahrField_game.text()
        gerne = self.gerneField_game.text()
        console = self.consoleField_game.text()
        MariaDBintegration.Insert_games(name, jahr, gerne, console)
        #QMessageBox(self,'Messege - test',"Insert Succesfull",QMessageBox.Ok)
    @pyqtSlot()
    def deleteclick(self):
        id = self.idFelddel_game.text()
        name = self.nameFielddel_game.text()
        MariaDBintegration.Delete_games(id, name)

def main():
    app = QApplication(sys.argv)
    ex = GUI()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
