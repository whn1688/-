#汇总各种表头信息

table_names = {"人员信息表":"Emp_info",
                "库存信息表":"Stock_info",
              "料号信息表":"Item_info",
              "入库信息表":"Storagein_info",
              "出库信息表":"Storageout_info",
              "储位信息表":"Station_info",
              "用户信息表":"User_info",
              "机种信息表":"Machine_info",
              "厂商信息表":"Supplier_info"}


#人员信息表：工号，姓名，部门
Emp_info_columns= "JobNum varchar(50)," \
                  "Name varchar(50)," \
                  "department varchar(50)"

#库存信息表:料号, 型号, 品名, 数量, 单位, 机种, 储位,备注, 是否固资, 固资号
Stock_info_columns = "ItemNum varchar(50)," \
                     "Model varchar(255)," \
                     "ProductName varchar(255)," \
                     "Number decimal(12,2)," \
                     "Unit varchar(50)," \
                     "MachineType varchar(50)," \
                     "Station varchar(50)," \
                     "Tips varchar(255)," \
                     "FixedAssets varchar(2)," \
                     "FixedAssetsNum varchar(50)"

#料号信息表：料号, 型号, 品名, 单位, 储位, 是否固资, 固资号
Item_info_columds = "ItemNum varchar(50)," \
                    "Model varchar(255)," \
                     "ProductName varchar(255)," \
                     "Unit varchar(50)," \
                     "Station varchar(50)," \
                     "FixedAssets varchar(2)," \
                     "FixedAssetsNum varchar(50)"
#入库信息表:料号, 型号, 品名, 数量, 单位, 机种, 储位,备注, 是否固资, 固资号,厂商，收货人员，入库人员，入库时间
Storagein_info_columds = "ItemNum varchar(50)," \
                         "Model varchar(255)," \
                     "ProductName varchar(255)," \
                     "Number decimal(12,2)," \
                     "Unit varchar(50)," \
                     "MachineType varchar(50)," \
                     "Station varchar(50)," \
                     "Tips varchar(255)," \
                     "FixedAssets varchar(2)," \
                     "FixedAssetsNum varchar(50)," \
                     "Supplier varchar(255)," \
                     "ReceiveEmp varchar(50)," \
                     "StorageinEmp varchar(50)," \
                     "StorageinTime datetime" \

#出库信息表:料号, 型号, 品名, 数量, 单位, 机种, 储位,备注, 是否固资, 固资号,领用人员，出库人员，出库时间
Storageout_info_columds = "ItemNum varchar(50)," \
                          "Model varchar(255)," \
                     "ProductName varchar(255)," \
                     "Number decimal(12,2)," \
                     "Unit varchar(50)," \
                     "MachineType varchar(50)," \
                     "Station varchar(50)," \
                     "Tips varchar(255)," \
                     "FixedAssets varchar(2)," \
                     "FixedAssetsNum varchar(50)," \
                     "ApplyEmp varchar(50)," \
                     "StorageoutEmp varchar(50)," \
                     "StorageoutTime datetime" \

Station_info_columns = "StationName varchar(50)"
Machine_info_columns = "MachineName varchar(50)"
Supplier_info_columns = "Supplier varchar(255)"
#用户信息表:用户名，密码，权限
User_info_columns = "Username varchar(50)," \
                    "Password varchar(50)," \
                    "Authority varchar(10)"

all_columns_list = [Emp_info_columns,
                    Stock_info_columns,
                    Item_info_columds,
                    Storagein_info_columds,
                    Storageout_info_columds,
                    Station_info_columns,
                    User_info_columns,
                    Machine_info_columns,
                    Supplier_info_columns]

"""Item_columns = {"料号":0, "型号":1, "品名":2, "数量":3, "单位":4, "机种":4, "储位":5,"备注":6, "确认人":7, "厂商":8, "入库人员":9,
               "固资号":10, "部门":11, "收货人员":12, "是否固资":13,"入库时间":14, "出库时间":15,"领用人员":16}"""

#'_'.join(lists)