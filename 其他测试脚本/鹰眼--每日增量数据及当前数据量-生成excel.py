import pymysql
import xlwt
import xlrd
from xlutils.copy import copy
from datetime import date,datetime,timedelta
import os
import time

# 查询指定库 caiji,hawkeye-----------
use_ku='caiji'
# --------------------
t=time.strftime("%Y-%m-%d",time.localtime())
sheet_name=str(t)+use_ku

tb_time=(date.today()+timedelta(days=-1)).strftime("%Y%m%d")+'20'
# tb_time='2021052420'
t_name='数据库每日数据及增量数据统计.xls'
if not os.path.exists(os.path.join(os.getcwd(),t_name)):
    wb = xlwt.Workbook(encoding='utf-8')
    wb.add_sheet('test')
    wb.save(t_name)
not_wd=['tb_data_classification','tb_data_field_mapping','tb_data_list','tb_data_riskcount_mapping','tb_data_runbatch','tb_data_runbatch_detail','tb_data_source','tb_data_source_services']

db = pymysql.connect("xx", "root", "xx", 'hawkeye')
cur = db.cursor()
# cur.execute("show tables")
cur.execute("select table_name from tb_classification_table where classify_id in (select id from tb_data_classification where source_id in (1,3))")
tables=cur.fetchall()
db.close()
db = pymysql.connect("xx", "root", "xx", use_ku)
cur=db.cursor()
zong_num=0
zong_num_add=0
zong_data=0
read = xlrd.open_workbook(t_name)
wb = copy(read)
try:
    sheet=wb.add_sheet(sheet_name)
except:
    sheet=wb.get_sheet(sheet_name)

hang=0
sheet.write(hang,0,'表名')
sheet.write(hang,1,'当前数据量')
sheet.write(hang,2,'当前数据大小(M)')
sheet.write(hang,3,'当日增加数据量')
hang+=1

for i in tables:
    if "tb_data_" in i[0] and '2021' not in i[0]:
        if i[0] not in not_wd:
            # 表名
            table_name=i[0]
            sql = "select count(*) from " + i[0]
            cur.execute(sql)
            # 当前数据量
            num=cur.fetchone()[0]
            zong_num=zong_num+num
            sql="select count(*) from "+table_name+" where FROM_UNIXTIME(update_time/1000, '%Y%m%d%H')>="+tb_time
            cur.execute(sql)
            # 增量数据
            zeng_num=cur.fetchone()[0]
            zong_num_add=zong_num_add+zeng_num
            # 当前空间
            sql="SELECT (data_length+index_length)/1024/1024 as data FROM information_schema.TABLES where TABLE_SCHEMA =  'caiji' and TABLE_NAME='"+table_name+"'"
            cur.execute(sql)
            data=cur.fetchone()[0]
            zong_data+=data
            # print(sql)

            sheet.write(hang,0,table_name)
            sheet.write(hang,1,num)
            sheet.write(hang,2,data)
            sheet.write(hang,3,zeng_num)
            hang+=1

sheet.write(hang,0,'总计')
sheet.write(hang,1,zong_num)
sheet.write(hang,2,zong_data)
sheet.write(hang,3,zong_num_add)

hang+=1
# 查询采集库数据时有记录采集开始结束时间，应用库为采集库同步过去的数据
if use_ku=='caiji':
    sql="select count(*) from tb_batch_progress where FROM_UNIXTIME(start_time/1000, '%Y%m%d%H')>="+tb_time
    # print(sql)
    cur.execute(sql)
    x=cur.fetchone()[0]
    if  x:
        sql="select FROM_UNIXTIME(start_time/1000, '%Y-%m-%d %H:%i:%S') as st,FROM_UNIXTIME(end_time/1000, '%Y-%m-%d %H:%i:%s') as em from tb_batch_progress where FROM_UNIXTIME(start_time/1000, '%Y%m%d%H')>="+tb_time+" order by start_time desc"
        cur.execute(sql)
        # print(sql)
        data=cur.fetchone()
        sheet.write(hang,0,'开始时间')
        sheet.write(hang,1,data[0])
        hang+=1
        sheet.write(hang, 0, '结束时间')
        sheet.write(hang, 1, data[1])
        hang+=1

wb.save(t_name)
db.close()
print('结束')
