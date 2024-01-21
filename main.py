import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget, QTableWidgetItem


class DBCoffee(QWidget):
    def __init__(self):
        super(DBCoffee, self).__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect('coffee.sqlite')
        self.open_db()

    def open_db(self):

        query = "SELECT * FROM coffee_specifications"
        rez = self.con.execute(query).fetchall()
        self.tableWidget.setColumnCount(len(rez[0]))
        self.tableWidget.setRowCount(len(rez))
        self.tableWidget.setHorizontalHeaderLabels(["ID", 'Название', 'Степень обжарки', 'Молотый', 'Описание',
                                                    'Цена', 'Объём'])
        for i, row1 in enumerate(rez):
            for j, vol in enumerate(row1):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(vol)))
        self.tableWidget.resizeColumnsToContents()

    def closeEvent(self, event):
        # При закрытии формы закроем и наше соединение
        # с базой данных
        self.con.close()



def except_hoock(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hoock
    app = QApplication(sys.argv)
    wnd = DBCoffee()
    wnd.show()
    sys.exit(app.exec())
