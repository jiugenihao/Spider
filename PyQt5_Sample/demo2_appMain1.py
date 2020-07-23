import sys
from PyQt5 import QtWidgets
import UI_FormHello

app = QtWidgets.QApplication(sys.argv)

base_widget = QtWidgets.QWidget()
ui = UI_FormHello.Ui_FormHello()
ui.setupUi(base_widget)

base_widget.show()
sys.exit(app.exec())