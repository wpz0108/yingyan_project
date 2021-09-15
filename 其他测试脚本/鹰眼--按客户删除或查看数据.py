import pymysql

"""
进行采集同步的测试时，使用所有客户数据量比较大，跑一次任务太耗时
将客户表换成测试的表，添加两三个客户进行采集，同步测试，之后清除该客户数据，恢复客户表
即任务的测试不影响库中原有数据
其他测试需要知道某客户数据量时也可使用
"""
def data(khs,type,ku):
    for k in ku:
        print('--------------------------')
        if type=='sel':
            print(k,'库查询数据')
        if type=='del':
            print(k,'库清除数据')
        print('--------------------------')
        db = pymysql.connect("xx.104", "root", "xx", 'hawkeye')
        cur = db.cursor()
        cur.execute("select table_name from tb_classification_table where classify_id in (select id from tb_data_classification where source_id in (1,3))")
        tables=cur.fetchall()
        db.close()
        db = pymysql.connect("xx.104", "root", "xx", k)
        cur = db.cursor()
        for kh in khs:
            n=0
            for i in tables:
                # 删除或查询该客户某个维度表数据
                if type=='del':
                    sql = "delete from " + i[0]+' where param_company="'+kh+'"'
                    effect_rows=cur.execute(sql)
                    if effect_rows !=0:
                        print(kh,i[0],'--清除',effect_rows,'行')
                    n+=effect_rows
                elif type=='sel':
                    sql = "select count(*) from " + i[0] + ' where param_company="' + kh + '"'
                    cur.execute(sql)
                    num=cur.fetchone()[0]
                    if num!=0:
                        print(kh,i[0],'--数据量：',num)
                    n+=num
            # 该客户所有维度表的数据量--查询或清除的数据量
            print(n)
        db.commit()
        db.close()
if __name__ == '__main__':

    # khs = ['河北xx有限责任公司','石家庄xx开发有限公司']
    khs = ['伍忠民_xx','王培_xx']
    type = 'sel'
    # type = 'del'
    ku = ['caiji','hawkeye']
    # ku = ['caiji']
    # 查询列表客户在采集应用库的数据量
    data(khs,type,ku)