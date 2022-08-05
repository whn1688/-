table_names = {"人员信息表":"Emp_info",
                "库存信息表":"Stock _info",
              "料号信息表":"Item_info",
              "入库信息表":"Storagein_info",
              "出库信息表":"Storageout_info",
              "储位信息表":"Station_info",
              "用户信息表":"User_info",
              "机种信息表":"Machine_info",
              "厂商信息表":"Supplier_info"}
print(table_names.keys())
for value in table_names:
    print(table_names[value])