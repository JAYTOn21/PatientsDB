from PyQt6 import QtCore, QtGui, QtWidgets


class aboutDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(aboutDialog, self).__init__(parent)
        self.setObjectName("Dialog")
        self.resize(417, 371)
        self.setMinimumSize(QtCore.QSize(417, 371))
        self.setMaximumSize(QtCore.QSize(417, 16777215))
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser = QtWidgets.QTextBrowser(parent=self)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(parent=self)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "О программе"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">База данных показателей пациентов с хронической обструктивной болезнью лёгких</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Выполнили:<br />Абрамов М.С.<br />Акинин А.А.<br />Байдикова С.А.<br />Бубченко Е.И.<br />Кайдаракова Е.А.<br />Ковригина А.Д.<br />Шиганов С.В.<br />Яковлев Д.А.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Абакан, 2024</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Закрыть"))
        self.pushButton.clicked.connect(self.close)
