# PyQt5 demo2_1
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

# create app
app = QtWidgets.QApplication(sys.argv)

# create widget
widgetHello = QtWidgets.QWidget()

# set widget property
widgetHello.resize(280, 150)
widgetHello.setWindowTitle("Demo2_1")

# add label
labHello = QtWidgets.QLabel(widgetHello)
labHello.setText("Hello world, PyQt5")

# set font
font = QtGui.QFont()
font.setPointSize(12)
font.setBold(True)

labHello.setFont(font)
size = labHello.sizeHint()
labHello.setGeometry(10, 10, size.width(), size.height())
widgetHello.show()

sys.exit(app.exec())