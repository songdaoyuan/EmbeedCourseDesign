import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import qdarkstyle

from lib.SQLite3 import SQLITE

class insertInfoDialog(QDialog):
    insert_Info_successful_signal = pyqtSignal()

    def __init__(self, parent=None):
        super(insertInfoDialog, self).__init__(parent)
        self.setUpUI()
        self.setWindowModality(Qt.WindowModal)
        self.setWindowTitle("录入用户信息")

    def setUpUI(self):
        self.resize(350, 250)
        self.layout = QFormLayout()
        self.setLayout(self.layout)

        # Label控件
        self.titleLable = QLabel('信息录入')
        self.firstNameLable = QLabel("First Name:")
        self.lastNameLable = QLabel("Last Name:")
        self.numberLabel = QLabel("Phone:")

        # button控件
        self.insertInfoButton = QPushButton("确认")

        # lineEdit控件
        self.firstNameEdit = QLineEdit()
        self.lastNameEdit = QLineEdit()
        self.numberEdit = QLineEdit()
        

        # 添加进formlayout
        self.layout.addRow("", self.titleLable)
        self.layout.addRow(self.firstNameLable, self.firstNameEdit)
        self.layout.addRow(self.lastNameLable, self.lastNameEdit)
        self.layout.addRow(self.numberLabel, self.numberEdit)
        self.layout.addRow("", self.insertInfoButton)

        # 设置字体
        font = QFont()
        font.setPixelSize(20)
        self.titleLable.setFont(font)
        font.setPixelSize(14)
        self.firstNameLable.setFont(font)
        self.lastNameLable.setFont(font)
        self.numberLabel.setFont(font)

        self.firstNameEdit.setFont(font)
        self.lastNameEdit.setFont(font)
        self.numberEdit.setFont(font)

        # button设置
        font.setPixelSize(16)
        self.insertInfoButton.setFont(font)
        self.insertInfoButton.setFixedHeight(32)
        self.insertInfoButton.setFixedWidth(140)

        # 设置间距
        self.titleLable.setMargin(8)
        self.layout.setVerticalSpacing(10)

        self.insertInfoButton.clicked.connect(self.insertInfoButtonClicked)
    
    def insertInfoButtonClicked(self):
        firstName = self.firstNameEdit.text()
        lastName = self.lastNameEdit.text()
        number = self.numberEdit.text()
    
        DB = SQLITE()
        DB.ExecNonQuery(f"INSERT INTO 'Users' (ID, FirstName, LastName, Phone)VALUES (NULL, '{firstName}', '{lastName}', '{number}')")
        del DB
        print(QMessageBox.warning(self, "提示", "添加成功!", QMessageBox.Yes, QMessageBox.Ok))
        self.clearEdit()
        return
    
    def clearEdit(self):
        self.firstNameEdit.clear()
        self.lastNameEdit.clear()
        self.numberEdit.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = insertInfoDialog()
    mainMindow.show()
    sys.exit(app.exec_())
