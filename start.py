import sys
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from about1 import aboutDialog
from addDialog import addDialog
import qdarktheme
import _thread
import MySQLdb as mdb

from main import Ui_MainWindow
# from about import aboutDialog
# from card import addDialog
# from trans import transDialog


# from change import changeDialog

# try:
#     from PyQt5.QtWinExtras import QtWin
#     myappid = 'mycompany.myproduct.subproduct.version'
#     QtWin.setCurrentProcessExplicitAppUserModelID(myappid)
# except ImportError:
#     pass
#
#
def aboutfun():
    dialog = aboutDialog()
    dialog.exec()


def delfun():
    dlg = QMessageBox()
    dlg.setWindowTitle("Удаление данных")
    dlg.setText("Вы уверены, что хотите удалить данные о пациенте?")
    dlg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
    but1 = dlg.button(QMessageBox.StandardButton.Yes)
    but1.setText("Да")
    but2 = dlg.button(QMessageBox.StandardButton.No)
    but2.setText("Нет")
    dlg.setIcon(QMessageBox.Icon.Question)
    dlg.exec()
    if dlg.clickedButton() == but1:
        return 1
    else:
        return 2


class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.ui.loadData()
        self.ui.aboutAction.triggered.connect(aboutfun)
        self.ui.action_2.triggered.connect(self.addData)
        self.ui.action_4.triggered.connect(self.deldata)

    def deldata(self):
        row = self.ui.tableView.currentIndex().row()
        ind = self.ui.tableView.model().index(row, 0).data()
        if ind is not None:
            data = delfun()
            if data == 1:
                self.ui.delete()
                self.ui.loadData()

    def addData(self):
        add = addDialog()
        add.exec()
        self.ui.loadData()
    #
    # def changedata(self):
    #     row = self.ui.tableView.currentIndex().row()
    #     ind = self.ui.tableView.model().index(row, 0).data()
    #     if ind is not None:
    #         name = self.ui.tableView.model().index(row, 1).data()
    #         con = self.ui.tableView.model().index(row, 2).data()
    #         price = self.ui.tableView.model().index(row, 3).data()
    #         weight = self.ui.tableView.model().index(row, 4).data()
    #         dishType = self.ui.tableView.model().index(row, 5).data()
    #         com = self.ui.tableView.model().index(row, 6).data()
    #         db = mdb.connect('localhost', 'root', '2173', 'restdb')
    #         cur = db.cursor()
    #         cur.execute(f"select idtype_of_dish from type_of_dish where '{str(dishType)}' = name_of_type")
    #         data = cur.fetchall()
    #         dishId = data[0][0] - 1
    #         price = str(price).replace('р.', '')
    #         cur.execute(f"SELECT type_of_weight.name_of_type from type_of_weight join type_of_dish where "
    #                         f"type_of_weight.idtype_of_weight = type_of_dish.type_of_weight_idtype_of"
    #                         f"_weight and {dishId + 1} = type_of_dish.idtype_of_dish;")
    #         data = cur.fetchall()
    #         cur.execute(f"select idtype_of_weight from type_of_weight")
    #         weightLength = len(cur.fetchall())
    #         for i in range(weightLength):
    #             weight = str(weight).replace(str(data[0][0]), '')
    #         ch = changeDialog()
    #         ch.lineEdit_2.setText(name)
    #         ch.lineEdit_3.setText(con)
    #         ch.lineEdit_4.setText(weight)
    #         ch.lineEdit.setText(price)
    #         ch.lineEdit_5.setText(com)
    #         ch.comboBox.setCurrentText(dishType)
    #         ch.label_7.setText(ind)
    #         ch.exec_()
    #         self.ui.LoadData()

    def show(self):
        self.main_win.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # app.setWindowIcon(QtGui.QIcon('MR.png'))

    main_win = MainWindow()

    main_win.show()
    sys.exit(app.exec())
