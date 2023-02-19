import sys
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class CustomMainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(CustomMainWindow, self).__init__(*args, **kwargs)

        layout = QVBoxLayout()

        TW = QTabWidget()

        web1 = QWebEngineView()
        web1.load(QUrl("http://www.google.com"))
        

        web2 = QWebEngineView()
        web2.load(QUrl("http://www.google.com"))

        TW.addTab(web1, 'web1')
        TW.addTab(web2, 'web2')
        layout.addWidget(TW)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.resize(1131, 651)

app = QApplication(sys.argv)

CMWindow = CustomMainWindow() 
CMWindow.show()
sys.exit(app.exec ())