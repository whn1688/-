import sys
from PyQt5 import QtCore
from PyQt5.QtCore import QAbstractTableModel, Qt, QAbstractItemModel
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from gui import UserInterface, Storagein, Storageout
from SqliteMethods import SqliteMethods as sm

class Example(QMainWindow):
    def __init__(self):
        self.app = QApplication(sys.argv)
        super().__init__()
        self.ui = UserInterface.Ui_MainWindow()
        self.ui.setupUi(self)
        self.dialog1 = Dialog_Storagein()
        self.dialog2 = Dialog_Storageout()
        self.db = sm("./northwindEF.db")
        # 初始化
        self.init_ui()


    # ui初始化
    def init_ui(self):
        # 初始化方法，这里可以写按钮绑定等的一些初始函数

        #1.按钮点击操作
        self.ui.mBtn_Details.clicked.connect(lambda:self.mbuttonClicked(btnName="储位详情"))
        self.ui.mBtn_Storage.clicked.connect(lambda:self.mbuttonClicked(btnName="出入库界面"))
        self.ui.mBtn_Search.clicked.connect(lambda: self.mbuttonClicked(btnName="查询界面"))
        self.ui.mBtn_AddStation.clicked.connect(lambda: self.mbuttonClicked(btnName="储位信息维护"))
        self.ui.mBtn_AddItem.clicked.connect(lambda: self.mbuttonClicked(btnName="料号信息维护"))
        self.ui.mBtn_Addother.clicked.connect(lambda: self.mbuttonClicked(btnName="其他信息维护"))
        self.ui.mBtn_StorageOut.clicked.connect(lambda: self.mbuttonClicked(btnName="出库"))
        self.ui.mBtn_StorageIn.clicked.connect(lambda: self.mbuttonClicked(btnName="入库"))

        # 2.数据库操作
        table_list = self.db.ReadTableList()
        column_list = self.db.ColumnsList(table_list["name"][8])
        print(column_list.values)
        self.table_list = table_list["name"]
        datas = []
        for i in table_list["name"]:
            datas.append(self.db.SelectWholeTable(i))
        self.dataset = datas
        data = self.db.SelectWholeTable(table_list["name"][8])

        model = PandasModel(data,column_list)
        self.ui.tableView.setModel(model)

        self.show()
#按钮点击事件函数
    def mbuttonClicked(self, btnName=""):

        if btnName == "储位详情":
            self.ui.stackedWidget.setCurrentIndex(0)
        elif btnName == "出入库界面":
            self.ui.stackedWidget.setCurrentIndex(1)
        elif btnName == "查询界面":
            self.ui.stackedWidget.setCurrentIndex(2)
        elif btnName == "储位信息维护":
            self.ui.stackedWidget.setCurrentIndex(3)
        elif btnName == "料号信息维护":
            self.ui.stackedWidget.setCurrentIndex(4)
        elif btnName == "其他信息维护":
            self.ui.stackedWidget.setCurrentIndex(5)
        elif btnName == "出库":
            self.dialog2.exec_()
        elif btnName == "入库":
            self.dialog1.exec_()

#入库界面
class Dialog_Storagein(QDialog):
    def __init__(self):
        self.app = QApplication(sys.argv)
        super().__init__()
        self.dialog_in = Storagein.Ui_Dialog()
        self.dialog_in.setupUi(self)

#出库界面
class Dialog_Storageout(QDialog):
    def __init__(self):
        self.app = QApplication(sys.argv)
        super().__init__()
        self.dialog_out = Storageout.Ui_Dialog()
        self.dialog_out.setupUi(self)

#表格显示模板
#说明：表格需要一个模板来填充显示
class PandasModel(QAbstractTableModel):
    def __init__(self, data, column_list, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self._data = data
        self._column_list = column_list

    def rowCount(self, parent=None):
        return len(self._data.values)

    def columnCount(self, parent=None):
        return self._data.columns.size

#行首列首设置
    def headerData(self, section, orientation, role) :
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal :
                 return self._column_list[section]
            elif orientation == Qt.Vertical:
                 return section

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return QtCore.QVariant(str(
                    self._data.values[index.row()][index.column()]))
        return QtCore.QVariant()

# 程序入口
if __name__ == '__main__':
    e = Example()
    sys.exit(e.app.exec())