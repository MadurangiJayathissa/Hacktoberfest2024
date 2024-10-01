import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton, QListView
from PySide6.QtCore import QStringListModel

class TodoListApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Todo List App")
        self.setGeometry(100, 100, 400, 300)

        self.tasks = []

        # Setup UI components
        self.setup_ui()

        # Initialize task list view
        self.update_task_list()

    def setup_ui(self):
        """Setup UI components for the app."""
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        # Task List View
        self.task_list = QListView()
        self.task_list.setEditTriggers(QListView.NoEditTriggers)
        self.task_list.setSelectionMode(QListView.SingleSelection)
        self.layout.addWidget(self.task_list)

        # Input Label and Task Input Field
        self.layout.addWidget(QLabel("Enter a task:"))
        self.task_input = QLineEdit()
        self.layout.addWidget(self.task_input)

        # Add and Remove Buttons
        self.add_button = QPushButton("Add")
        self.add_button.clicked.connect(self.add_task)
        self.layout.addWidget(self.add_button)

        self.remove_button = QPushButton("Remove")
        self.remove_button.clicked.connect(self.remove_task)
        self.layout.addWidget(self.remove_button)

    def add_task(self):
        """Add a task to the task list."""
        task = self.task_input.text().strip()
        if task:  # Ensure non-empty task
            self.tasks.append(task)
            self.task_input.clear()
            self.update_task_list()

    def remove_task(self):
        """Remove the selected task from the task list."""
        selected_index = self.task_list.currentIndex()
        if selected_index.isValid():
            self.tasks.pop(selected_index.row())
            self.update_task_list()

    def update_task_list(self):
        """Update the list view with current tasks."""
        model = QStringListModel(self.tasks)
        self.task_list.setModel(model)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TodoListApp()
    window.show()
    sys.exit(app.exec())
