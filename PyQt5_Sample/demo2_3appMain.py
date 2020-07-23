import sys
from PyQt5.QtWidgets import QApplication
from myDialog import QMyDialog

app = QApplication(sys.argv)
mainform = QMyDialog()
mainform.show()
sys.exit(app.exec_())