from add_bq import Bq
from add_gz_gzRes import Gz

def add(x,y):
    gz = Gz('1000302')
    for i in range(x, y):
        name = '测试规则0820--' + str(i)
        gz.add_gz(name)
        print('添加规则：',name)

        name='测试规则结果0820--'+str(i)
        gz.add_gz_res('测试分类',name)
        print('添加结果：',name)
    gz.quit()

    bq = Bq('1000302')
    for i in range(x,y):
        name = '测试统计标签0820---' + str(i)
        bq.add_bq_tj(name)
        print('添加统计标签：', name)

        name = '测试属性标签0820---' + str(i)
        bq.add_bq_sx(name)
        print('添加属性标签：',name)
    bq.quit()

if __name__ == '__main__':
    # 一次自动添加多个标签（统计 属性） 规则 规则结果
    add(1,10)
    print('完成')


