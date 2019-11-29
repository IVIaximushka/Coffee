import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
import sqlite3
from ui_fo import Ui_MainWindow as f1
from ui_ft import Ui_MainWindow as f2


class MyWidget(QMainWindow, f1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        con = sqlite3.connect('coffee.db')
        cur = con.cursor()
        self.table = cur.execute("SELECT * FROM Coffee").fetchall()
        con.close()
        self.show_table(self.table)
        self.pushButton.clicked.connect(self.run)

    def show_table(self, table):
        length = len(table)
        self.tableWidget.setRowCount(length)
        for i in range(length):
            for j in range(7):
                item = QTableWidgetItem(str(table[i][j]))
                self.tableWidget.setItem(i, j, item)

    def run(self):
        self.current_form = ExWidget()
        self.current_form.setWindowTitle('Add')
        self.current_form.show()


class ExWidget(QMainWindow, f2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        con = sqlite3.connect('coffee.db')
        cur = con.cursor()
        cur.execute(self.lineEdit.text())
        con.commit()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())