import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from gui import UserInterface, Storagein, Storageout


class Example(QMainWindow):
    def __init__(self):
        self.app = QApplication(sys.argv)
        super().__init__()
        self.ui = UserInterface.Ui_MainWindow()
        self.ui.setupUi(self)
        # 初始化
        self.init_ui()

        self.dialog1 = Dialog_Storagein()
        self.dialog2 = Dialog_Storageout()

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

        self.show()
    # 按钮点击操作函数
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
            #self.dialog2.show()
            self.dialog2.exec_()

            #调用/创建出库界面
        elif btnName == "入库":
            #self.dialog1.show()
            self.dialog1.exec_()
            # 调用/创建入库界面

    def exitFuc(self):
        pass

class Dialog_Storagein(QDialog):
    def __init__(self):
        self.app = QApplication(sys.argv)
        super().__init__()
        self.dialog_in = Storagein.Ui_Dialog()
        self.dialog_in.setupUi(self)
        # 初始化
        #self.init_ui()

        # ui初始化
    def init_ui(self):
    # 初始化方法，这里可以写按钮绑定等的一些初始函数
        self.show()
    # 1.按钮点击操作
class Dialog_Storageout(QDialog):
    def __init__(self):
        self.app = QApplication(sys.argv)
        super().__init__()
        self.dialog_out = Storageout.Ui_Dialog()
        self.dialog_out.setupUi(self)
        # 初始化
        # self.init_ui()

        # ui初始化

    def init_ui(self):
        # 初始化方法，这里可以写按钮绑定等的一些初始函数
        self.show()
    # 1.按钮点击操作

# 程序入口
if __name__ == '__main__':
    e = Example()
    sys.exit(e.app.exec())