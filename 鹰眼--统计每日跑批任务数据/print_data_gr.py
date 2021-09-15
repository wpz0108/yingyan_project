import pymysql
import xlrd
from xlutils.copy import copy
import time
from datetime import datetime,date,timedelta
from get_gr_num import gr_num
from ku import c,h

t_name="跑批任务报告-王朋朝.xlsx"
t=time.strftime("%Y-%m-%d",time.localtime())

read=xlrd.open_workbook(t_name,formatting_info=True)

sheet=0
wb=0
if t in read.sheet_names():
    wb=copy(read)
    sheet=wb.get_sheet(t)
else:
    print("没有sheet页：",t)
    exit()

tb_time=(date.today()+timedelta(days=-1)).strftime('%Y-%m-%d ')+'20:00:00'

db = pymysql.connect("xxx", "root", "xx", c)
cur=db.cursor()

# 106节点客户数
sql='''
SELECT task_type, node_sign, thread_name, func_input,
 func_output, func_result, from_unixtime(start_time/1000),
 from_unixtime(end_time/1000) FROM tb_log_task WHERE func_type = 14 AND 
 from_unixtime(create_time/1000) >='''+'"'+tb_time+'"'+" and node_sign like '%172%'"

cur.execute(sql)
res=cur.fetchone()
if not res:
    print('106 个人采集有问题')
    with open('106-p.txt','w',encoding='utf-8') as f:
        f.write(' ')
else:
    l=eval(res[3])
    with open('106-p.txt','w',encoding='utf-8') as f:
        f.write(l[1])
    v=gr_num(106)
    if sheet:
        sheet.write(2,5,l[1].count("name"))
        sheet.write(2,6,v)

# 128节点客户数
sql='''
SELECT task_type, node_sign, thread_name, func_input,
 func_output, func_result, from_unixtime(start_time/1000),
 from_unixtime(end_time/1000) FROM tb_log_task WHERE func_type = 14 AND 
 from_unixtime(create_time/1000) >='''+'"'+tb_time+'"'+" and node_sign like '%128%'"

cur.execute(sql)
res=cur.fetchone()
if not res:
    print('128 个人采集有问题')
    with open('128-p.txt','w',encoding='utf-8') as f:
        f.write(' ')
else:
    l=eval(res[3])
    # print('128 个人数量',l[1].count("name"))
    with open('128-p.txt','w',encoding='utf-8') as f:
        f.write(l[1])
    v=gr_num(128)
    if sheet:
        sheet.write(1,5,l[1].count("name"))
        sheet.write(1,6,v)

if wb:
    wb.save(t_name)


