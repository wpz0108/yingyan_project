import pymysql
from datetime import date,datetime,timedelta

def del_data(ku,key):
    # 跑批时间 昨天晚上10点
    tb_time = (date.today() + timedelta(days=-1)).strftime("%Y%m%d") + '22'
    # 查询所有原始表 法海-1 天眼查-3 如 tb_data_cpws tb_data_tyc_qygg
    db = pymysql.connect("xx", "root", "xx", 'hawkeye')
    cur = db.cursor()
    cur.execute("select table_name from tb_classification_table where classify_id in (select id from tb_data_classification where source_id in (1,3))")
    tables = cur.fetchall()

    for k in ku:
        print('--------------------------')
        print(i,'库清除数据')
        print('--------------------------')
        # 101---开发 104----测试
        db = pymysql.connect("xx.104", "root", "xx", k)
        cur = db.cursor()
        #清除数据或删除昨天采集任务采集的数据
        for i in tables:
            if key=='all':
                sql = "truncate " + i[0]
            else:
                sql = "delete from  " + i[0]+" where from_unixtime(create_time/1000,'%Y%m%d%H')>='"+tb_time+"'"
            cur.execute(sql)
            print(i[0],'表清除完成')
        db.commit()
        # 如果是清空数据 则查询是否有表未清除完
        if key=='all':
            for i in tables:
                sql="select count(*) from "+i[0]
                cur.execute(sql)
                num=cur.fetchone()[0]
                if num!=0:
                    print(i[0],'表未清除完，数据量：',num)
        db.close()
if __name__ == '__main__':
    # 要清除的库名
    ku = ['caiji', 'hawkeye']
    # ku=['caiji_shenzhen','hawkeye_shenzhen']

    # 清除全部原始数据 key为all即清除全部 为任意其他字符为清除昨天跑批数据
    del_data(ku,'all')
    # 清除昨天跑批采集的数据 key任意字符
    # del_data(ku,1)
