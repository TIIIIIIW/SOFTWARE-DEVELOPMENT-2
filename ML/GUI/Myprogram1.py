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

    def loadStockname(self):
        conn = sqlite3.connect('share.sqlite')
        cursor = conn.cursor()
        sqlquery = """SELECT DISTINCT Symbol 
                FROM Stock_price_day as SP 
                INNER JOIN Information as I 
                on I.SymbolId = SP.SymbolId;"""
        cursor.execute(sqlquery)

        listName = cursor.fetchall()
        self.listWidget_name.clear()

        for i in range(len(listName)):
            item= QtWidgets.QListWidgetItem(listName[i][0])
            self.listWidget_name.addItem(item)

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
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(190, 120, 973, 561))
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
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_loaddata = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_loaddata.setGeometry(QtCore.QRect(1090, 690, 75, 23))
        self.pushButton_loaddata.setObjectName("pushButton_loaddata")
        self.pushButton_loaddata.clicked.connect(self.loaddata)

        self.pushButton_set100 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_set100.setGeometry(QtCore.QRect(30, 120, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.pushButton_set100.setFont(font)
        self.pushButton_set100.setObjectName("pushButton_set100")
        self.pushButton_set100.clicked.connect(self.loadStockname)
        
        self.pushButton_Industry = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Industry.setGeometry(QtCore.QRect(30, 320, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.pushButton_Industry.setFont(font)
        self.pushButton_Industry.setObjectName("pushButton_Industry")
        self.pushButton_Data = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Data.setGeometry(QtCore.QRect(30, 220, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.pushButton_Data.setFont(font)
        self.pushButton_Data.setObjectName("pushButton_Data")
        self.listWidget_name = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_name.setGeometry(QtCore.QRect(290, 120, 791, 561))
        self.listWidget_name.setObjectName("listWidget_name")
        self.listWidget_name.raise_()
        self.tableWidget.raise_()
        self.label.raise_()
        self.pushButton_loaddata.raise_()
        self.pushButton_set100.raise_()
        self.pushButton_Industry.raise_()
        self.pushButton_Data.raise_()
        Prototype.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Prototype)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
        self.menubar.setObjectName("menubar")
        Prototype.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Prototype)
        self.statusbar.setObjectName("statusbar")
        Prototype.setStatusBar(self.statusbar)

        self.retranslateUi(Prototype)
        self.pushButton_Data.clicked.connect(self.tableWidget.show) # type: ignore
        self.pushButton_Data.clicked.connect(self.pushButton_loaddata.show) # type: ignore
        self.pushButton_set100.clicked.connect(self.tableWidget.hide) # type: ignore
        self.pushButton_set100.clicked.connect(self.pushButton_loaddata.hide) # type: ignore
        self.pushButton_Industry.clicked.connect(self.tableWidget.hide) # type: ignore
        self.pushButton_Industry.clicked.connect(self.pushButton_loaddata.hide) # type: ignore
        self.pushButton_set100.clicked.connect(self.listWidget_name.show) # type: ignore
        self.pushButton_Data.clicked.connect(self.listWidget_name.hide) # type: ignore
        self.pushButton_Industry.clicked.connect(self.listWidget_name.hide) # type: ignore
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
        self.pushButton_loaddata.setText(_translate("Prototype", "Load Data"))
        self.pushButton_set100.setText(_translate("Prototype", "SET100"))
        self.pushButton_Industry.setText(_translate("Prototype", "Industry"))
        self.pushButton_Data.setText(_translate("Prototype", "Data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Prototype = QtWidgets.QMainWindow()
    ui = Ui_Prototype()
    ui.setupUi(Prototype)
    Prototype.show()
    sys.exit(app.exec_())
