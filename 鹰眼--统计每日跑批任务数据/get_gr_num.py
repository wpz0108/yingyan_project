import re
from datetime import timedelta, date
import pymysql
from ku import c,h

tb_time=(date.today()+timedelta(days=-1)).strftime('%Y-%m-%d ')+'20:00:00'

def gr_num(node):
    with open(str(node)+'-p.txt','r',encoding='utf-8') as f:
        str1=f.read()
    if str1!=' ':
        name=re.findall("name=(.*?)\,",str1)
        number=re.findall("idcardNo=(.*?)\}",str1)
        d=[]
        for i in range(len(name)):
            d.append(name[i]+'_'+number[i])

        wd=['tb_data_ajlc_party','tb_data_bgt_party','tb_data_cpws_party','tb_data_fygg_party','tb_data_ktgg_party','tb_data_shixin_party','tb_data_zxgg_party','tb_data_ajlc', 'tb_data_bgt', 'tb_data_cpws', 'tb_data_fygg', 'tb_data_ktgg', 'tb_data_shixin', 'tb_data_zxgg']

        db = pymysql.connect("xxx", "root", "xx", c)
        cur = db.cursor()
        gr=str(tuple(d))
        all=0
        for i in wd:
            sql="select count(*) from "+i+" where from_unixtime(update_time/1000,'%Y%m%d')='"+tb_time+"' and param_company in "+ gr
            cur.execute(sql)
            num=cur.fetchone()[0]
            all+=num
        print(node,' 个人客户数：',len(d),' 当日新增数据量：',all)
        return all
    else:
        print(node,'有问题，没有读取到客户')
        return '有问题'
if __name__ == '__main__':
    gr_num(128)