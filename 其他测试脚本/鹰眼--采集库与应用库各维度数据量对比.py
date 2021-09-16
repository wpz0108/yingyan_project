import pymysql
from time import sleep

ku=['caiji','hawkeye']

caiji={}
ying={}
kong_wd=[]
no_wd=[]

# 获取要查询的表名
db = pymysql.connect("xx.104", "root", "xx", 'hawkeye')
cur = db.cursor()
cur.execute("select table_name from tb_classification_table where classify_id in (select id from tb_data_classification where source_id in (1,3))")
tables=cur.fetchall()
db.close()

# 循环表，查询采集库该表及对应的数据量存到字典中
db = pymysql.connect("xx.104", "root", "xx", 'caiji')
cur=db.cursor()
for i in tables:
    tname=i[0]
    sql="select count(*) from "+tname
    cur.execute(sql)
    num=cur.fetchone()[0]
    caiji[tname]=num
    if num==0:
       kong_wd.append(tname)
db.close()

# 循环表名，查询应用库该表数据量并与采集库对应表的数据量对比
db = pymysql.connect("xx.104", "root", "xx",'hawkeye')
cur = db.cursor()
for table in caiji.keys():
    caiji_num=caiji[table]
    sql="select count(*) from "+table
    cur.execute(sql)
    ying_num=cur.fetchone()[0]
    if ying_num!=caiji_num:
        print('------------')
        print(table,"表采集库与应用库条数不一致")
        print('采集库:',caiji_num,' 应用库:',ying_num)
        print('------------')
        no_wd.append(table)
    else:
        # print(table, "表采集库与应用库条数一致",'采集库:',caiji_num,' 应用库:',ying_num)
        pass
    # sleep(0.5)

print('无数据的维度：',kong_wd)
print('数据量不同的维度 ',no_wd)
db.close()

# exit()
print('-------------根据昨日跑批批次号request_number查不一致维度的最新的同步数据量，修改id中的request_number-------------------')
db1 = pymysql.connect("xx.104", "root", "xx",'caiji')
db2 = pymysql.connect("xx.104", "root", "xx",'hawkeye')
cur1 = db1.cursor()
cur2 = db2.cursor()
# 昨日采集任务批次号，企业个人各一个
id = ['FH_TYC_C_B_1625216923292_25f5f8f27c994754886bc2c2b0386c94',
      'FH_TYC_C_B_1625216923383_c98b5aa7925d4809acb97bfd3888dcba']
for no in no_wd:
    for i in id:
        sql = 'select count(*) from ' + no + ' where request_number like "%' + i + '%"'
        cur1.execute(sql)
        cai = cur1.fetchone()[0]
        cur2.execute(sql)
        haw = cur2.fetchone()[0]
        if cai == haw:
            # print('一致')
            pass
        else:
            print('根据批次号查询仍不一致的维度:',no, ' caiji:', cai, ' hawkeye:', haw, ' 对应批次号：',i)
db1.close()
db2.close()


