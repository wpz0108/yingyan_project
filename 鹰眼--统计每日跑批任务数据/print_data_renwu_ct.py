import pymysql
from datetime import date,datetime,timedelta
from ku import c,h
import time
import xlrd
import xlwt
from xlutils.copy import copy
t_time=time.strftime('%Y-%m-%d',time.localtime())
# t_name='测试报告-王朋朝-'+t_time+'.xlsx'
t_name='跑批任务报告-王朋朝.xlsx'

tb_time=(date.today()+timedelta(days=-1)).strftime("%Y%m%d")+'20'

def zeng(gs,use_ku,time_x):
    not_wd=['tb_data_classification','tb_data_field_mapping','tb_data_list','tb_data_riskcount_mapping','tb_data_runbatch','tb_data_runbatch_detail','tb_data_source','tb_data_source_services','tb_data_runbatch_history']

    db = pymysql.connect("xxx", "root", "xx", h)
    cur = db.cursor()
    cur.execute("select table_name from tb_classification_table where classify_id in (select id from tb_data_classification where source_id in (1,3))")
    tables=cur.fetchall()
    db.close()

    db = pymysql.connect("xxx", "root", "xx", use_ku)
    cur=db.cursor()
    db_h = pymysql.connect("xxx", "root", "xx", h)
    cur_h=db_h.cursor()
    zong_add=0
    if time_x =='update_time' or time_x=='create_time':
        for i in tables:
            # if "tb_data_" in i[0]:
            if "tb_data_" in i[0] and '2021' not in i[0]:
                # 表名
                table_name=i[0]
                sql = "select count(*) from " + table_name + " where FROM_UNIXTIME(" + time_x + "/1000, '%Y%m%d')=" + tb_time + ' and param_company in ' + str(gs)
                # print(sql)
                cur.execute(sql)
                # 增量数据
                zeng_num=cur.fetchone()[0]
                zong_add+=zeng_num

        db.close()
        db_h.close()
        return zong_add
    elif time_x == 'c_time':
        sql = "select count(*) from tb_dimension_history where FROM_UNIXTIME(create_time/1000, '%Y%m%d')=" + tb_time + ' and customer_code in ' + str(gs)
        # print(sql)
        cur_h.execute(sql)
        num=cur_h.fetchone()[0]
        db.close()
        db_h.close()
        return num

def data():
    all_gs=[]
    all_gr=[]
    db = pymysql.connect("xxx", "root", "xx", h)
    cur = db.cursor()
    cur.execute('select DISTINCT customer_name from tb_manage_customer where is_delete=0 union select customer_relation_name from tb_relation_customer where customer_type="C"')
    res=cur.fetchall()
    for i in res:
        all_gs.append(i[0])
    cur.execute('select  customer_name,id_number from tb_manager_customer_personal where is_delete=0 union select customer_relation_name,id_number from tb_relation_customer where customer_type="P"')
    res_p=cur.fetchall()
    for k,v in res_p:
        all_gr.append(k+'_'+str(v))
    # print(all_gr)
    # exit()
    print('统计'+tb_time)


    # 新增公司----填写公司-------
    new=['name']
    # 新增个人----填写个人
    new_p=['name_card', 'name_card']

    for i in new:
        all_gs.remove(i)
    if len(new)==1:
        new=str(tuple(new)).replace(',','')
    else:
        new=str(tuple(new))

    for v in new_p:
        all_gr.remove(v)
    if len(new_p)==1:
        new_p=str(tuple(new_p)).replace(',','')
    else:
        new_p=str(tuple(new_p))


    read=xlrd.open_workbook(t_name,formatting_info=True)
    wb=copy(read)
    sheet=wb.get_sheet(t_time)

    # 方法中的方法
    def qy():
        num11 = zeng(tuple(all_gs), c, 'create_time')
        print('存量企业采集-新增：',num11)
        sheet.write(16,1,num11)
        num333 = zeng(tuple(all_gs), c, 'update_time')
        print('存量企业采集-更新：', num333-num11)
        sheet.write(16,2,num333-num11)
        num3 = zeng(tuple(all_gs), h, 'update_time')
        print('存量企业同步量：',num3)
        sheet.write(16,3, num3)


        num11 = zeng(new, 'caiji', 'create_time')
        print('新增企业采集-新增：',num11)
        sheet.write(17,1,num11)
        num333 = zeng(new, 'caiji', 'update_time')
        print('新增企业采集-更新：', num333-num11)
        sheet.write(17,2,num333-num11)
        num3 = zeng(new, 'hawkeye', 'update_time')
        print('新增企业同步量：',num3)
        sheet.write(17,3, num3)
    qy()

    def gr():
        num11 = zeng(tuple(all_gr), c, 'create_time')
        print('存量个人采集-新增：',num11)
        sheet.write(18,1,num11)
        num333 = zeng(tuple(all_gr), c, 'update_time')
        print('存量个人采集-更新：', num333-num11)
        sheet.write(18,2,num333-num11)
        num3 = zeng(tuple(all_gr), h, 'update_time')
        print('存量个人同步量：',num3)
        sheet.write(18,3, num3)

        num11 = zeng(new_p, 'caiji', 'create_time')
        print('新增个人采集-新增：',num11)
        sheet.write(19,1,num11)
        num333 = zeng(new_p, 'caiji', 'update_time')
        print('新增个人采集-更新：', num333-num11)
        sheet.write(19,2,num333-num11)
        num3 = zeng(new_p, 'hawkeye', 'update_time')
        print('新增个人同步量：',num3)
        sheet.write(19,3, num3)
    gr()

    wb.save(t_name)
    db.close()

if __name__ == '__main__':
    data()