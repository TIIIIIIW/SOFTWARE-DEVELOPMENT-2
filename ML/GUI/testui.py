from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QStackedWidget, QLabel)

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.stacked_widget.currentChanged.connect(self.set_button_state)
        self.next_button.clicked.connect(self.next_page)
        self.prev_button.clicked.connect(self.prev_page)


    def initUI(self):

        self.next_button = QPushButton('Next')
        self.prev_button = QPushButton('Previous')
        self.next_button.setEnabled(False)
        self.prev_button.setEnabled(False)
        self.stacked_widget = QStackedWidget()

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.prev_button)
        hbox.addWidget(self.next_button)

        vbox = QVBoxLayout()
        vbox.addWidget(self.stacked_widget)
        vbox.addLayout(hbox)

        self.setLayout(vbox)


    def set_button_state(self, index):
        self.prev_button.setEnabled(index > 0)
        n_pages = len(self.stacked_widget)
        self.next_button.setEnabled( index % n_pages < n_pages - 1)

    def insert_page(self, widget, index=-1):
        self.stacked_widget.insertWidget(index, widget)
        self.set_button_state(self.stacked_widget.currentIndex())

    def next_page(self):
        new_index = self.stacked_widget.currentIndex()+1
        if new_index < len(self.stacked_widget):
            self.stacked_widget.setCurrentIndex(new_index)

    def prev_page(self):
        new_index = self.stacked_widget.currentIndex()-1
        if new_index >= 0:
            self.stacked_widget.setCurrentIndex(new_index)

if __name__ == '__main__':

    app = QApplication([])
    ex = Example()
    for i in range(5):
        ex.insert_page(QLabel(f'This is page {i+1}'))
    ex.resize(400,300)
    ex.show()
    app.exec()