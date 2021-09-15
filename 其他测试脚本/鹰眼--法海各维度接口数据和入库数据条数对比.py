import pymysql
import requests
import json
from time import sleep
import random

not_wd=['tb_data_classification','tb_data_field_mapping','tb_data_list','tb_data_riskcount_mapping','tb_data_runbatch','tb_data_runbatch_detail','tb_data_source','tb_data_source_services']

print("caiji库各维度表取一个公司和法海对应维度接口条数对比--------")
db = pymysql.connect("xx", "root", "xx", 'caiji')
cur = db.cursor()
cur.execute("show tables")
tables=cur.fetchall()
for i in tables:
    if "tb_data_" in i[0] and "_tyc_" not in i[0] and "2021" not in i[0] and "_party" not in i[0]:
        if i[0] not in not_wd:
            sql = "select DISTINCT param_company from " + i[0]
            cur.execute(sql)
            gss_all=cur.fetchall()
            if gss_all==None or len(gss_all)==0:
                print('----------')
                print("!!!!!---",i[0],'表没有数据，请检查对应维度---',i[0][8:])
            else:
                # 随机取一个公司
                gs=random.choice(gss_all)[0]
                wd=i[0][8:]
                url="http://xx?authCode=xx&q=party:"+gs+"&pageno=1&range=20&dataType="+wd+"&comeFrom=bank"
                res=requests.get(url)
                data=json.loads(res.text)
                if 'totalCount' not in data:
                    print('----------')
                    print('!!!!!!接口请求有问题，请检查')
                    print(data)
                    print('公司：',gs,'，维度:',wd)
                    print(url)
                else:
                    if data['totalCount']==0:
                        print('----------')
                        print('!!!!接口无数据，请检查该公司该维度')
                        print('公司：', gs, '，维度:', wd)
                        print(url)
                    else:
                        fh_num=data['totalCount']
                        sql = "select count(*) from " + i[0]+" where  param_company='"+gs+"'"
                        cur.execute(sql)
                        ku_num=cur.fetchone()[0]
                        if fh_num==ku_num:
                            # print('----------')
                            # print("接口条数和入库条数一致")
                            # print('公司：', gs, '，维度:', wd, "，维度表：", i[0])
                            # print(url)
                            pass
                        else:
                            url = "http://xx?authCode=xx&q=party:" + gs + "&pageno=1&range=20&dataType=" + wd + "&comeFrom=bank"
                            data = requests.get(url)
                            j = json.loads(data.text)
                            # page=j['totalPageNum'] 249
                            s1 = set()
                            print('*****************获取去重数据*********************')
                            a = 1
                            for num in range(1, int(j['totalPageNum']) + 1):
                                print(a, '----', int(j['totalPageNum']))
                                a += 1
                                url = "http://xx?authCode=xx&q=party:" + gs + "&pageno=" + str(num) + "&range=20&dataType=" + wd + "&comeFrom=bank"
                                data = requests.get(url)
                                j = json.loads(data.text)
                                for n in j[wd + 'List']:
                                    s1.add(str(n['entryId']).lower())
                            fhai_num = len(s1)
                            if fhai_num != ku_num:
                                print('----------')
                                print("!!!!!!接口去重后条数和入库条数不一致，请检查")
                                print('去重前：', fh_num, '接口去重后条数：', fhai_num, " 维度表条数:", ku_num)
                                print('公司：', gs, '，维度:', wd, "，维度表：", i)
                                print(url)
                            else:
                                # print('----------')
                                # print("去重后一致")
                                # print('去重前：', fh_num, '接口去重后条数：', fhai_num, " 维度表条数:", ku_num)
                                # print('公司：', gs, '，维度:', wd, "，维度表：", i)
                                # print(url)
                                # print('----------')
                                pass

db.close()


