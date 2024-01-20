from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLineEdit,
    QLabel,
    QMenu,
    QTextEdit,
)
from PyQt5.QtGui import QPixmap
import sys


# Create the main window class
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the main window's title and initial size
        self.setWindowTitle("Contraption UI")
        self.setGeometry(100, 100, 800, 600)

        # Create a central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Create the main layout
        self.main_layout = QVBoxLayout()
        self.central_widget.setLayout(self.main_layout)

        # Create and set the menu bar
        menu_bar = self.menuBar()
        file_menu = QMenu("File", self)
        menu_bar.addMenu(file_menu)

        # Create a search bar
        search_bar = QLineEdit()
        search_bar.setPlaceholderText("Search...")
        self.main_layout.addWidget(search_bar)

        # Create the content area
        content_area = QHBoxLayout()

        # Left side - About a machine
        left_side = QVBoxLayout()
        machine_label = QLabel("About a machine")
        machine_image = QLabel()
        machine_image.setPixmap(QPixmap("p01.png"))  # Placeholder for the image
        machine_text = QTextEdit("Description of the machine...")
        left_side.addWidget(machine_label)
        left_side.addWidget(machine_image)
        left_side.addWidget(machine_text)
        content_area.addLayout(left_side)

        # Right side - About an inventor
        right_side = QVBoxLayout()
        inventor_label = QLabel("About an inventor")
        inventor_image = QLabel()
        inventor_image.setPixmap(QPixmap("p01.png"))  # Placeholder for the image
        inventor_text = QTextEdit("Biography of the inventor...")
        right_side.addWidget(inventor_label)
        right_side.addWidget(inventor_image)
        right_side.addWidget(inventor_text)
        content_area.addLayout(right_side)

        self.main_layout.addLayout(content_area)

        # Create the bottom area
        bottom_area = QVBoxLayout()
        hashtag_label = QLabel("#thisismycontraption")
        button_row = QHBoxLayout()
        for i in range(6):
            button = QPushButton(f"Button {i + 1}")
            button_row.addWidget(button)
        bottom_area.addWidget(hashtag_label)
        bottom_area.addLayout(button_row)
        self.main_layout.addLayout(bottom_area)


# Create the PyQt application
app = QApplication(sys.argv)

# Create the main window instance and show it
main_window = MainWindow()
main_window.show()

# Start the PyQt event loop
sys.exit(app.exec_())
