from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QGridLayout,
    QGroupBox,
    QCheckBox,
)
import sys


class OrganizerWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Personal Organizer UI")
        self.setGeometry(100, 100, 1024, 768)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout()
        self.central_widget.setLayout(self.main_layout)

        # Header section with title, date, and user's name
        header_layout = QHBoxLayout()
        title_label = QLabel("PERSONAL ORGANIZER")
        date_label = QLabel("Today is August 1, 2008")
        user_label = QLabel("User's Name")
        header_layout.addWidget(title_label)
        header_layout.addWidget(date_label)
        header_layout.addWidget(user_label)
        self.main_layout.addLayout(header_layout)

        # Main content grid layout
        content_grid = QGridLayout()

        # News section
        news_group = QGroupBox("NEWS")
        news_layout = QVBoxLayout()
        news_items = ["News Item 1", "News Item 2", "News Item 3"]
        for item in news_items:
            news_layout.addWidget(QCheckBox(item))
        news_group.setLayout(news_layout)
        content_grid.addWidget(news_group, 0, 0)

        # Events section
        events_group = QGroupBox("EVENTS")
        events_layout = QVBoxLayout()
        event_items = ["Event 1", "Event 2", "Event 3"]
        for item in event_items:
            events_layout.addWidget(QCheckBox(item))
        events_group.setLayout(events_layout)
        content_grid.addWidget(events_group, 0, 1)

        # Actions section
        actions_group = QGroupBox("ACTIONS")
        actions_layout = QVBoxLayout()
        action_items = ["Action 1", "Action 2", "Action 3"]
        for item in action_items:
            actions_layout.addWidget(QCheckBox(item))
        actions_group.setLayout(actions_layout)
        content_grid.addWidget(actions_group, 0, 2)

        # Personal section
        personal_group = QGroupBox("PERSONAL")
        personal_layout = QVBoxLayout()
        personal_items = ["Personal Item 1", "Personal Item 2", "Personal Item 3"]
        for item in personal_items:
            personal_layout.addWidget(QCheckBox(item))
        personal_group.setLayout(personal_layout)
        content_grid.addWidget(personal_group, 1, 0, 1, 2)  # Span two columns

        # Inbox section
        inbox_group = QGroupBox("INBOX")
        inbox_layout = QVBoxLayout()
        inbox_items = ["Inbox Item 1", "Inbox Item 2", "Inbox Item 3"]
        for item in inbox_items:
            inbox_layout.addWidget(QCheckBox(item))
        inbox_group.setLayout(inbox_layout)
        content_grid.addWidget(inbox_group, 1, 2)

        # Add content grid to the main layout
        self.main_layout.addLayout(content_grid)

        # Footer section with status message
        footer_layout = QHBoxLayout()
        status_message = QLabel("Gray out when news item or action completed")
        footer_layout.addWidget(status_message)
        self.main_layout.addLayout(footer_layout)


app = QApplication(sys.argv)
organizer_window = OrganizerWindow()
organizer_window.show()
sys.exit(app.exec_())
