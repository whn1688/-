import sys
from PyQt5 import QtCore
from PyQt5.QtCore import QAbstractTableModel, Qt, QAbstractItemModel
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from gui import UserInterface, Storagein, Storageout, login
from SqliteMethods import SqliteMethods as sm
#主界面
class Example(QMainWindow):
    def __init__(self):
        self.app = QApplication(sys.argv)
        super().__init__()
        self.ui = UserInterface.Ui_MainWindow()
        self.ui.setupUi(self)
        # 初始化
        self.init_ui()

    # ui初始化
    def init_ui(self):
        # 初始化方法，这里可以写按钮绑定等的一些初始函数
        #数据库操作
        self.db = sm("./database/DG.db")
        table_list = self.db.ReadTableList()
        column_list = self.db.ColumnsList(table_list["name"][4])
        self.table_list = table_list["name"]

        # 读取用户信息
        userinfo = self.db.SelectWholeTable(table_list["name"][8])
        data = self.db.SelectWholeTable(table_list["name"][4])
        model = PandasModel(data, column_list)
        self.ui.tableView.setModel(model)

        #1.创建各种界面实列
        self.dialog1 = Dialog_Storagein()
        self.dialog2 = Dialog_Storageout()
        self.login1 = Loginui(userinfo)

        #2.按钮点击操作
        self.ui.mBtn_Details.clicked.connect(lambda:self.mbuttonClicked(btnName="储位详情"))
        self.ui.mBtn_Storage.clicked.connect(lambda:self.mbuttonClicked(btnName="出入库界面"))
        self.ui.mBtn_Search.clicked.connect(lambda: self.mbuttonClicked(btnName="查询界面"))
        self.ui.mBtn_AddStation.clicked.connect(lambda: self.mbuttonClicked(btnName="储位信息维护"))
        self.ui.mBtn_AddItem.clicked.connect(lambda: self.mbuttonClicked(btnName="料号信息维护"))
        self.ui.mBtn_Addother.clicked.connect(lambda: self.mbuttonClicked(btnName="其他信息维护"))
        self.ui.mBtn_StorageOut.clicked.connect(lambda: self.mbuttonClicked(btnName="出库"))
        self.ui.mBtn_StorageIn.clicked.connect(lambda: self.mbuttonClicked(btnName="入库"))
        self.login1.ui.lBtn_Login.clicked.connect(lambda: self.mbuttonClicked(btnName="登录"))   #登陆界面按钮

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
        elif btnName == "登录":
            sts = self.login1.Func_login()
            if sts == True:
                self.show()
                self.login1.hide()

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
#登录界面
class Loginui(QMainWindow):
    def __init__(self,user_info):
        self.app = QApplication(sys.argv)
        super().__init__()
        self.ui = login.Ui_MainWindow()
        self.ui.setupUi(self)
        self._user_info = user_info
        self.loginsts = False
        # 初始化
        self.init_ui()
    # ui初始化
    def init_ui(self):
        self.show()
    #登录判断
    def Func_login(self):
        login_info=['login']
        self.user=self.ui.lineEdit.text()
        self.password=self.ui.lineEdit_2.text()
        user_l=len(str(self.user))
        #判断输入格式是否正确
        if self.user=='':
            QMessageBox.information(self,'提示','账号不能为空!', QMessageBox.Ok | QMessageBox.Close, QMessageBox.Close)
            return False
        elif user_l<5 or user_l>20:
            QMessageBox.information(self, '提示', '账号长度不对!', QMessageBox.Ok | QMessageBox.Close, QMessageBox.Close)
            return False
        else:
            if self.password=='':
                QMessageBox.information(self, '提示', '密码不能为空!', QMessageBox.Ok | QMessageBox.Close, QMessageBox.Close)
                return False
            else:
                login_info.append(self.user)
                login_info.append(self.password)
                login_info=' '.join(login_info)
                i = 0
                # 判断用户及密码是否正确
                for name in self._user_info["Username"].values:
                    if  self.user == name and self.password == self._user_info["Password"].values[i]:#and self.password in self._user_info["Password"]
                        QMessageBox.information(self, '登录成功', '登录成功!', QMessageBox.Ok | QMessageBox.Close, QMessageBox.Close)
                        return True
                        break
                        #
                        #widget1.show()
                        #ui1.label.setText(self.user)
                    elif self.user != name and i == self._user_info.shape[0]-1:
                        QMessageBox.information(self, '失败', '登录失败，无此账号!!', QMessageBox.Ok | QMessageBox.Close,QMessageBox.Close)
                        return False
                        break
                    elif self.user ==name and self.password != self._user_info["Password"].values[i]:
                        QMessageBox.information(self, '失败', '登录失败，密码错误!!', QMessageBox.Ok | QMessageBox.Close,QMessageBox.Close)
                        return False
                        break
                    i+=1


# 程序入口
if __name__ == '__main__':
    e = Example()
    sys.exit(e.app.exec())