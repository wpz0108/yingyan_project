import pymysql
import time
import xlwt
import xlrd
import  os
from xlutils.copy import copy
import re
# 1下载包， pip3 install xlutils
# 2读取的表改成 gs_sql.xlsx 放到同级目录
# 3执行后生成文件 年-月-日库名-统计标签命中公司溯源数据.xlsx

i_ku="hawkeye"
wb=xlwt.Workbook(encoding='utf-8')
sheet=wb.add_sheet('sheet')
hang=0
t=time.strftime("%Y-%m-%d", time.localtime())
name=str(t)+i_ku+'-统计标签命中公司溯源数据'+'.xlsx'
wb.save(name)

biao=os.path.join(os.getcwd(),name)

gs_sql=xlrd.open_workbook('gs_sql.xlsx')
table_gs=gs_sql.sheet_by_index(0)

hang_num=table_gs.nrows
biaotou=table_gs.row_values(0)

# 写入表头
read=xlrd.open_workbook(biao)
wb=copy(read)
sheet=wb.get_sheet(0)
sheet.write(hang,0,biaotou[0])
sheet.write(hang,1,biaotou[1])
sheet.write(hang,2,biaotou[2])
wb.save(name)
hang=hang+1

# 循环读取的表，得到一行公司-标签-sql数据，处理sql后执行，从原始数据表查询原始数据再写入excel
for i in range(1,hang_num):
    db = pymysql.connect("xx.104", "root", "xx", i_ku)
    cur = db.cursor()
    read = xlrd.open_workbook(biao)
    wb = copy(read)
    sheet = wb.get_sheet(0)

    # 公司名 标签名 sql 表名
    gs=table_gs.row_values(i)[0]
    bqian=table_gs.row_values(i)[1]
    sql=table_gs.row_values(i)[2]
    sql=sql.replace("\n",' ')
    biao_name=re.compile('from(.*?)where').findall(sql)
    sql_exec = sql.replace("${custName}", "'" + gs + "'")

    sheet.write(hang, 0, gs)
    sheet.write(hang, 1, bqian)
    sheet.write(hang, 2, sql_exec)
    hang=hang+1

    # 查表字段写入
    biao_name=biao_name[0].strip(' ')
    sheet.write(hang,0,biao_name+'表原始数据')
    hang=hang+1
    sql_zd="select COLUMN_NAME from information_schema.COLUMNS where table_name = '"+biao_name+"'"
    cur.execute(sql_zd)
    data=cur.fetchall()
    num=0
    for zd in data:
        sheet.write(hang,num,zd[0])
        num=num+1
    hang=hang+1

    # 查原始数据写入
    cur.execute(sql_exec)
    data_rows = cur.fetchall()
    row=0
    for data_row in data_rows:
        num1 = 0
        for data_zd in data_row:
            sheet.write(hang, num1, data_zd)
            num1 = num1 + 1
        hang = hang + 1
        row=row+1
    hang = hang + 1
    wb.save(name)
    db.close()
    print('读取第',i,'行，写入原始数据--公司：',gs,'，标签名：',bqian,'，共',row,'条原始数据')
print('写入完成')

