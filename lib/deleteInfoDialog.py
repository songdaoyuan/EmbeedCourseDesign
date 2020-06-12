import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import qdarkstyle

from lib.SQLite3 import SQLITE

class deleteInfoDialog(QDialog):
    delete_Info_successful_signal = pyqtSignal()

    def __init__(self, parent=None):
        super(deleteInfoDialog, self).__init__(parent)
        self.setUpUI()
        self.setWindowModality(Qt.WindowModal)
        self.setWindowTitle("删除用户信息")

    def setUpUI(self):
        self.resize(350, 280)
        self.layout = QFormLayout()
        self.setLayout(self.layout)

        # Label控件
        self.titleLable = QLabel('信息删除')
        self.idLable = QLabel("ID:")
        self.firstNameLable = QLabel("First Name:")
        self.lastNameLable = QLabel("Last Name:")
        self.numberLabel = QLabel("Phone:")

        # button控件
        self.deleteInfoButton = QPushButton("确认")

        # lineEdit控件
        self.idEdit = QLineEdit()
        self.firstNameEdit = QLineEdit()
        self.lastNameEdit = QLineEdit()
        self.numberEdit = QLineEdit()
        

        # 添加进formlayout
        self.layout.addRow("", self.titleLable)
        self.layout.addRow(self.idLable, self.idEdit)
        self.layout.addRow(self.firstNameLable, self.firstNameEdit)
        self.layout.addRow(self.lastNameLable, self.lastNameEdit)
        self.layout.addRow(self.numberLabel, self.numberEdit)
        self.layout.addRow("", self.deleteInfoButton)

        # 设置字体
        font = QFont()
        font.setPixelSize(20)
        self.titleLable.setFont(font)
        font.setPixelSize(14)
        self.idLable.setFont(font)
        self.firstNameLable.setFont(font)
        self.lastNameLable.setFont(font)
        self.numberLabel.setFont(font)

        self.idEdit.setFont(font)
        self.firstNameEdit.setFont(font)
        self.lastNameEdit.setFont(font)
        self.numberEdit.setFont(font)

        # button设置
        font.setPixelSize(16)
        self.deleteInfoButton.setFont(font)
        self.deleteInfoButton.setFixedHeight(32)
        self.deleteInfoButton.setFixedWidth(140)

        # 设置间距
        self.titleLable.setMargin(8)
        self.layout.setVerticalSpacing(10)

        self.deleteInfoButton.clicked.connect(self.deleteInfoButtonClicked)
        self.idEdit.textChanged.connect(self.idEditChanged)
    
    def idEditChanged(self):
        ID = self.idEdit.text()
        if (ID == ""):
            self.firstNameEdit.clear()
            self.lastNameEdit.clear()
            self.numberEdit.clear()
        
        # 查询对应ID，如果存在就更新form
        else:
            DB = SQLITE()
            self.result = DB.ExecQuery(f"SELECT * FROM Users WHERE ID={ID}")
            del DB
            if not self.result == []:
                self.firstNameEdit.setText(self.result[0][1])
                self.lastNameEdit.setText(self.result[0][2])
                self.numberEdit.setText(self.result[0][3])
            return
    
    def deleteInfoButtonClicked(self):
        ID = self.idEdit.text()
        firstName = self.firstNameEdit.text()
        lastName = self.lastNameEdit.text()
        number = self.numberEdit.text()
        
        DB = SQLITE()
        result = DB.ExecQuery(f"SELECT * FROM Users WHERE ID = {ID}")
        del DB
        if result == []:
            print(QMessageBox.warning(self, "警告", "该用户不存在，请检查ID输入!", QMessageBox.Yes, QMessageBox.Ok))
            self.clearEdit()
            return
        else:
            DB = SQLITE()
            DB.ExecNonQuery(f"DELETE FROM Users WHERE ID = {ID}")
            del DB
            print(QMessageBox.warning(self, "提示", "删除成功!", QMessageBox.Yes, QMessageBox.Ok))
            self.clearEdit()
            return
    
    def clearEdit(self):
        self.idEdit.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = deleteInfoDialog()
    mainMindow.show()
    sys.exit(app.exec_())
