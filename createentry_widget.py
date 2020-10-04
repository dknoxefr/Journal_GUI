

from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
import sqlite3

class Ui_create_entry_widget(object):

    conn = sqlite3.connect('journal.db')

    c = conn.cursor()

    def setupUi(self, create_entry_widget):
        create_entry_widget.setObjectName("create_entry_widget")
        create_entry_widget.resize(803, 564)
        self.journalentry_box = QtWidgets.QPlainTextEdit(create_entry_widget)
        self.journalentry_box.setGeometry(QtCore.QRect(10, 70, 781, 441))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.journalentry_box.setFont(font)
        self.journalentry_box.setObjectName("journalentry_box")
        self.label = QtWidgets.QLabel(create_entry_widget)
        self.label.setGeometry(QtCore.QRect(20, 20, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.cancel_button = QtWidgets.QPushButton(create_entry_widget)
        self.cancel_button.setGeometry(QtCore.QRect(450, 520, 341, 36))
        self.cancel_button.setObjectName("cancel_button")
        self.subject_textbox = QtWidgets.QLineEdit(create_entry_widget)
        self.subject_textbox.setGeometry(QtCore.QRect(90, 20, 691, 36))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.subject_textbox.setFont(font)
        self.subject_textbox.setObjectName("subject_textbox")
        self.save_button = QtWidgets.QPushButton(create_entry_widget)
        self.save_button.setGeometry(QtCore.QRect(10, 520, 351, 36))
        self.save_button.setObjectName("save_button")

        self.retranslateUi(create_entry_widget)
        QtCore.QMetaObject.connectSlotsByName(create_entry_widget)
        create_entry_widget.setTabOrder(self.subject_textbox, self.journalentry_box)
        create_entry_widget.setTabOrder(self.journalentry_box, self.save_button)
        create_entry_widget.setTabOrder(self.save_button, self.cancel_button)

        self.save_button.clicked.connect(lambda:self.save_entry(create_entry_widget))
        self.cancel_button.clicked.connect(lambda:self.exit_entry(create_entry_widget))

    def retranslateUi(self, create_entry_widget):
        _translate = QtCore.QCoreApplication.translate
        create_entry_widget.setWindowTitle(_translate("create_entry_widget", "Journal Entry"))
        self.label.setText(_translate("create_entry_widget", "Subject:"))
        self.cancel_button.setText(_translate("create_entry_widget", "Cancel"))
        self.save_button.setText(_translate("create_entry_widget", "Save"))

    def save_entry(self,create_entry_widget):
        '''Gets inputs from user, appends it to a text file and reloads the menu'''
        get_date = datetime.now()
        subby = self.subject_textbox.text()
        entry = self.journalentry_box.toPlainText()
        with self.conn:
            self.c.execute("INSERT INTO pages VALUES (:date, :subject, :entry)",
                      {'date': get_date.strftime("%x"), 'subject': subby, 'entry': entry})
        create_entry_widget.hide()


    def exit_entry(self,create_entry_widget):
        create_entry_widget.hide()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    create_entry_widget = QtWidgets.QWidget()
    ui = Ui_create_entry_widget()
    ui.setupUi(create_entry_widget)
    create_entry_widget.show()
    sys.exit(app.exec_())
