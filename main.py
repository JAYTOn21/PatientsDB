from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
import MySQLdb as mdb
from PyQt6.QtWidgets import QAbstractItemView


def dbret():
    try:
        db = mdb.connect('localhost', 'root', '2173', 'mydb')
        return db
    except mdb.Error as e:
        print(f'Error: {e}')


class patientsTableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(patientsTableModel, self).__init__()
        self.data = data

    def columnCount(self, parent=None):
        return len(self.data[0])

    def rowCount(self, parent=None):
        return len(self.data)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        row = index.row()
        col = index.column()
        if role == Qt.ItemDataRole.DisplayRole:
            colExc = [4, 5, 10, 11, 12, 17, 18, 19, 25, 35, 36, 37, 38, 39, 40, 41, 42, 46, 47]
            cell = str(self.data[row][col])
            if cell != 'None':
                if col == 3:
                    if self.data[row][col] == 1:
                        return 'М'
                    else:
                        return 'Ж'
                elif self.data[row][col] in [0, '0']:
                    return ''
                elif self.data[row][col] in [1, '1'] and col in colExc:
                    return '✓'
                else:
                    return cell
            else:
                return ''
        else:
            return None

    def headerData(self, section, orientation, role=None):
        if role == Qt.ItemDataRole.DisplayRole and orientation == Qt.Orientation.Horizontal:

            db = dbret()
            cursor = db.cursor()
            cursor.execute('SELECT * FROM patients')
            header = next(zip(*cursor.description))
            db.close()
            return header[section]
        else:
            return QtCore.QAbstractTableModel.headerData(self, section, orientation, role)


class Ui_MainWindow(object):
    def loadData(self):
        db = dbret()
        cur = db.cursor()
        cur.execute('SELECT * FROM patients')
        data = cur.fetchall()
        model = patientsTableModel(data)
        self.tableView.setModel(model)
        self.tableView.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.tableView.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.tableView.setColumnHidden(0, True)
        self.tableView.setColumnHidden(1, True)
        self.tableView.resizeColumnsToContents()
        self.tableView.setSelectionMode(self.tableView.SelectionMode.SingleSelection)
        db.close()

    def delete(self):
        db = dbret()
        cur = db.cursor()
        row = self.tableView.currentIndex().row()
        ind = int(self.tableView.model().index(row, 0).data())
        sql = "DELETE FROM patients WHERE idpatients = %s"
        val = (ind, )
        cur.execute(sql, val)
        db.commit()
        db.close()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 0))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tableView = QtWidgets.QTableView(parent=self.centralwidget)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(parent=self.menuBar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(parent=self.menuBar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menuBar)
        self.action_2 = QtGui.QAction(parent=MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtGui.QAction(parent=MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtGui.QAction(parent=MainWindow)
        self.action_4.setObjectName("action_4")
        self.aboutAction = QtGui.QAction(parent=MainWindow)
        self.aboutAction.setObjectName("aboutAction")
        self.menu.addSeparator()
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menu.addAction(self.action_4)
        self.menu_2.addAction(self.aboutAction)
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Пациенты"))
        self.menu.setTitle(_translate("MainWindow", "Данные"))
        self.menu_2.setTitle(_translate("MainWindow", "Информация"))
        self.action_2.setText(_translate("MainWindow", "Добавить"))
        self.action_3.setText(_translate("MainWindow", "Изменить"))
        self.action_4.setText(_translate("MainWindow", "Удалить"))
        self.aboutAction.setText(_translate("MainWindow", "О программе"))
