"""
Copyright (C) 2025 Ayrik Nabirahni. This file
is apart of the DHOC project, and licensed under
the GNU AGPL-3.0-or-later. See LICENSE and README for more details.
"""

import sys
from binacle.ui.main_window import Ui_MainWindow
from PyQt6 import QtWidgets


# DHOC Entrypoint here. Opens Main Window GUI
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec())