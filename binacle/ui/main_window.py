"""
Copyright (C) 2025 Ayrik Nabirahni. This file
is apart of the DHOC project, and licensed under
the GNU AGPL-3.0-or-later. See LICENSE and README for more details.
"""

from PyQt6 import QtCore, QtGui, QtWidgets
from config.settings import *
import time 

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # FONT SETUP HERE ----------
        label_font = QtGui.QFont('Bahnschrift')
        label_font.setPointSize(11)
        button_font = QtGui.QFont('Bahnschrift')
        button_font.setPointSize(14)
        big_label_font = QtGui.QFont('Bahnschrift')
        big_label_font.setPointSize(17)
        # FONT SETUP HERE ----------


        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line_lat = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.line_lat.setGeometry(QtCore.QRect(10, 40, 251, 20))
        self.line_lat.setAutoFillBackground(False)
        self.line_lat.setText(str(azimuth_settings['latitude']))
        self.line_lat.setClearButtonEnabled(False)
        self.line_lat.setObjectName("line_lat")
        self.label_lat = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_lat.setGeometry(QtCore.QRect(10, 20, 251, 21))
        self.label_lat.setFont(label_font)
        self.label_lat.setObjectName("label_lat")
        self.label_lon = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_lon.setGeometry(QtCore.QRect(10, 80, 251, 21))
        self.label_lon.setFont(label_font)
        self.label_lon.setObjectName("label_lon")
        self.line_lon = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.line_lon.setGeometry(QtCore.QRect(10, 100, 251, 20))
        self.line_lon.setText(str(azimuth_settings['longitude']))
        self.line_lon.setObjectName("line_lon")
        self.line_planet = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.line_planet.setGeometry(QtCore.QRect(10, 150, 251, 20))
        self.line_planet.setText(azimuth_settings['planet'])
        self.line_planet.setObjectName("line_planet")
        self.label_planet = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_planet.setGeometry(QtCore.QRect(10, 130, 251, 21))
        self.label_planet.setFont(label_font)
        self.label_planet.setObjectName("label_planet")
        self.button_findazimuth = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_findazimuth.setGeometry(QtCore.QRect(60, 190, 151, 41))
        self.button_findazimuth.setFont(button_font)
        self.button_findazimuth.setObjectName("button_findazimuth")
        self.console_textedit = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.console_textedit.setEnabled(True)
        self.console_textedit.setGeometry(QtCore.QRect(0, 400, 801, 211))
        self.console_textedit.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.console_textedit.setReadOnly(True)
        self.console_textedit.setObjectName("console_textedit")
        self.console_textedit.setFont(label_font)
        self.label_output = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_output.setGeometry(QtCore.QRect(0, 370, 800, 31))
        self.label_output.setFont(big_label_font)
        self.label_output.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_output.setObjectName("label_output")
        self.label_lon_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_lon_2.setGeometry(QtCore.QRect(540, 80, 251, 21))
        self.label_lon_2.setFont(label_font)
        self.label_lon_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_lon_2.setObjectName("label_lon_2")
        self.line_motorsteps = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.line_motorsteps.setGeometry(QtCore.QRect(540, 40, 251, 20))
        self.line_motorsteps.setText(str(motor_settings['stepper_motor_steps']))
        self.line_motorsteps.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.line_motorsteps.setObjectName("line_motorsteps")
        self.line_motorrpm = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.line_motorrpm.setGeometry(QtCore.QRect(540, 150, 251, 20))
        self.line_motorrpm.setText(str(motor_settings['rpm']))
        self.line_motorrpm.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.line_motorrpm.setObjectName("line_motorrpm")
        self.button_pointtelescope = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_pointtelescope.setGeometry(QtCore.QRect(590, 190, 151, 41))
        self.button_pointtelescope.setFont(button_font)
        self.button_pointtelescope.setObjectName("button_pointtelescope")
        self.line_gearratio = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.line_gearratio.setGeometry(QtCore.QRect(540, 100, 251, 20))
        self.line_gearratio.setText(str(motor_settings['gear_ratio']))
        self.line_gearratio.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.line_gearratio.setObjectName("line_gearratio")
        self.label_motorrpm = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_motorrpm.setGeometry(QtCore.QRect(540, 130, 251, 21))
        self.label_motorrpm.setFont(label_font)
        self.label_motorrpm.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_motorrpm.setObjectName("label_motorrpm")
        self.label_motorsteps = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_motorsteps.setGeometry(QtCore.QRect(540, 20, 251, 21))
        self.label_motorsteps.setFont(label_font)
        self.label_motorsteps.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_motorsteps.setObjectName("label_motorsteps")
        self.buttton_arduinosettings = QtWidgets.QPushButton(parent=self.centralwidget)
        self.buttton_arduinosettings.setGeometry(QtCore.QRect(320, 270, 161, 41))
        self.buttton_arduinosettings.setFont(button_font)
        self.buttton_arduinosettings.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.buttton_arduinosettings.setAutoDefault(False)
        self.buttton_arduinosettings.setDefault(False)
        self.buttton_arduinosettings.setFlat(False)
        self.buttton_arduinosettings.setObjectName("buttton_arduinosettings")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # INITIAL "MESSAGES" TO OUTPUT
        self.send_to_console(f'Dominguez Hills Observatory Controller V{version} initialized')
        self.send_to_console(f'Created by Ayrik Nabirahni')

        # iniitialize arduino window
        self.arduino_settings_window = None

        # SET BUTTON SIGNALS/SLOTS HERE
        self.button_findazimuth.clicked.connect((lambda: self.find_azimuth_clicked(self.line_lat.text(), self.line_lon.text(), self.line_planet.text())))
        self.button_pointtelescope.clicked.connect((lambda: self.point_telescope_clicked(self.line_lat.text(), self.line_lon.text(), self.line_planet.text(), self.line_motorsteps.text(), self.line_gearratio.text(), self.line_motorrpm.text())))
        self.buttton_arduinosettings.clicked.connect(self.arduino_settings_clicked)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DH Observatory Controller"))
        self.line_lat.setPlaceholderText(_translate("MainWindow", "33.863907"))
        self.label_lat.setText(_translate("MainWindow", "Current Latitude (+ or -)"))
        self.label_lon.setText(_translate("MainWindow", "Current Longitude (+ or -)"))
        self.line_lon.setPlaceholderText(_translate("MainWindow", "-118.255190"))
        self.line_planet.setPlaceholderText(_translate("MainWindow", "Mars"))
        self.label_planet.setText(_translate("MainWindow", "Target Planet"))
        self.button_findazimuth.setText(_translate("MainWindow", "Find Azimuth"))
        self.label_output.setText(_translate("MainWindow", "Output"))
        self.label_lon_2.setText(_translate("MainWindow", "Gear Ratio (if none, enter 1)"))
        self.line_motorsteps.setPlaceholderText(_translate("MainWindow", "200"))
        self.line_motorrpm.setPlaceholderText(_translate("MainWindow", "3000"))
        self.button_pointtelescope.setText(_translate("MainWindow", "Point Telescope"))
        self.line_gearratio.setPlaceholderText(_translate("MainWindow", "100"))
        self.label_motorrpm.setText(_translate("MainWindow", "Motor RPM"))
        self.label_motorsteps.setText(_translate("MainWindow", "Stepper Motor Steps"))
        self.buttton_arduinosettings.setText(_translate("MainWindow", "Arduino Settings"))

    def send_to_console(self, text):
        current_time = time.strftime("%H:%M:%S")
        self.console_textedit.insertPlainText(f"{current_time} -> {str(text)} {'\n'}")
        self.console_textedit.ensureCursorVisible()


    def arduino_settings_clicked(self):
        # Create a QDialog instance
        self.arduino_settings_dialog = QtWidgets.QDialog()
        
        # Show the dialog
        self.arduino_settings_dialog.show()
        





    def find_azimuth_clicked(self, lat, lon, planet):
        azimuth_settings['latitude'] = lat.strip()
        azimuth_settings['longitude'] = lon.strip()
        azimuth_settings['planet'] = planet.strip().capitalize()

        planet_bary = azimuth_settings['planet'] + ' Barycenter'

            
    def point_telescope_clicked(self, lat, lon, planet, motor_steps, gear_ratio, motor_rpm):
        azimuth_settings['latitude'] = lat.strip()
        azimuth_settings['longitude'] = lon.strip()
        azimuth_settings['planet'] = planet.strip().capitalize()

        planet_bary = azimuth_settings['planet'] + ' Barycenter'

        motor_settings['stepper_motor_steps'] = motor_steps.strip()
        motor_settings['gear_ratio'] = gear_ratio.strip()
        motor_settings['rpm'] = motor_rpm.strip()




        if azimuth_settings['latitude'] != None and azimuth_settings['longitude'] != None and azimuth_settings['planet'] != None and motor_settings['stepper_motor_steps'] != None and motor_settings['gear_ratio'] != None and motor_settings['rpm'] != None: 
            try:
                azimuth_settings['latitude'] = float(azimuth_settings['latitude'])
                azimuth_settings['longitude'] = float(azimuth_settings['longitude'])
                planet_bary = str(planet_bary)
                motor_settings['stepper_motor_steps'] = int(motor_settings['stepper_motor_steps'])
                motor_settings['gear_ratio'] = int(motor_settings['gear_ratio'])
                motor_settings['rpm'] = int(motor_settings['rpm'])
            except ValueError:
                self.send_to_console(prompt_invalid_values)
                return None


        else:
            self.send_to_console(prompt_invalid_values)
            return None

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
