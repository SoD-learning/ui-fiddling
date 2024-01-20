from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QListWidget,
    QListWidgetItem,
    QStackedWidget,
    QGroupBox,
    QCheckBox,
)
import sys


class TemplateWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Category Activity UI")
        self.setGeometry(100, 100, 1024, 768)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout()
        self.central_widget.setLayout(self.main_layout)

        # Header section with tabs
        header_layout = QHBoxLayout()
        tabs = ["Tab1", "Tab2", "Tab3", "Tab4"]
        for tab in tabs:
            button = QPushButton(tab)
            header_layout.addWidget(button)
        self.main_layout.addLayout(header_layout)

        # Main content area with category list and details
        content_layout = QHBoxLayout()

        # Category list on the left
        self.category_list = QListWidget()
        categories = [
            "Film & Photo",
            "Exploration",
            "Cartoon",
            "Animation",
            "Sports",
            "Culinary Arts",
            "Outdoor & Adventure",
            "Other Category",
        ]
        for category in categories:
            QListWidgetItem(category, self.category_list)
        content_layout.addWidget(self.category_list)

        # Corresponding category details on the right
        self.details_stack = QStackedWidget()
        for category in categories:
            detail_group = self.create_detail_group(category)
            self.details_stack.addWidget(detail_group)
        content_layout.addWidget(self.details_stack)

        self.category_list.currentRowChanged.connect(self.details_stack.setCurrentIndex)

        self.main_layout.addLayout(content_layout)

    def create_detail_group(self, category_name):
        group_box = QGroupBox(category_name)
        layout = QVBoxLayout()

        # Add checkboxes or other widgets to represent the activities
        activities = ["Activity 1", "Activity 2", "Activity 3"]
        for activity in activities:
            checkbox = QCheckBox(activity)
            layout.addWidget(checkbox)

        group_box.setLayout(layout)
        return group_box


app = QApplication(sys.argv)
template_window = TemplateWindow()
template_window.show()
sys.exit(app.exec_())
