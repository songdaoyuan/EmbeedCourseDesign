import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import qdarkstyle
from lib.SQLite3 import SQLITE
from lib.alterInfoDialog import alterInfoDialog
from lib.deleteInfoDialog import deleteInfoDialog
from lib.insertInfoDialog import insertInfoDialog


class Main(QWidget):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setWindowTitle("基于PyQt和SQLite的嵌入式课程设计")
        self.resize(500, 300)
        self.layout = QVBoxLayout()
        self.Hlayout = QHBoxLayout()

        self.insertButton = QPushButton("新增")
        self.alterButton = QPushButton("修改")
        self.deleteButton = QPushButton("删除")
        self.refreshButton = QPushButton("刷新")

        self.insertButton.clicked.connect(self.insertButtonClicked)
        self.alterButton.clicked.connect(self.alterButtonClicked)
        self.deleteButton.clicked.connect(self.deleteButtonClicked)
        self.refreshButton.clicked.connect(self.refreshButtonClicked)


        self.model = QStandardItemModel(7, 4)
        self.model.setHorizontalHeaderLabels(['ID', 'First Name', 'Last Name', 'Phone Number'])

        # #Todo 优化2 添加数据
        # self.model.appendRow([
        #     QStandardItem('row %s,column %s' % (11,11)),
        #     QStandardItem('row %s,column %s' % (11,11)),
        #     QStandardItem('row %s,column %s' % (11,11)),
        #     QStandardItem('row %s,column %s' % (11,11)),
        # ])
        DB = SQLITE()
        content = DB.returnTableContent()
        del DB

        for i in range(0,len(content)):
            for j in range(0,len(content[0])):
                self.model.setItem(i, j, QStandardItem(str(content[i][j])))

        # 实例化表格视图，设置模型为自定义的模型
        self.tableView = QTableView()
        self.tableView.setModel(self.model)

        Hlayout = QHBoxLayout()
        Hlayout.addWidget(self.insertButton)
        Hlayout.addWidget(self.alterButton)
        Hlayout.addWidget(self.deleteButton)
        Hlayout.addWidget(self.refreshButton)
        widget = QWidget()
        widget.setLayout(Hlayout)
        #widget.setFixedWidth(500)
        self.Hlayout.addWidget(widget)

        self.layout.addLayout(self.Hlayout)
        self.layout.addWidget(self.tableView)
        self.setLayout(self.layout)

    def insertButtonClicked(self):
        insertDialog = insertInfoDialog(self)
        #insertDialog.add_book_success_signal.connect(self.insertDialog.searchButtonClicked)
        insertDialog.show()
        insertDialog.exec_()

    def alterButtonClicked(self):
        alterDialog = alterInfoDialog(self)
        #alterDialog.alter_Info_successful_signal.connect(self.alterDialog.searchButtonClicked)
        alterDialog.show()
        alterDialog.exec_()

    def deleteButtonClicked(self):
        deleteDialog = deleteInfoDialog(self)
        #deleteDialog.drop_book_successful_signal.connect(self.deleteDialog.searchButtonClicked)
        deleteDialog.show()
        deleteDialog.exec_()

    def refreshButtonClicked(self):
        print('233')
        DB = SQLITE()
        content = DB.returnTableContent()
        del DB
        self.model.removeRows(0,self.model.rowCount())
        for i in range(0,len(content)):
            for j in range(0,len(content[0])):
                self.model.setItem(i, j, QStandardItem(str(content[i][j])))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    Main = Main()
    Main.show()
    sys.exit(app.exec_())