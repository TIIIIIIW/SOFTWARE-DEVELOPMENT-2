import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication

import sqlite3

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("PrototypeGUI.ui", self)
        self.tableWidget.setColumnWidth(0, 148)
        self.tableWidget.setColumnWidth(1, 139)
        self.tableWidget.setColumnWidth(2, 139)
        self.tableWidget.setColumnWidth(3, 139)
        self.tableWidget.setColumnWidth(4, 139)
        self.tableWidget.setColumnWidth(5, 139)
        self.tableWidget.setColumnWidth(6, 130)

    def loadData(self):
        conn = sqlite3.connect('share.sqlite')
        cursor = conn.cursor()
        sqlquery = """SELECT SP."Date",SP.Open,Sp.High,SP.Low,SP.Close,SP."Adj Close",SP.Volume,I.Symbol 
                FROM Stock_price_day as SP 
                INNER JOIN Information as I 
                on I.SymbolId = SP.SymbolId;
                """

        self.tableWidget.setRowCount(50)
        tablerow = 0
        for row in cursor.execute(sqlquery):
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[5]))
            self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(row[6]))
            tablerow+=1

#main
app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1200)
widget.setFixedHeight(800)
widget.show()
try:
    sys.exit(app.exec_())
except Exception as e:
    print("Exiting with exception:", e)