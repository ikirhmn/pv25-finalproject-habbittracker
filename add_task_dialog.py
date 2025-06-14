# add_task_dialog.py
from PyQt5 import QtWidgets, QtCore
from db import insert_task

class AddTaskDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add New Task")
        self.setFixedSize(300, 250)

        layout = QtWidgets.QVBoxLayout()

        self.title_input = QtWidgets.QLineEdit()
        self.title_input.setPlaceholderText("Title")

        self.category_input = QtWidgets.QLineEdit()
        self.category_input.setPlaceholderText("Category")

        self.date_input = QtWidgets.QDateEdit()
        self.date_input.setCalendarPopup(True)
        self.date_input.setDate(QtCore.QDate.currentDate())

        self.time_input = QtWidgets.QTimeEdit()
        self.time_input.setTime(QtCore.QTime.currentTime())

        self.notes_input = QtWidgets.QTextEdit()
        self.notes_input.setPlaceholderText("Notes")

        self.save_button = QtWidgets.QPushButton("Save")
        self.save_button.clicked.connect(self.save_data)

        layout.addWidget(self.title_input)
        layout.addWidget(self.category_input)
        layout.addWidget(self.date_input)
        layout.addWidget(self.time_input)
        layout.addWidget(self.notes_input)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def save_data(self):
        title = self.title_input.text()
        category = self.category_input.text()
        date = self.date_input.date().toString("yyyy-MM-dd")
        time = self.time_input.time().toString("HH:mm")
        notes = self.notes_input.toPlainText()

        if title.strip():
            insert_task(title, category, date, time, notes)
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Title is required.")
