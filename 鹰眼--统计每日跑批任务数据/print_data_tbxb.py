import pymysql
from datetime import datetime,date,timedelta
import time
import xlrd
import xlwt
from xlutils.copy import copy
t_time=time.strftime('%Y-%m-%d',time.localtime())
t_name='跑批任务报告-王朋朝.xlsx'
from ku import c,h

read=xlrd.open_workbook(t_name,formatting_info=True)
wb=copy(read)
sheet1=wb.get_sheet(t_time)

tb_time=(date.today()+timedelta(days=-1)).strftime('%Y-%m-%d ')+'20:00:00'

db = pymysql.connect("xxx", "root", "xx", c)
cur=db.cursor()

sql="""
SELECT task_type, node_sign, thread_name, func_input,
 func_output, func_result, from_unixtime(start_time/1000),
 from_unixtime(end_time/1000) FROM tb_log_task WHERE func_type = 999 AND 
 node_sign='172.17.0.1' and func_result like '%同步任务开始%' and 
 from_unixtime(create_time/1000) >= """+"'"+tb_time+"' order by start_time desc limit 1"
cur.execute(sql)
res=cur.fetchone()
if not res:
    print('问题')
else:
    print('106 同步开始：',res[6])
    sheet1.write(6,2,res[6])

sql="""
SELECT task_type, node_sign, thread_name, func_input,
 func_output, func_result, from_unixtime(start_time/1000),
 from_unixtime(end_time/1000) FROM tb_log_task WHERE func_type = 999 AND 
 node_sign='172.17.0.1' and func_output like '%同步任务结束%' and 
 from_unixtime(create_time/1000) >= """+"'"+tb_time+"' order by end_time desc limit 1"
cur.execute(sql)
res=cur.fetchone()
if not res:
    print('问题')
else:
    print('106 同步结束：',res[7])
    sheet1.write(6,3,res[7])

sql="""
SELECT task_type, node_sign, thread_name, func_input,
 func_output, func_result, from_unixtime(start_time/1000),
 from_unixtime(end_time/1000) FROM tb_log_task WHERE func_type = 999 AND 
 node_sign='192.168.5.128' and func_result like '%同步任务开始%' and 
 from_unixtime(create_time/1000) >= """+"'"+tb_time+"' order by start_time desc limit 1"
cur.execute(sql)
res=cur.fetchone()
if not res:
    print('问题')
else:
    print('128 同步开始：',res[6])
    sheet1.write(5,2,res[6])

sql="""
SELECT task_type, node_sign, thread_name, func_input,
 func_output, func_result, from_unixtime(start_time/1000),
 from_unixtime(end_time/1000) FROM tb_log_task WHERE func_type = 999 AND 
 node_sign='192.168.5.128' and func_output like '%同步任务结束%' and 
 from_unixtime(create_time/1000) >= """+"'"+tb_time+"' order by end_time desc limit 1"
cur.execute(sql)
res=cur.fetchone()
if not res:
    print('问题')
else:
    print('128 同步结束：',res[7])
    sheet1.write(5,3,res[7])
print('--------------------')

sql="""
SELECT task_type, node_sign, thread_name, func_input,
 func_output, func_result, from_unixtime(start_time/1000),
 from_unixtime(end_time/1000) FROM tb_log_task WHERE func_type = 999 AND 
 node_sign='172.17.0.1' and func_result like '%标签任务开始%' and 
 from_unixtime(create_time/1000) >= """+"'"+tb_time+"' order by start_time desc limit 1"
cur.execute(sql)
res=cur.fetchone()
if not res:
    print('问题')
else:
    print('106 标签开始：',res[6])
    sheet1.write(8,2,res[6])

sql="""
SELECT task_type, node_sign, thread_name, func_input,
 func_output, func_result, from_unixtime(start_time/1000),
 from_unixtime(end_time/1000) FROM tb_log_task WHERE func_type = 999 AND 
 node_sign='172.17.0.1' and func_output like '%标签任务结束%' and 
 from_unixtime(create_time/1000) >= """+"'"+tb_time+"' order by end_time desc limit 1"
cur.execute(sql)
res=cur.fetchone()
if not res:
    print('问题')
else:
    print('106 标签结束：',res[7])
    sheet1.write(8,3,res[7])

sql="""
SELECT task_type, node_sign, thread_name, func_input,
 func_output, func_result, from_unixtime(start_time/1000),
 from_unixtime(end_time/1000) FROM tb_log_task WHERE func_type = 999 AND 
 node_sign='192.168.5.128' and func_result like '%标签任务开始%' and 
 from_unixtime(create_time/1000) >= """+"'"+tb_time+"' order by start_time desc limit 1"
cur.execute(sql)
res=cur.fetchone()
if not res:
    print('问题')
else:
    print('128 标签开始：',res[6])
    sheet1.write(7,2,res[6])

sql="""
SELECT task_type, node_sign, thread_name, func_input,
 func_output, func_result, from_unixtime(start_time/1000),
 from_unixtime(end_time/1000) FROM tb_log_task WHERE func_type = 999 AND 
 node_sign='192.168.5.128' and func_output like '%标签任务结束%' and 
 from_unixtime(create_time/1000) >= """+"'"+tb_time+"' order by end_time desc limit 1"
cur.execute(sql)
res=cur.fetchone()
if not res:
    print('问题')
else:
    print('128 标签结束：',res[7])
    sheet1.write(7,3,res[7])
print('--------------------')

sql="""
SELECT task_type, node_sign, thread_name, func_input,
 func_output, func_result, from_unixtime(start_time/1000),
 from_unixtime(end_time/1000) FROM tb_log_task WHERE func_type = 41 AND 
 node_sign='192.168.5.128' and
 func_result like '%跑批报告画像任务执行开始%' and
 from_unixtime(create_time/1000) >= """+"'"+tb_time+"' order by start_time desc limit 1 "
# print(sql)
cur.execute(sql)
res=cur.fetchone()
if not res:
    print('问题')
else:
    print('128 画像报告开始：',res[6])
    sheet1.write(10,2,res[6])

sql="""
SELECT task_type, node_sign, thread_name, func_input,
 func_output, func_result, from_unixtime(start_time/1000),
 from_unixtime(end_time/1000) FROM tb_log_task WHERE func_type = 41 AND 
 node_sign='192.168.5.128' and
 func_output like '%跑批报告画像任务执行完毕%' and
 from_unixtime(create_time/1000) >= """+"'"+tb_time+"' order by end_time desc limit 1"
cur.execute(sql)
res=cur.fetchone()
if not res:
    print('问题')
else:
    print('128 画像报告结束：',res[7])
    sheet1.write(10,3,res[7])

sql="""
SELECT task_type, node_sign, thread_name, func_input,
 func_output, func_result, from_unixtime(start_time/1000),
 from_unixtime(end_time/1000) FROM tb_log_task WHERE func_type = 41 AND 
 node_sign='172.17.0.1' and
 func_result like '%跑批报告画像任务执行开始%' and
 from_unixtime(create_time/1000) >= """+"'"+tb_time+"' order by start_time desc limit 1 "
cur.execute(sql)
res=cur.fetchone()
if not res:
    print('问题')
else:
    print('106 画像报告开始：',res[6])
    sheet1.write(11,2,res[6])

sql="""
SELECT task_type, node_sign, thread_name, func_input,
 func_output, func_result, from_unixtime(start_time/1000),
 from_unixtime(end_time/1000) FROM tb_log_task WHERE func_type = 41 AND 
 node_sign='172.17.0.1' and
 func_output like '%跑批报告画像任务执行完毕%' and
 from_unixtime(create_time/1000) >= """+"'"+tb_time+"' order by end_time desc limit 1"
cur.execute(sql)
res=cur.fetchone()
if not res:
    print('问题')
else:
    print('106 画像报告结束：',res[7])
    sheet1.write(11,3,res[7])
print('-----------------------------------------------')

wb.save(t_name)





