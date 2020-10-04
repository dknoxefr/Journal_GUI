
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from createentry_widget import Ui_create_entry_widget


class Ui_MainWindow(object):

    conn = sqlite3.connect('journal.db')

    c = conn.cursor()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.create_button = QtWidgets.QPushButton(self.centralwidget)
        self.create_button.setGeometry(QtCore.QRect(10, 510, 221, 36))
        self.create_button.setObjectName("create_button")
        self.View_button = QtWidgets.QPushButton(self.centralwidget)
        self.View_button.setGeometry(QtCore.QRect(270, 510, 231, 36))
        self.View_button.setObjectName("View_button")
        self.Select_button = QtWidgets.QPushButton(self.centralwidget)
        self.Select_button.setGeometry(QtCore.QRect(540, 510, 241, 36))
        self.Select_button.setObjectName("Select_button")
        self.Text_box = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Text_box.setGeometry(QtCore.QRect(10, 60, 771, 441))
        self.Text_box.setReadOnly(True)
        self.Text_box.setPlainText("")
        self.Text_box.setObjectName("Text_box")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 54, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 20, 54, 17))
        self.label_2.setObjectName("label_2")
        self.Subject_box = QtWidgets.QLineEdit(self.centralwidget)
        self.Subject_box.setGeometry(QtCore.QRect(270, 10, 511, 36))
        self.Subject_box.setObjectName("Subject_box")
        self.date_box = QtWidgets.QLineEdit(self.centralwidget)
        self.date_box.setGeometry(QtCore.QRect(60, 10, 113, 36))
        self.date_box.setObjectName("date_box")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Entry = QtWidgets.QAction(MainWindow)
        self.actionNew_Entry.setObjectName("actionNew_Entry")
        self.actionView_Summary = QtWidgets.QAction(MainWindow)
        self.actionView_Summary.setObjectName("actionView_Summary")
        self.actionSelect_journal_entry = QtWidgets.QAction(MainWindow)
        self.actionSelect_journal_entry.setObjectName("actionSelect_journal_entry")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionNew_Entry)
        self.menuFile.addAction(self.actionView_Summary)
        self.menuFile.addAction(self.actionSelect_journal_entry)
        self.menuFile.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.date_box, self.Subject_box)
        MainWindow.setTabOrder(self.Subject_box, self.Text_box)
        MainWindow.setTabOrder(self.Text_box, self.create_button)
        MainWindow.setTabOrder(self.create_button, self.View_button)
        MainWindow.setTabOrder(self.View_button, self.Select_button)

        self.View_button.clicked.connect(self.open_journal)
        self.Select_button.clicked.connect(self.openselectdate)
        self.create_button.clicked.connect(self.create_entry)

        self.actionNew_Entry.triggered.connect(self.create_entry)
        self.actionView_Summary.triggered.connect(self.open_journal)
        self.actionSelect_journal_entry.triggered.connect(self.openselectdate)
        self.actionExit.triggered.connect(exit)
        self.actionAbout.triggered.connect(self.aboutbox)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Journal"))
        self.create_button.setText(_translate("MainWindow", "Create new journal entry"))
        self.View_button.setText(_translate("MainWindow", "View journal summary"))
        self.Select_button.setText(_translate("MainWindow", "Select journal entry"))
        self.label.setText(_translate("MainWindow", "Date"))
        self.label_2.setText(_translate("MainWindow", "Subject"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "Help"))
        self.actionNew_Entry.setText(_translate("MainWindow", "New Entry"))
        self.actionNew_Entry.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionView_Summary.setText(_translate("MainWindow", "View Summary"))
        self.actionView_Summary.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionSelect_journal_entry.setText(_translate("MainWindow", "Select journal entry"))
        self.actionSelect_journal_entry.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

    def create_entry(self):
        self.create_entry_widget = QtWidgets.QWidget()
        self.ui = Ui_create_entry_widget()
        self.ui.setupUi(self.create_entry_widget)
        self.create_entry_widget.show()

    def openselectdate(self):
        select_date = self.date_box.text()
        with self.conn:
            self.c.execute("SELECT * FROM pages WHERE date=:date", {'date': select_date})
            rows = self.c.fetchall()
            for row in rows:
                self.Text_box.setPlainText(row[2])
                self.Subject_box.setText(row[1])
                self.date_box.setText(row[0])


    def open_journal(self):
        self.Text_box.setPlainText("")
        with self.conn:
            self.c.execute("SELECT * FROM pages")
            rows = self.c.fetchall()
            for row in rows:
                info = [row[0], " - ", row[1]]
                summary = ''.join(info)
                self.Text_box.appendPlainText(summary)

    def aboutbox(self):
        self.Text_box.setPlainText("""Version 1.0.1 
Created by Derron Knox""")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
