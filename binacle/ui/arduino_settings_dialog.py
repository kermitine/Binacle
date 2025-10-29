"""
Copyright (C) 2025 Ayrik Nabirahni. This file
is apart of the DHOC project, and licensed under
the GNU AGPL-3.0-or-later. See LICENSE and README for more details.
"""

from PyQt6 import QtCore, QtGui, QtWidgets
from config.settings import *

class Arduino_settings(object):
    def setupUi(self, Dialog):
        # FONT SETUP HERE ----------
        label_font = QtGui.QFont('Bahnschrift')
        label_font.setPointSize(11)
        button_font = QtGui.QFont('Bahnschrift')
        button_font.setPointSize(14)
        big_label_font = QtGui.QFont('Bahnschrift')
        big_label_font.setPointSize(17)
        # FONT SETUP HERE ----------

        Dialog.setObjectName("Dialog")
        Dialog.resize(376, 100)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=Dialog)
        self.buttonBox.setFont(label_font)
        self.buttonBox.setGeometry(QtCore.QRect(280, 30, 81, 51))
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.line_baud = QtWidgets.QLineEdit(parent=Dialog)
        self.line_baud.setGeometry(QtCore.QRect(10, 20, 251, 20))
        self.line_baud.setAutoFillBackground(False)
        self.line_baud.setText(str(arduino_settings['baud_rate']))
        self.line_baud.setClearButtonEnabled(False)
        self.line_baud.setObjectName("line_baud")
        self.label_baud = QtWidgets.QLabel(parent=Dialog)
        self.label_baud.setGeometry(QtCore.QRect(10, 0, 251, 21))
        self.label_baud.setFont(label_font)
        self.label_baud.setObjectName("label_baud")
        self.label_port = QtWidgets.QLabel(parent=Dialog)
        self.label_port.setGeometry(QtCore.QRect(10, 50, 251, 21))
        self.label_port.setFont(label_font)
        self.label_port.setObjectName("label_port")
        self.line_port = QtWidgets.QLineEdit(parent=Dialog)
        self.line_port.setGeometry(QtCore.QRect(10, 70, 251, 20))
        self.line_port.setAutoFillBackground(False)
        self.line_port.setText(str(arduino_settings['port_number']))
        self.line_port.setClearButtonEnabled(False)
        self.line_port.setObjectName("line_port")

        self.retranslateUi(Dialog)
        #self.buttonBox.clicked.connect()
        self.buttonBox.accepted.connect(lambda: self.buttonbox_ok_pressed(self.line_port.text(), self.line_baud.text())) # type: ignore
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Arduino Settings"))
        self.line_baud.setPlaceholderText(_translate("Dialog", "9600"))
        self.label_baud.setText(_translate("Dialog", "Serial Baud Rate"))
        self.label_port.setText(_translate("Dialog", "Arduino Port # (EX: COM3 = 3)"))
        self.line_port.setPlaceholderText(_translate("Dialog", "3"))

    def buttonbox_ok_pressed(self, port_number, baud):
        arduino_settings['port'] = f'COM{port_number}'
        arduino_settings['port_number'] = int(port_number)
        arduino_settings['baud_rate'] = int(baud)
        


