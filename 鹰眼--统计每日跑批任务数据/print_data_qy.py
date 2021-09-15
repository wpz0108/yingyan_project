import pymysql
from datetime import date,datetime,timedelta
import time
import xlrd
import xlwt
from xlutils.copy import copy
t_time=time.strftime('%Y-%m-%d',time.localtime())
t_name='跑批任务报告-王朋朝.xlsx'
from ku import c,h

tb_time = (date.today() + timedelta(days=-1)).strftime("%Y%m%d")
db = pymysql.connect("xxx", "root", "xx", h)
cur1 = db.cursor()
# 法海风控分类是1 天眼查是3
sql = "select table_name from tb_classification_table where classify_id in (select id from tb_data_classification where source_id in (1,3) )"
cur1.execute(sql)
tables = cur1.fetchall()
db.close()

# gs='xx公司'
def gs_num(gs, cur):
    num = 0
    for t in tables:
        table_name = t[0]
        sql = "select count(*) from " + table_name + " where FROM_UNIXTIME(update_time/1000, '%Y%m%d')=" + tb_time + " and param_company=" + "'" + gs + "'"
        # sql = "select count(*) from " + table_name + " where  param_company=" + "'" + gs + "'"
        cur.execute(sql)
        n = cur.fetchone()[0]
        num += n
    return num

def all_data(gs):
    num=len(gs)
    all=0
    db = pymysql.connect("xxx", "root", "xx", c)
    cur = db.cursor()
    for g in gs:
        x=gs_num(g,cur)
        all+=x
    db.close()
    # print('所有公司数据量：',all)
    return num,all
def all_data_new(kh):
    num=len(kh)
    all=0
    db = pymysql.connect("xxx", "root", "xx", c)
    cur = db.cursor()
    for t in tables:
        table_name = t[0]
        sql = "select count(*) from " + table_name + " where FROM_UNIXTIME(update_time/1000, '%Y%m%d')=" + tb_time + " and param_company in " +str(kh)
        # sql = "select count(*) from " + table_name + " where  param_company=" + "'" + gs + "'"
        cur.execute(sql)
        n = cur.fetchone()[0]
        all += n
    return num,all

def shuju():
    read=xlrd.open_workbook(t_name,formatting_info=True)
    wb = copy(read)
    sheet1 = wb.get_sheet(t_time)

    tb_time=(date.today()+timedelta(days=-1)).strftime('%Y-%m-%d ')+'22:00:00'
    db = pymysql.connect("xxx", "root", "xx", c)
    cur=db.cursor()

    sql="""
    SELECT task_type, node_sign, thread_name, func_input,
     func_output, func_result, from_unixtime(start_time/1000),
     from_unixtime(end_time/1000) FROM tb_log_task WHERE func_type = 999 AND
      func_result like '%采集任务开始%' and node_sign='192.168.5.128' 
    and from_unixtime(create_time/1000) >= """+"'"+tb_time+"' limit 1"
    cur.execute(sql)
    res=cur.fetchone()
    if not res:
        print('128节点公司采集开始有问题')
    else:
        # 调用方法查数量，数据量
        kh=eval(res[3])[1]
        # 用新方法统计数据
        # num,all=all_data(kh)
        num,all=all_data_new(tuple(kh))
        print('192.168.5.128',' 公司采集开始时间',res[6])
        sheet1.write(3,2,res[6])
        print('公司数：',num,' 当日新增数据量：',all)
        sheet1.write(3,5,num)
        sheet1.write(3,6,all)

    sql = """
        SELECT task_type, node_sign, thread_name, func_input,
         func_output, func_result, from_unixtime(start_time/1000),
         from_unixtime(end_time/1000) FROM tb_log_task WHERE func_type = 999 AND
          func_output like '%采集任务结束%' and node_sign='192.168.5.128' 
        and from_unixtime(create_time/1000) >= """ + "'" + tb_time + "' limit 1"
    cur.execute(sql)
    res = cur.fetchone()
    if not res:
        print("128公司采集结束有问题")
    else:
        print('结束时间：',res[7])
        sheet1.write(3, 3, res[7])
    print('-------------------------')

    sql="""
    SELECT task_type, node_sign, thread_name, func_input,
     func_output, func_result, from_unixtime(start_time/1000),
     from_unixtime(end_time/1000) FROM tb_log_task WHERE func_type = 999 AND
      func_result like '%采集任务开始%' and node_sign='172.17.0.1' 
    and from_unixtime(create_time/1000) >= """+"'"+tb_time+"' limit 1"
    cur.execute(sql)
    res=cur.fetchone()
    if not res:
        print("106公司采集开始有问题")
    else:
        # 调用方法查数量，数据量
        kh=eval(res[3])[1]
        # num,all=all_data(kh)
        num, all = all_data_new(tuple(kh))
        print('172.17.0.1',' 公司采集开始时间',res[6])
        sheet1.write(4, 2, res[6])
        print('公司数：',num,' 当日新增数据量：',all)
        sheet1.write(4,5,num)
        sheet1.write(4,6,all)

    sql="""
    SELECT task_type, node_sign, thread_name, func_input,
     func_output, func_result, from_unixtime(start_time/1000),
     from_unixtime(end_time/1000) FROM tb_log_task WHERE func_type = 999 AND
      func_output like '%采集任务结束%' and node_sign='172.17.0.1' 
    and from_unixtime(create_time/1000) >= """+"'"+tb_time+"' limit 1"
    cur.execute(sql)
    res=cur.fetchone()
    if not res:
        print("106公司采集结束有问题")
    else:
        print('结束时间：', res[7])
        sheet1.write(4, 3, res[7])
    print('-------------------------')
    wb.save(t_name)
if __name__ == '__main__':
    shuju()
