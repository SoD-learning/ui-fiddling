from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QMenu,
    QTextEdit,
)
from PyQt5.QtGui import QPixmap
import sys


class MuseumWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Museum of Life Sciences")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout()
        self.central_widget.setLayout(self.main_layout)

        menu_bar = self.menuBar()
        file_menu = QMenu("File", self)
        menu_bar.addMenu(file_menu)

        # Main content area
        content_area = QHBoxLayout()

        # Left side - About the trail
        left_side = QVBoxLayout()
        trail_label = QLabel("About the Trail")
        trail_image = QLabel()
        trail_image.setPixmap(QPixmap("p01.png"))  # Placeholder for the image
        trail_text = QTextEdit("Details about the trail...")
        left_side.addWidget(trail_label)
        left_side.addWidget(trail_image)
        left_side.addWidget(trail_text)
        content_area.addLayout(left_side)

        # Right side - About the Dino
        right_side = QVBoxLayout()
        dino_label = QLabel("About the Dino")
        dino_image = QLabel()
        dino_image.setPixmap(QPixmap("p01.png"))  # Placeholder for the image
        dino_text = QTextEdit("Information about the dino...")
        right_side.addWidget(dino_label)
        right_side.addWidget(dino_image)
        right_side.addWidget(dino_text)
        content_area.addLayout(right_side)

        # Adding content to the main layout
        self.main_layout.addLayout(content_area)

        # Side sections for navigation or additional information
        side_section = QVBoxLayout()
        navigation_label = QLabel("Navigation or Information")
        navigation_text = QTextEdit("Content goes here...")
        side_section.addWidget(navigation_label)
        side_section.addWidget(navigation_text)

        # Combine content and side sections
        combined_layout = QHBoxLayout()
        combined_layout.addLayout(content_area)
        combined_layout.addLayout(side_section)

        self.main_layout.addLayout(combined_layout)


app = QApplication(sys.argv)
museum_window = MuseumWindow()
museum_window.show()
sys.exit(app.exec_())
