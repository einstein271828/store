# import xlrd
# wb=xlrd.open_workbook(filename="2020年每个月的销售情况.xlsx",encoding_override=True)
# st=wb.sheet_by_name("一月")
# data=st.cell_value(0,0)
# print(data)


# st = wb.sheet_by_name("1月")
# cols = st.ncols
# rows = st.nrows
# data = st.col_values(2)
# print(sum(data[1:]))


# print("有",cols,"列,有",rows,"行！")


# for i in range(rows):
#     data = st.row_values(i)
#     print(data)


import xlrd
wb = xlrd.open_workbook(filename="2020年每个月的销售情况.xlsx",encoding_override=True)
store = {}
nsheet = wb.nsheets
for i in range(nsheet):
    st = wb.sheet_by_index(i)
    nrow = st.nrows
    for j in range(1,nrow):
        cell = st.row_values(j)
        if cell[1] in store:
          store[cell[1]] ={
            "sum_money":round(store[cell[1]]["sum_money"] + cell[2]*cell[4],2),
            "sum_count":int(store[cell[1]]["sum_count"]+cell[4])
        }
    else:
        store[cell[1]] = {
            "sum_money":round(cell[2]*cell[4],2),
            "sum_count":int(cell[4])
        }
all_sum = sum(store[item]["sum_money"] for item in store)
all_count = sum(store[item]["sum_count"] for item in store)
print("全年的统计总销售额：￥",round(all_sum,2))
print("全年的统计总销售量：",round(all_count,2),"件")
for name in store:
    print("***********************************")
    print(name,"的销售额占比为：",round(store[name]["sum_money"]/all_sum*100,2),"%")
    print(name,"的销售量占比为：",round(store[name]["sum_count"]/all_count*100,2),"%")









































