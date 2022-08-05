import pandas as pd
import os
import sqlite3
import Dbmessage as dbm


class SqliteMethods():
    def __init__(self, database_path):
        self._database_path = database_path
        self._database_path_exist = os.path.exists(self._database_path)
        if self._database_path_exist ==True:
            self.cursor = sqlite3.connect(self._database_path)
        else:
            self.Creatdb()

#创建数据库，填充table与column
    def Creatdb(self):
        self.cursor = sqlite3.connect(self._database_path)
        #for value in table_names:
        i = 0
        for value in dbm.table_names.keys():
            self.cursor.execute("create table {} ({}); ".format(dbm.table_names[value],dbm.all_columns_list[i]))
            i = i + 1

    def CreatTable(self):
        pass
    def ChangeFormat(self,message):
        if type(message) == type(str()):
            return "'{}'".format(message)
        else:
            return message

    def ReadTableList(self):
        #table_list = self.cursor.execute("SELECT name FROM sqlite_master WHERE type=’table’ ORDER BY name; ")
        table_list = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name; ", self.cursor)
        return table_list

    #完全通过规则操作数据库
    def SqlConsole(self,rule):
        try:
            result = self.cursor.execute(rule)
        except LookupError:
            return "请确认输入的规则是否正确"
        else:
            return result

    #按照规则查找
    def SelectTableByRule(self, table_name, rule):
        result = pd.read_sql_query("select * from {} where {}".format(table_name, rule),self.cursor)
        return result

    #返回指定表的所有信息
    def SelectWholeTable(self, table_name):
        result = pd.read_sql_query("select * from "+table_name, self.cursor)
        return result

    #按列数值查找所有行
    def SelectInColumns(self, table_name, column_name, value_name):
        result = pd.read_sql_query("select * from {} where {} like '%{}%'".format(table_name, column_name, value_name),self.cursor)
        return result

    # 按规则替换
    def UpdateTableByRule(self, table_name, column_name, new_value, rule):
        new_value = self.ChangeFormat(new_value)
        self.cursor.execute("update {} set {}={} where {}".format(table_name, column_name, new_value, rule))
        self.cursor.commit()
        return "操作成功"

    #按规则插入(datas输入为str类型)
    def InsertRowByRule(self, table_name, datas):
        self.cursor.execute("insert into {} values ({})".format(table_name, datas))
        self.cursor.commit()
        return "操作成功"

    #TODO 交互式插入
    #查询当前表的列
    def ColumnsList(self, table_name):
        db = self.SelectWholeTable(table_name)
        columnslist = db.columns
        return columnslist

    #按规则删除
    def DeleteRowByRule(self, table_name, rule):
        self.cursor.execute("delete from {} where {}".format(table_name, rule))
        self.cursor.commit()
        return "操作成功"

if __name__ == "__main__":
    db_path = "./database/DG.db"
    db = SqliteMethods(db_path)
    l = db.InsertRowByRule(
        "User_info",
        "'admin1','123456','1'"
    )


