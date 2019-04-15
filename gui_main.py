import sys
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QApplication, QPushButton, QWidget, QAction, QFormLayout, QGroupBox, QLabel, QTabWidget,QVBoxLayout,QLineEdit,QMessageBox, QPlainTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from MariaDBintegration import *


class GUI(QMainWindow):
# GUI for MariaDBintegration
    def __init__(self):
        super().__init__()
        self.title = 'MariaDB library'
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

        # initialize tabs
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()
        self.tab6 = QWidget()
        self.tabs.resize(1000, 500)

        # add tabs
        self.tabs.addTab(self.tab1, "Insert Game")
        self.tabs.addTab(self.tab2, "Delete Game")
        self.tabs.addTab(self.tab3, "Show games table")
        self.tabs.addTab(self.tab4, "Insert Book")
        self.tabs.addTab(self.tab5, "Delete Book")
        self.tabs.addTab(self.tab6, "Show books table")

        # Create 1 Tab
        self.tab1.layout = QGridLayout(self)
        self.labeltab1 = QLabel('Insert values for Game entry and click "Insert"')
        self.insertButton = QPushButton("Insert")
        self.nameField_game = QLineEdit(self)
        self.namelabel_game = QLabel("Name:")
        self.jahrField_game = QLineEdit(self)
        self.jahrlabel_game = QLabel("Jahr:")
        self.gerneField_game = QLineEdit(self)
        self.gernelabel_game = QLabel("Gerne:")
        self.consoleField_game = QLineEdit(self)
        self.consolelabel_game = QLabel("Console:")
        self.tab1.layout.addWidget(self.labeltab1, 5, 1)
        self.tab1.layout.addWidget(self.namelabel_game, 1, 0)
        self.tab1.layout.addWidget(self.nameField_game, 1, 1)
        self.tab1.layout.addWidget(self.jahrlabel_game, 2, 0)
        self.tab1.layout.addWidget(self.jahrField_game, 2, 1)
        self.tab1.layout.addWidget(self.gernelabel_game, 3, 0)
        self.tab1.layout.addWidget(self.gerneField_game, 3, 1)
        self.tab1.layout.addWidget(self.consolelabel_game, 4, 0)
        self.tab1.layout.addWidget(self.consoleField_game, 4, 1)
        self.tab1.layout.addWidget(self.insertButton, 5, 0)
        self.tab1.setLayout(self.tab1.layout)

        # Create 2 Tab
        self.tab2.layout = QGridLayout(self)
        self.labeltab2 = QLabel('Insert values for Game delete and click "Delete"')
        self.deleteButton = QPushButton("Delete")
        self.idFelddel_game = QLineEdit(self)
        self.iddellabel_gane = QLabel("Id:")
        self.nameFielddel_game = QLineEdit(self)
        self.namelabeldel_game = QLabel("Name:")
        self.tab2.layout.addWidget(self.labeltab2, 3, 1)
        self.tab2.layout.addWidget(self.iddellabel_gane, 1, 0)
        self.tab2.layout.addWidget(self.idFelddel_game, 1, 1)
        self.tab2.layout.addWidget(self.namelabeldel_game, 2, 0)
        self.tab2.layout.addWidget(self.nameFielddel_game, 2, 1)
        self.tab2.layout.addWidget(self.deleteButton, 3, 0)
        self.tab2.setLayout(self.tab2.layout)

        # create tab 3
        self.tab3.layout = QGridLayout(self)
        self.returngames = QPlainTextEdit()
        self.returnbutton_games = QPushButton("Reload")
        self.tab3.layout.addWidget(self.returngames)
        self.tab3.layout.addWidget(self.returnbutton_games)
        self.tab3.setLayout(self.tab3.layout)

        # create tab 4
        self.tab4.layout = QGridLayout(self)
        self.labeltab4 = QLabel('Insert values for Book entry and click "Insert"')
        self.insertButton_books = QPushButton("Insert")
        self.nameField_book = QLineEdit(self)
        self.namelabel_book = QLabel("Name:")
        self.authorField_book = QLineEdit(self)
        self.authorlabel_book = QLabel("Author:")
        self.jahrField_book = QLineEdit(self)
        self.jahrlabel_book = QLabel("Jahr:")
        self.volumeField_book = QLineEdit(self)
        self.volumelabel_book = QLabel("Volume:")
        self.langField_book = QLineEdit(self)
        self.langlabel_book = QLabel("Language:")
        self.tab4.layout.addWidget(self.labeltab4, 6, 1)
        self.tab4.layout.addWidget(self.namelabel_book, 1, 0)
        self.tab4.layout.addWidget(self.nameField_book, 1, 1)
        self.tab4.layout.addWidget(self.authorlabel_book, 2, 0)
        self.tab4.layout.addWidget(self.authorField_book, 2, 1)
        self.tab4.layout.addWidget(self.jahrlabel_book, 3, 0)
        self.tab4.layout.addWidget(self.jahrField_book, 3, 1)
        self.tab4.layout.addWidget(self.volumelabel_book, 4, 0)
        self.tab4.layout.addWidget(self.volumeField_book, 4, 1)
        self.tab4.layout.addWidget(self.langlabel_book, 5, 0)
        self.tab4.layout.addWidget(self.langField_book, 5, 1)
        self.tab4.layout.addWidget(self.insertButton_books, 6, 0)
        self.tab4.setLayout(self.tab4.layout)

        # create tab 5
        self.tab5.layout = QGridLayout(self)
        self.labeltab5 = QLabel('Insert values for Book delete and click "Delete"')
        self.deleteButton_book = QPushButton("Delete")
        self.idFelddel_book = QLineEdit(self)
        self.iddellabel_book = QLabel("Id:")
        self.nameFielddel_book = QLineEdit(self)
        self.namelabeldel_book = QLabel("Name:")
        self.tab5.layout.addWidget(self.labeltab5, 3, 1)
        self.tab5.layout.addWidget(self.iddellabel_book, 1, 0)
        self.tab5.layout.addWidget(self.idFelddel_book, 1, 1)
        self.tab5.layout.addWidget(self.namelabeldel_book, 2, 0)
        self.tab5.layout.addWidget(self.nameFielddel_book, 2, 1)
        self.tab5.layout.addWidget(self.deleteButton_book, 3, 0)
        self.tab5.setLayout(self.tab5.layout)

        # create tab 6
        self.tab6.layout = QGridLayout(self)
        self.returnbooks = QPlainTextEdit(self)
        self.returnbutton_books = QPushButton("Reload")
        self.tab6.layout.addWidget(self.returnbooks)
        self.tab6.layout.addWidget(self.returnbutton_books)
        self.tab6.setLayout(self.tab6.layout)

        # add tabs to Widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

        # buttons clicked
        self.insertButton.clicked.connect(self.insertclick)
        self.deleteButton.clicked.connect(self.deleteclick)
        self.insertButton_books.clicked.connect(self.insertclick_books)
        self.deleteButton_book.clicked.connect(self.deleteclick_books)
        self.returnbutton_games.clicked.connect(self.reloadtable_games)
        self.returnbutton_books.clicked.connect(self.reloadtable_books)

    # method for push of insert game button
    @pyqtSlot()
    def insertclick(self):
        name = self.nameField_game.text()
        jahr = self.jahrField_game.text()
        gerne = self.gerneField_game.text()
        console = self.consoleField_game.text()
        MariaDBintegration.Insert_games(name, jahr, gerne, console)
    # method for push of delete game button
    @pyqtSlot()
    def deleteclick(self):
        id = self.idFelddel_game.text()
        name = self.nameFielddel_game.text()
        MariaDBintegration.Delete_games(id, name)


    # method for push of insert book button
    @pyqtSlot()
    def insertclick_books(self):
        name = self.nameField_book.text()
        author = self.authorField_book.text()
        jahr = self.jahrField_book.text()
        volume = self.volumeField_book.text()
        lang = self.langField_book.text()
        MariaDBintegration.Insert_books(name, author, jahr, volume, lang)
    # method for push of delete book button
    @pyqtSlot()
    def deleteclick_books(self):
        id = self.idFelddel_book.text()
        name = self.nameField_book.text()
        MariaDBintegration.Delete_books(id, name)
    # method for reload games
    @pyqtSlot()
    def reloadtable_games(self):
        tempreturn = MariaDBintegration.Return_games()
        self.returngames.setPlainText(tempreturn)

    # method for reload books
    @pyqtSlot()
    def reloadtable_books(self):
        tempreturn = MariaDBintegration.Return_books()
        self.returnbooks.setPlainText(tempreturn)


def main():
    app = QApplication(sys.argv)
    ex = GUI()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
