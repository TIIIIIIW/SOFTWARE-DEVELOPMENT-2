import sys
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

###############################
def combobox_value():
    conn = sqlite3.connect('newshare.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT Symbol FROM Information ORDER BY Symbol ASC")
    result = cursor.fetchall()
    values = [item[0] for item in result]
    return values
###############################

class Ui_MainWindow(object):

    ###############################
    def loadSet100(self):
        selected_item = self.comboBox_set100.currentText()
        conn = sqlite3.connect('newshare.sqlite')
        cursor = conn.cursor()
        sqlquery = f"""SELECT SP."Date",SP.Open,Sp.High,SP.Low,SP.Close,SP.Volume,I.Symbol 
                FROM Stock_price_day as SP 
                INNER JOIN Information as I 
                on I.SymbolId = SP.SymbolId
                WHERE Symbol = '{selected_item}'
                ORDER BY Date DESC
                LIMIT 150;
                """
        result = conn.execute(sqlquery)
        self.tableWidget_set100.setRowCount(0)

        for row_num, row_data in enumerate(result):
            self.tableWidget_set100.insertRow(row_num)
            for column_num, data in enumerate(row_data):
                self.tableWidget_set100.setItem(row_num, column_num, QtWidgets.QTableWidgetItem(str(data)))

        conn.close()

    def infoSet100(self):
        selected_item = self.comboBox_set100.currentText()
        conn = sqlite3.connect('newshare.sqlite')
        cursor = conn.cursor()
        sqlquery = f"""SELECT Symbol FROM Information WHERE Symbol = '{selected_item}'
                        UNION ALL
                        SELECT Market FROM Information WHERE Symbol = '{selected_item}'
                        UNION ALL
                        SELECT Short_Industry FROM Industry INNER JOIN Information ON Industry.IndustryId = Information.IndustryId WHERE Symbol = '{selected_item}'
                        UNION ALL
                        SELECT Full_Industry FROM Industry INNER JOIN Information ON Industry.IndustryId = Information.IndustryId WHERE Symbol = '{selected_item}'
                        UNION ALL
                        SELECT Short_Sector FROM Sector INNER JOIN Information ON Sector.SectorId = Information.SectorId WHERE Symbol = '{selected_item}'
                        UNION ALL
                        SELECT Full_Sector FROM Sector INNER JOIN Information ON Sector.SectorId = Information.SectorId WHERE Symbol = '{selected_item}'
                        UNION ALL
                        SELECT "Dividend Policy" FROM Information WHERE Symbol = '{selected_item}'
                        UNION ALL
                        SELECT "Business Type" FROM Information WHERE Symbol = '{selected_item}';
                """
        result = conn.execute(sqlquery)
        self.tableWidget_infoset100.setRowCount(8)
        for row_num, row_data in enumerate(result):
            for column_num, data in enumerate(row_data):
                self.tableWidget_infoset100.setItem(row_num, column_num, QtWidgets.QTableWidgetItem(str(data)))
        conn.close()
    ###############################

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1820, 980)
        MainWindow.setMinimumSize(QtCore.QSize(1820, 980))
        MainWindow.setMaximumSize(QtCore.QSize(1820, 980))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(120, -30, 1581, 202))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_set100 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_set100.setMinimumSize(QtCore.QSize(150, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_set100.setFont(font)
        self.pushButton_set100.setObjectName("pushButton_set100")
        self.horizontalLayout.addWidget(self.pushButton_set100)
        self.pushButton_nasdaq = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_nasdaq.setMinimumSize(QtCore.QSize(150, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_nasdaq.setFont(font)
        self.pushButton_nasdaq.setObjectName("pushButton_nasdaq")
        self.horizontalLayout.addWidget(self.pushButton_nasdaq)
        self.pushButton_crypto = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_crypto.setMinimumSize(QtCore.QSize(150, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_crypto.setFont(font)
        self.pushButton_crypto.setObjectName("pushButton_crypto")
        self.horizontalLayout.addWidget(self.pushButton_crypto)
        self.comboBox_set100 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_set100.setGeometry(QtCore.QRect(120, 150, 1341, 41))
        self.comboBox_set100.setObjectName("comboBox_set100")

        ###############################
        self.comboBox_set100.setEditable(True)
        self.comboBox_set100.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBox_set100.completer().setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        self.comboBox_set100.setFont(QtGui.QFont('Arial', 15))
        self.comboBox_set100.currentIndexChanged.connect(self.loadSet100)
        self.comboBox_set100.currentIndexChanged.connect(self.infoSet100)
        ###############################

        self.pushButton_loadset100 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_loadset100.setGeometry(QtCore.QRect(1500, 150, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_loadset100.setFont(font)
        self.pushButton_loadset100.setObjectName("pushButton_loadset100")
        self.pushButton_dataset100 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_dataset100.setGeometry(QtCore.QRect(120, 220, 81, 31))
        self.pushButton_dataset100.setObjectName("pushButton_dataset100")
        self.pushButton_infoset100 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_infoset100.setGeometry(QtCore.QRect(210, 220, 81, 31))
        self.pushButton_infoset100.setObjectName("pushButton_infoset100")
        self.tableWidget_set100 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_set100.setGeometry(QtCore.QRect(120, 280, 421, 651))
        self.tableWidget_set100.setObjectName("tableWidget_set100")
        self.tableWidget_set100.setColumnCount(7)
        self.tableWidget_set100.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_set100.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_set100.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_set100.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_set100.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_set100.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_set100.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_set100.setHorizontalHeaderItem(6, item)
        self.tableWidget_infoset100 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_infoset100.setGeometry(QtCore.QRect(120, 280, 421, 271))
        self.tableWidget_infoset100.setObjectName("tableWidget_infoset100")
        self.tableWidget_infoset100.setColumnCount(1)
        self.tableWidget_infoset100.setRowCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_infoset100.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_infoset100.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_infoset100.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_infoset100.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_infoset100.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_infoset100.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_infoset100.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_infoset100.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_infoset100.setHorizontalHeaderItem(0, item)
        self.tableWidget_infoset100.raise_()
        self.tableWidget_set100.raise_()
        self.horizontalLayoutWidget.raise_()
        self.comboBox_set100.raise_()
        self.pushButton_loadset100.raise_()
        self.pushButton_dataset100.raise_()
        self.pushButton_infoset100.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1820, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_dataset100.clicked.connect(self.tableWidget_set100.show) # type: ignore
        self.pushButton_dataset100.clicked.connect(self.tableWidget_infoset100.hide) # type: ignore
        self.pushButton_infoset100.clicked.connect(self.tableWidget_set100.hide) # type: ignore
        self.pushButton_infoset100.clicked.connect(self.tableWidget_infoset100.show) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ###############################
        layout = QtWidgets.QVBoxLayout(MainWindow)
        TW = QtWidgets.QTabWidget(MainWindow)

        web1 = QWebEngineView(MainWindow)
        web1.load(QUrl("http://127.0.0.1:8050/"))
        # web2 = QWebEngineView()
        # web2.load(QUrl("http://www.google.com"))

        TW.addTab(web1, 'Price&Volume Graph')
        # TW.addTab(web2, 'Other')
        layout.addWidget(TW)

        widget = QWidget(MainWindow)
        widget.setLayout(layout)
        widget.setGeometry(QtCore.QRect(570, 250, 1143, 690))
        ###############################

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_set100.setText(_translate("MainWindow", "SET100"))
        self.pushButton_nasdaq.setText(_translate("MainWindow", "NASDAQ"))
        self.pushButton_crypto.setText(_translate("MainWindow", "CRYPTO"))
        self.pushButton_loadset100.setText(_translate("MainWindow", "Update"))
        self.pushButton_dataset100.setText(_translate("MainWindow", "Data"))
        self.pushButton_infoset100.setText(_translate("MainWindow", "Information"))

        ###############################
        item = self.tableWidget_set100.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date"))
        self.tableWidget_set100.setColumnWidth(0, 130)
        item = self.tableWidget_set100.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Open"))
        self.tableWidget_set100.setColumnWidth(1, 130)
        item = self.tableWidget_set100.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "High"))
        self.tableWidget_set100.setColumnWidth(2, 130)
        item = self.tableWidget_set100.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Low"))
        self.tableWidget_set100.setColumnWidth(3, 130)
        item = self.tableWidget_set100.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Close"))
        self.tableWidget_set100.setColumnWidth(4, 130)
        item = self.tableWidget_set100.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Volume"))
        self.tableWidget_set100.setColumnWidth(5, 130)
        item = self.tableWidget_set100.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Symbol"))
        self.tableWidget_set100.setColumnWidth(6, 130)
        ###############################

        item = self.tableWidget_infoset100.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Symbol"))
        item = self.tableWidget_infoset100.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Market"))
        item = self.tableWidget_infoset100.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Industry Symbol"))
        item = self.tableWidget_infoset100.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Industry"))
        item = self.tableWidget_infoset100.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "Sector Symbol"))
        item = self.tableWidget_infoset100.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "Sector"))
        item = self.tableWidget_infoset100.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "Dividend Policy"))
        item = self.tableWidget_infoset100.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "Business Type"))
        item = self.tableWidget_infoset100.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Information"))
        self.tableWidget_infoset100.setColumnWidth(0, 320)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    ###############################
    ui.comboBox_set100.addItems(combobox_value())
    ###############################

    MainWindow.show()
    sys.exit(app.exec_())
