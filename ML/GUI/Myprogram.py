from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_Prototype(object):
    def loaddata(self):
        conn = sqlite3.connect('share.sqlite')
        cursor = conn.cursor()
        sqlquery = """SELECT SP."Date",SP.Open,Sp.High,SP.Low,SP.Close,SP.Volume,I.Symbol 
                FROM Stock_price_day as SP 
                INNER JOIN Information as I 
                on I.SymbolId = SP.SymbolId;
                """
        result = conn.execute(sqlquery)
        self.tableWidget.setRowCount(0)

        for row_num, row_data in enumerate(result):
            self.tableWidget.insertRow(row_num)
            for column_num, data in enumerate(row_data):
                self.tableWidget.setItem(row_num, column_num, QtWidgets.QTableWidgetItem(str(data)))

        conn.close()

    def setupUi(self, Prototype):
        Prototype.setObjectName("Prototype")
        Prototype.resize(1200, 800)
        Prototype.setMinimumSize(QtCore.QSize(1200, 800))
        Prototype.setMaximumSize(QtCore.QSize(1200, 800))
        Prototype.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(Prototype)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(190, 120, 973, 380))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 101, 51))
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(630, 530, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.loaddata)

        Prototype.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Prototype)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
        self.menubar.setObjectName("menubar")
        Prototype.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Prototype)
        self.statusbar.setObjectName("statusbar")
        Prototype.setStatusBar(self.statusbar)

        self.retranslateUi(Prototype)
        QtCore.QMetaObject.connectSlotsByName(Prototype)

    def retranslateUi(self, Prototype):
        _translate = QtCore.QCoreApplication.translate
        Prototype.setWindowTitle(_translate("Prototype", "Prototype"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Prototype", "Date"))
        self.tableWidget.setColumnWidth(0, 148)
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Prototype", "Open"))
        self.tableWidget.setColumnWidth(1, 139)
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Prototype", "High"))
        self.tableWidget.setColumnWidth(2, 139)
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Prototype", "Low"))
        self.tableWidget.setColumnWidth(3, 139)
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Prototype", "Close"))
        self.tableWidget.setColumnWidth(4, 139)
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Prototype", "Volume"))
        self.tableWidget.setColumnWidth(5, 139)
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Prototype", "Symbol"))
        self.tableWidget.setColumnWidth(6, 130)
        self.label.setText(_translate("Prototype", "SET"))
        self.pushButton.setText(_translate("Prototype", "Load Data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Prototype = QtWidgets.QMainWindow()
    ui = Ui_Prototype()
    ui.setupUi(Prototype)
    Prototype.show()
    sys.exit(app.exec_())
