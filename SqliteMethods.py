import pandas as pd
import sqlite3

class SqliteMethods():

    def __init__(self, database_path):
        self.cursor = sqlite3.connect(database_path)

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
    db_path = "./database/DG#1.db"
    db = SqliteMethods(db_path)
    l = db.InsertRowByRule(
        "FEATURE_THRESHOLD_LIST",
        "1,2,3,4,5,6,7,8,9,10,11,12,13,14,151,16"
    )


