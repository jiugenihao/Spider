## 与UI窗口类对应的业务逻辑类
import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtGui import QPalette
from PyQt5.QtCore import Qt, pyqtSlot
from ui_Dialog import Ui_Dialog

class QMyDialog(QDialog):
    def __init__(self, parent=None):
        # 调用父类构造函数，创建窗口
        super().__init__(parent)

        # 创建UI对象
        self.ui = Ui_Dialog()

        # 构造UI
        self.ui.setupUi(self)
        self.ui.radioBlue.clicked.connect(self.do_setTextColor)
        self.ui.radioRed.clicked.connect(self.do_setTextColor)
        self.ui.radioBlack.clicked.connect(self.do_setTextColor)

    def on_btnClear_clicked(self):
        self.ui.textEdit.clear()
        pass

    def on_chkBoxBold_toggled(self, checked):
        font = self.ui.textEdit.font()
        font.setBold(checked)
        self.ui.textEdit.setFont(font)
        pass

    def on_chkBoxUnder_toggled(self, checked):
        font = self.ui.textEdit.font()
        font.setUnderline(checked)
        self.ui.textEdit.setFont(font)
        pass

    #def on_chkBoxItelic_clicked(self):
    #    checked = self.ui.chkBoxItelic.isChecked()
    #    font = self.ui.textEdit.font()
    #    font.setItalic(checked)
    #    self.ui.textEdit.setFont(font)
    #    pass

    
    @pyqtSlot(bool)
    def on_chkBoxItelic_clicked(self, checked):
        font = self.ui.textEdit.font()
        font.setItalic(checked)
        self.ui.textEdit.setFont(font)
        pass

    def do_setTextColor(self):
        plet = self.ui.textEdit.palette()
        if (self.ui.radioBlack.isChecked()):
            plet.setColor(QPalette.Text, Qt.black)
        elif (self.ui.radioBlue.isChecked()):
            plet.setColor(QPalette.Text, Qt.blue)
        elif (self.ui.radioRed.isChecked()):
            plet.setColor(QPalette.Text, Qt.red)
        self.ui.textEdit.setPalette(plet)
        pass

    pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QMyDialog()
    form.show()
    sys.exit(app.exec_())
    pass