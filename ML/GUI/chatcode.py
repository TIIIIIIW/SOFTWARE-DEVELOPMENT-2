from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QVBoxLayout
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()

        # Create a QLabel to display the selected item
        self.label = QLabel("Please select an item", self)

        # Create a QComboBox and populate it with some items
        self.comboBox = QComboBox(self)
        self.comboBox.addItems(["Item 1", "Item 2", "Item 3"])

        # Connect the currentIndexChanged signal to the update_label function
        self.comboBox.currentIndexChanged.connect(self.update_label)

        # Create a vertical layout and add the label and combo box to it
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.comboBox)

    def update_label(self):
        # Get the selected item and update the label with it
        selected_item = self.comboBox.currentText()
        self.label.setText(f"Selected item: {selected_item}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())