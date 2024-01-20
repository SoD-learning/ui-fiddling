from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QMenu,
    QTextEdit,
    QGridLayout,
)
from PyQt5.QtGui import QPixmap
import sys


class CoastalCapitalWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Coastal Capital Partners UI")
        self.setGeometry(100, 100, 1024, 768)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout()
        self.central_widget.setLayout(self.main_layout)

        menu_bar = self.menuBar()
        file_menu = QMenu("File", self)
        menu_bar.addMenu(file_menu)

        # Logo and header section
        header_section = QHBoxLayout()
        logo_label = QLabel("Logo Here")
        # Assuming the logo is an image, use QLabel to display it
        logo_label.setPixmap(QPixmap("logo_p01.png"))  # Placeholder for the logo
        header_section.addWidget(logo_label)

        # Add horizontal navigation
        navigation_layout = QHBoxLayout()
        for i in range(5):
            nav_button = QPushButton(f"Nav {i+1}")
            navigation_layout.addWidget(nav_button)
        header_section.addLayout(navigation_layout)

        self.main_layout.addLayout(header_section)

        # Main content area
        content_area = QGridLayout()

        # This is where you add your content widgets, such as QLabel, QTextEdit, or custom widgets
        # For example, adding a QTextEdit for the main content description
        content_label = QLabel(
            "Coastal Capital Partners: Focused on Quality & Performance"
        )
        content_text = QTextEdit("Main content goes here...")
        content_area.addWidget(content_label, 0, 0, 1, 2)  # Span two columns
        content_area.addWidget(content_text, 1, 0, 1, 2)  # Span two columns

        # Placeholders for other content, such as images, blog posts, etc.
        image_placeholder = QLabel("Image Placeholder")
        image_placeholder.setPixmap(
            QPixmap("p01.png")
        )  # Placeholder for content images
        content_area.addWidget(image_placeholder, 0, 2)

        blog_post_placeholder = QLabel("Blog Post Placeholder")
        content_area.addWidget(blog_post_placeholder, 1, 2)

        self.main_layout.addLayout(content_area)

        # Footer section for copyright and contact info
        footer_section = QLabel("Copyright and Contact Info Here")
        self.main_layout.addWidget(footer_section)


app = QApplication(sys.argv)
coastal_window = CoastalCapitalWindow()
coastal_window.show()
sys.exit(app.exec_())
