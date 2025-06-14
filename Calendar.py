import pygame
from PyQt5 import QtCore, QtGui, QtWidgets
from add_task_dialog import AddTaskDialog
from db import get_all_tasks, insert_task, init_db
from export import export_to_csv, export_to_pdf

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Habbits Tracker")
        MainWindow.resize(749, 561)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 731, 521))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.frame.setPalette(palette)
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 70, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.frame)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 90, 461, 391))
        self.calendarWidget.setAutoFillBackground(False)
        self.calendarWidget.setStyleSheet("QCalendarWidget {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #d0d0d0;\n"
"    border-radius: 8px;\n"
"    color: #333333;\n"
"    font-family: \"Segoe UI\", sans-serif;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"/* Navigation bar (bulan & tahun) */\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar {\n"
"    background-color: #42c3ff;\n"
"    border-bottom: 1px solid #dddddd;\n"
"    border-top-left-radius: 8px;\n"
"    border-top-right-radius: 8px;\n"
"}\n"
"\n"
"/* Tombol navigasi bulan (← →) */\n"
"QCalendarWidget QToolButton {\n"
"    background: transparent;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    padding: 5px;\n"
"    border: none;\n"
"}\n"
"QCalendarWidget QToolButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* Tahun (spinbox) */\n"
"QCalendarWidget QSpinBox {\n"
"    background: white;\n"
"    border: 1px solid #cccccc;\n"
"    border-radius: 4px;\n"
"    padding: 2px 6px;\n"
"}\n"
"\n"
"/* Grid kalender (tanggal) */\n"
"QCalendarWidget QAbstractItemView {\n"
"    background-color: #ffffff;\n"
"    selection-background-color: #42c3ff;\n"
"    selection-color: white;\n"
"    gridline-color: #e0e0e0;\n"
"    font-size: 14px;\n"
"    border-bottom-left-radius: 8px;\n"
"    border-bottom-right-radius: 8px;\n"
"}\n"
"")
        self.calendarWidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.HongKong))
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setSelectionMode(QtWidgets.QCalendarWidget.SingleSelection)
        self.calendarWidget.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.ISOWeekNumbers)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(True)
        self.calendarWidget.setObjectName("calendarWidget")
        self.calendarWidget.selectionChanged.connect(self.on_date_changed)
        self.Reminder = QtWidgets.QWidget(self.frame)
        self.Reminder.setGeometry(QtCore.QRect(490, 220, 231, 261))
        font = QtGui.QFont()
        font.setKerning(True)
        self.Reminder.setFont(font)
        self.Reminder.setAutoFillBackground(False)
        self.Reminder.setStyleSheet("QWidget#Reminder {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #000000;\n"
"    border-radius : 8px\n"
"}\n"
"")
        self.Reminder.setObjectName("Reminder")
        self.label_6 = QtWidgets.QLabel(self.Reminder)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAccessibleName("")
        self.label_6.setAccessibleDescription("")
        self.label_6.setText("Reminder")
        self.label_6.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_6.setObjectName("label_6")
        self.reminderList = QtWidgets.QListWidget(self.Reminder)
        self.reminderList.setGeometry(QtCore.QRect(10, 30, 211, 211))
        self.reminderList.setObjectName("reminderList")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(624, 60, 91, 23))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color:   #42c3ff;\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/plus (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(8, 8))
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.open_add_task_dialog)
        self.containerWidgettimer = QtWidgets.QWidget(self.frame)
        self.containerWidgettimer.setGeometry(QtCore.QRect(490, 90, 231, 121))
        font = QtGui.QFont()
        font.setKerning(True)
        self.containerWidgettimer.setFont(font)
        self.containerWidgettimer.setTabletTracking(False)
        self.containerWidgettimer.setAutoFillBackground(False)
        self.containerWidgettimer.setStyleSheet("QWidget#containerWidgettimer {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #000000;\n"
"    border-radius: 8px;\n"
"}\n"
"")
        self.containerWidgettimer.setObjectName("containerWidgettimer")
        self.label_5 = QtWidgets.QLabel(self.containerWidgettimer)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAccessibleName("")
        self.label_5.setAccessibleDescription("")
        self.label_5.setText("Pomodoro Timer")
        self.label_5.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_5.setObjectName("label_5")
        self.minus_3 = QtWidgets.QPushButton(self.containerWidgettimer)
        self.minus_3.setGeometry(QtCore.QRect(30, 40, 31, 31))
        self.minus_3.setStyleSheet("QPushButton {\n"
"    background-color:   #ffffff;\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}")
        self.minus_3.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minus_3.setIcon(icon1)
        self.minus_3.setIconSize(QtCore.QSize(30, 30))
        self.minus_3.setObjectName("minus_3")
        self.plus_3 = QtWidgets.QPushButton(self.containerWidgettimer)
        self.plus_3.setGeometry(QtCore.QRect(170, 40, 31, 31))
        self.plus_3.setStyleSheet("QPushButton {\n"
"    background-color:   #ffffff;\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}")
        self.plus_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("assets/plus (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.plus_3.setIcon(icon2)
        self.plus_3.setIconSize(QtCore.QSize(30, 30))
        self.plus_3.setObjectName("plus_3")
        self.plus_3.clicked.connect(self.increase_time)
        self.minus_3.clicked.connect(self.decrease_time)
        self.timerLabel_3 = QtWidgets.QLabel(self.containerWidgettimer)
        self.timerLabel_3.setGeometry(QtCore.QRect(70, 40, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat,sans-serif")
        font.setPointSize(-1)
        self.timerLabel_3.setFont(font)
        self.timerLabel_3.setAccessibleName("")
        self.timerLabel_3.setAccessibleDescription("")
        self.timerLabel_3.setStyleSheet("QLabel#timerLabel_3 {\n"
"    background-color: #ffffff;\n"
"    color: #000000;\n"
"    border: 1px solid #000000;\n"
"    border-radius: 8px;\n"
"    padding: 6px 12px;\n"
"    font-family: \'Montserrat\', sans-serif;\n"
"    font-size: 18px;\n"
"    qproperty-alignment: AlignCenter;\n"
"}\n"
"")
        self.timerLabel_3.setText("00:25")
        self.timerLabel_3.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.timerLabel_3.setObjectName("timerLabel_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.containerWidgettimer)
        self.pushButton_4.setGeometry(QtCore.QRect(74, 90, 81, 21))
        self.pushButton_4.clicked.connect(self.start_focus_timer)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton#pushButton_4 {\n"
"    background-color: #ffffff;\n"
"    color: #000000;\n"
"    border: 1px solid #000000;\n"
"    border-radius: 8px;\n"
"    padding: 6px 12px;\n"
"}\n"
"")
        self.focus_minutes = 25  # default awal
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.remaining_seconds = self.focus_minutes * 60

        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 749, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuExport = QtWidgets.QMenu(self.menuFile)
        self.menuExport.setObjectName("menuExport")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuExit = QtWidgets.QMenu(self.menubar)
        self.menuExit.setObjectName("menuExit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.showMessage("Rizki Rahman Maulana| F1D022093")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCSV = QtWidgets.QAction(MainWindow)
        self.actionCSV.setObjectName("actionCSV")
        self.actionPDF = QtWidgets.QAction(MainWindow)
        self.actionPDF.setObjectName("actionPDF")
        self.menuExport.addAction(self.actionCSV)
        self.menuExport.addAction(self.actionPDF)
        self.menuFile.addAction(self.menuExport.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuExit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.connect_menu_actions()
        self.update_timer_display() 

    def open_add_task_dialog(self):
        dialog = AddTaskDialog()
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
                selected_date = self.calendarWidget.selectedDate().toString("yyyy-MM-dd")
                self.load_reminders(selected_date)

    def load_reminders(self,selected_date):
        self.reminderList.clear()
        tasks = get_all_tasks()

        for task in tasks:
           if task[3] == selected_date:  # task[3] = tanggal (yyyy-mm-dd)
                title = task[1]
                time = task[4]
                self.reminderList.addItem(f"{title} ({time})")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Timeline"))
        self.label_2.setText(_translate("MainWindow", "Building better habits"))
        self.pushButton.setText(_translate("MainWindow", "Add new Task"))
        self.pushButton_4.setText(_translate("MainWindow", "Start Timer"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuExport.setTitle(_translate("MainWindow", "Export"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuExit.setTitle(_translate("MainWindow", "Exit"))
        self.actionCSV.setText(_translate("MainWindow", "CSV"))
        self.actionPDF.setText(_translate("MainWindow", "PDF"))

    def connect_menu_actions(self):
        self.actionCSV.triggered.connect(lambda: self.export_handler(export_to_csv, "CSV"))
        self.actionPDF.triggered.connect(lambda: self.export_handler(export_to_pdf, "PDF"))

    def export_handler(self, func, fmt):
        try:
                func()
                QtWidgets.QMessageBox.information(None, "Export Success", f"Data berhasil diekspor ke {fmt}.")
        except Exception as e:
                QtWidgets.QMessageBox.critical(None, "Export Failed", str(e))

    def on_date_changed(self):
        selected_qdate = self.calendarWidget.selectedDate()
        selected_date = selected_qdate.toString("yyyy-MM-dd")
        self.load_reminders(selected_date)

    def update_timer_display(self):
        minutes = self.remaining_seconds // 60
        seconds = self.remaining_seconds % 60
        self.timerLabel_3.setText(f"{minutes:02d}:{seconds:02d}")

    def update_timer(self):
        if self.remaining_seconds > 0:
                self.remaining_seconds -= 1
                self.update_timer_display()
        else:
                self.timer.stop()
                self.play_sound("sound/notification.wav")
                QtWidgets.QMessageBox.information(None, "Selesai!", "Waktu fokusmu selesai, saatnya break! 🍃")


    def start_focus_timer(self):
        self.timer.start(1000)  # setiap 1 detik

    def increase_time(self):
        self.focus_minutes += 5
        self.remaining_seconds = self.focus_minutes * 60
        self.update_timer_display()

    def decrease_time(self):
        if self.focus_minutes > 5:
            self.focus_minutes -= 5
            self.remaining_seconds = self.focus_minutes * 60
            self.update_timer_display()
            
    def play_sound(self, filename):
        try:
                pygame.mixer.init()
                pygame.mixer.music.load(filename)
                pygame.mixer.music.play()
        except Exception as e:
                print(f"Gagal play sound: {e}")



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


if __name__ == "__main__":
    import sys
    init_db()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    selected_date = ui.calendarWidget.selectedDate().toString("yyyy-MM-dd")
    ui.load_reminders(selected_date)
    MainWindow.show()
    sys.exit(app.exec_())
