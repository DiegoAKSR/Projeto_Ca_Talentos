# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_banco.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DMBANK(object):
    def setupUi(self, DMBANK):
        DMBANK.setObjectName("DMBANK")
        DMBANK.resize(410, 375)
        DMBANK.setStyleSheet("background-color: rgb(71, 98, 104);")
        self.centralwidget = QtWidgets.QWidget(DMBANK)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(15, 0, 390, 310))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../Downloads/HatchfulExport-All/facebook_profile_image.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.line_input = QtWidgets.QLineEdit(self.centralwidget)
        self.line_input.setGeometry(QtCore.QRect(82, 219, 261, 31))
        self.line_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 87 8pt \"Arial Black\";\n"
"font: 87 8pt \"Arial Black\";\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;")
        self.line_input.setText("")
        self.line_input.setObjectName("line_input")
        self.btn_sacar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sacar.setGeometry(QtCore.QRect(70, 260, 80, 23))
        self.btn_sacar.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.btn_sacar.setObjectName("btn_sacar")
        self.btn_depositar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_depositar.setGeometry(QtCore.QRect(170, 260, 80, 23))
        self.btn_depositar.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.btn_depositar.setObjectName("btn_depositar")
        self.label_saldo = QtWidgets.QLabel(self.centralwidget)
        self.label_saldo.setGeometry(QtCore.QRect(270, 30, 130, 35))
        self.label_saldo.setStyleSheet("font: 87 9pt \"Arial Black\";\n"
"\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;")
        self.label_saldo.setText("")
        self.label_saldo.setObjectName("label_saldo")
        self.label_nome = QtWidgets.QLabel(self.centralwidget)
        self.label_nome.setGeometry(QtCore.QRect(10, 10, 145, 20))
        self.label_nome.setStyleSheet("font: 87 8pt \"Arial Black\";\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;")
        self.label_nome.setText("")
        self.label_nome.setObjectName("label_nome")
        self.label_idade = QtWidgets.QLabel(self.centralwidget)
        self.label_idade.setGeometry(QtCore.QRect(10, 35, 113, 20))
        self.label_idade.setStyleSheet("font: 87 8pt \"Arial Black\";\n"
"font: 87 8pt \"Arial Black\";\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;")
        self.label_idade.setText("")
        self.label_idade.setObjectName("label_idade")
        self.label_conta_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_conta_2.setGeometry(QtCore.QRect(10, 60, 113, 20))
        self.label_conta_2.setStyleSheet("font: 87 8pt \"Arial Black\";\n"
"font: 87 8pt \"Arial Black\";\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;")
        self.label_conta_2.setText("")
        self.label_conta_2.setObjectName("label_conta_2")
        self.label_TelaPrincipal = QtWidgets.QLabel(self.centralwidget)
        self.label_TelaPrincipal.setGeometry(QtCore.QRect(76, 90, 275, 70))
        self.label_TelaPrincipal.setStyleSheet("font: 87 8pt \"Arial Black\";\n"
"background-color: rgb(95, 133, 140);\n"
"font: 87 8pt \"Arial Black\";\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"")
        self.label_TelaPrincipal.setText("")
        self.label_TelaPrincipal.setObjectName("label_TelaPrincipal")
        self.btn_transferir = QtWidgets.QPushButton(self.centralwidget)
        self.btn_transferir.setGeometry(QtCore.QRect(270, 260, 80, 23))
        self.btn_transferir.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.btn_transferir.setObjectName("btn_transferir")
        DMBANK.setCentralWidget(self.centralwidget)

        self.retranslateUi(DMBANK)
        QtCore.QMetaObject.connectSlotsByName(DMBANK)

    def retranslateUi(self, DMBANK):
        _translate = QtCore.QCoreApplication.translate
        DMBANK.setWindowTitle(_translate("DMBANK", "DMBANK"))
        self.btn_sacar.setText(_translate("DMBANK", "Sacar"))
        self.btn_depositar.setText(_translate("DMBANK", "Depositar"))
        self.btn_transferir.setText(_translate("DMBANK", "Transferir"))