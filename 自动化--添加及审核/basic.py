import pymysql

def name_sh(str):
    # 页面显示为（xx行/xx部门/name）
    l=str.split('/')
    name=l[len(l)-1].strip('）')
    return name
# 查询所有账号
def get_user():
    db = pymysql.connect("xx", "root", "xx", 'hawkeye')
    cur=db.cursor()
    cur.execute("SELECT user_code,user_name FROM `tb_sys_user` where user_status=1")
    res=cur.fetchall()
    user={}
    for k,v in res:
        user[v]=k
    db.close()
    return user