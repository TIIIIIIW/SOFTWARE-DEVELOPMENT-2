import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView

app = QApplication(sys.argv)

# Create a window and a layout
window = QWidget()
layout = QVBoxLayout()

# Create a QWebEngineView widget
view = QWebEngineView()

# Add the QWebEngineView widget to the layout
layout.addWidget(view)

# Set the layout of the window
window.setLayout(layout)

# Load a webpage
view.load(QUrl("http://localhost:8050"))

# Show the window
window.show()

# Run the event loop
sys.exit(app.exec_())