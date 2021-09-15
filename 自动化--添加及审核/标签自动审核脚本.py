from selenium import webdriver
from time import sleep
from add_bq import Bq
from basic import get_user,name_sh

class Audit():
    def __init__(self):
        self.audit_people=get_user()
        # 当前为第几级审核
        self.id=0
        self.url='xx'
        self.pwd='xx'

    def login(self,user):
        # 登录页面
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div[3]/div/input').send_keys(user)
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div[4]/div/input').send_keys(self.pwd)
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div[5]/div/input').send_keys('a')
        # 点击登录
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div[6]').click()

    #审核标签方法，调用获取待复核人方法，调用复核人方法复核
    def audit_bq(self,bq_name,user,key):
        # 获取复核人
        self.get_fh_people(bq_name,user)
        print('----------')
        print('第',self.id,'级审核')
        print('----------')
        if self.t=='待复核':
            for i in self.audit_people:
                # 页面t1显示为（xx行/xx部门/name）
                # 循环所有账号，如果姓名和页面截取的复核人姓名一致，则取该姓名对应的账号
                if i==name_sh(self.t1):
                    # 审核人姓名
                    sh_name=i
                    print(sh_name,' 开始审核')
                    # 审核人账号
                    sh_code=self.audit_people[i]
                    # 调用获取复核人方法获取复核人(登录创建标签的账号上查看)后需要退出，再登录复核人账号取审核
                    self.quit()
                    # 登录复核人账号审核
                    self.people_fh(sh_code,bq_name,key)
                    print(sh_name,' 审核结束')
                    break

    # 获取标签的当前待审核人 需要登录创建标签的账号上查看待复核人，之后退出
    def get_fh_people(self,bq_name,user):
        self.login(user)
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/section/aside/div/div[13]/div/img').click()
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div/div[1]/ul/li[2]/div/a').click()
        self.driver.implicitly_wait(1)
        # 搜索
        self.driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[1]/div[1]/div/div/input').send_keys(bq_name)
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[1]/div[1]/div/p').click()

        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/div[1]/div[5]/div[2]/table/tbody/tr/td[12]/div/span/div').click()
        self.driver.implicitly_wait(1)
        # 获取一级复核人时和获取二三级复核人的元素定位不同
        # t是复核状态，t1是复核人信息
        # 格式： 待复核（xx行/xx部门/姓名）
        if self.id==1:
            self.t=self.driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[2]/div/div/section/div[1]/div[4]/div/ul/li[1]/div[3]/div[1]/span').text
            self.t1=self.driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[2]/div/div/section/div[1]/div[4]/div/ul/li[1]/div[3]/div[1]').text
        else:
            self.t = self.driver.find_element_by_xpath(
                '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[6]/div/div/section/div[1]/div[5]/div/ul/li[1]/div[3]/div[1]/span').text
            self.t1 = self.driver.find_element_by_xpath(
                '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[6]/div/div/section/div[1]/div[5]/div/ul/li[1]/div[3]/div[1]').text
        self.quit()

        #  审核人审核方法,登录进行审核
    def people_fh(self,sh_code,bq_name,key):
        #  登录页面
        self.login(sh_code)
        # 复核标签列表页
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/section/aside/div/div[5]/div/img').click()
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div/div/div[1]/ul/li[4]/a').click()
        self.driver.implicitly_wait(1)
        # 搜索标签名，点开审核页面
        self.driver.find_element_by_xpath('/html/body/div/div/section/main/div/div/div[2]/div[2]/div[1]/div/div/input').send_keys(bq_name)
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath('/html/body/div/div/section/main/div/div/div[2]/div[2]/div[1]/div/p').click()
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath('/html/body/div/div/section/main/div/div/div[2]/div[2]/div[2]/div[1]/div[5]/div[2]/table/tbody/tr/td[10]/div/span/div').click()
        self.driver.implicitly_wait(1)
        # 如果为stop则停止自动审核，否则继续审核
        if key==0:
            exit()
        # 通过
        if key==1:
            self.driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div/div/div[2]/div[2]/div[7]/div/div/section/div[2]/div[1]/div').click()
        # 退回修改
        elif key == 2:
            self.driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div/div/div[2]/div[2]/div[7]/div/div/section/div[2]/div[2]/div').click()
        # 不通过
        elif key == 3:
            self.driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div/div/div[2]/div[2]/div[7]/div/div/section/div[2]/div[3]/div').click()

        sleep(1)
        self.driver.quit()

    #  查看标签的一级审核页面，key为0，即停止自动审核
    def get_yiji_page(self,bq_name,user):
        self.get_fh_people(bq_name,user)
        if self.t == '待复核':
            for i in self.audit_people:
                if i == name_sh(self.t1):
                    sh_name = i
                    sh_code = self.audit_people[i]
                    self.quit()
                    #  登录一级审核人账号,0代表不进行后续操作，手动去审核
                    self.people_fh(sh_code, bq_name, 0)
                    break

    # 编辑已发布的标签，标签审核通过后为已发布状态，编辑已发布标签即进入第二次审核
    def edit_fabu_bq(self,bq_name,user):
        self.login(user)
        self.driver.implicitly_wait(1)
        # 选择标签管理模块
        self.driver.find_element_by_xpath('/html/body/div[1]/div/section/aside/div/div[13]/div').click()
        sleep(1)
        # 搜索标签
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[1]/div[1]/div/input').send_keys(bq_name)
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[1]/div[1]/p').click()
        self.driver.implicitly_wait(1)
        sleep(1)
        # 点编辑
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[2]/div[1]/div[5]/div[2]/table/tbody/tr/td[11]/div/span[2]').click()
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[4]/div/div/section/div[1]/form/div[2]/div/div/input').clear()
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[4]/div/div/section/div[1]/form/div[2]/div/div/input').send_keys(bq_name + '二次')
        sleep(1)
        self.driver.implicitly_wait(1)
        # 提交
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[4]/div/div/section/div[3]/div/div[1]/div').click()

    # 将方法组合起来，添加标签--审核均通过--查看
    def add_audit_show(self,bq_name,user,fenlei):
        # 添加标签
        b = Bq(user)
        if fenlei=='sx':
            b.add_bq_sx(bq_name+'sx')
        elif fenlei=='tj':
            b.add_bq_tj(bq_name+'tj')
        b.quit()
        print(bq_name)
        # 三级审核都通过
        a = Audit()
        a.id = 1
        while a.id <= 3:
            # 等级小于等于3级，就一直调用审核标签方法（获取待复核人，登录复核人账号审核），1代表选择审核通过
            a.audit_bq(bq_name, user,1)
            a.id += 1
        # 查看该标签
        b = Bq(user)
        b.get_bq(bq_name)

    # 组合后的方法，编辑已发布标签--审核通过--查看
    def edit_audit_two_show(self,bq_name,user):
        # 编辑已发布规则
        a=Audit()
        a.edit_fabu_bq(bq_name,user)
        a.quit()
        # 三级都审核通过， 1通过
        a=Audit()
        a.id=1
        bq_name=bq_name+'二次'
        print(bq_name)
        while a.id<=3:
            a.audit_bq(bq_name,user,1)
            a.id+=1
        b = Bq(user)
        # 查看
        b.get_bq(bq_name)

    def quit(self):
        self.driver.quit()

if __name__ == '__main__':
    a=Audit()
    bq_name='测试统计标签0819-1'

    # 添加tj标签 三级审核通过并查看该标签
    a.add_audit_show(bq_name,'提交人账号','tj')

    # 已发布编辑 审核 查看
    a.edit_audit_two_show(bq_name,'编辑人账号')

    # 根据标签名和提交人，调用方法查看一级审核页面
    bq_name='已创建但未审核的标签名'
    a.get_yiji_page(bq_name,'提交人账号')

    # 组合方法进行一级通过 二级退回或一二级通过，三级退回，一级通过，二级不通过等
    # 如一级通过 二级退回
    # 添加
    user='提交人账号'
    b=Bq(user)
    bq_name='测试统计标签-1'
    b.add_bq_tj(bq_name)
    b.quit()

    print(bq_name)
    # 审核
    # ---------------------------
    a = Audit()
    a.id = 1
    # 1通过 2退回修改 3不通过
    # 一级通过 二级退回
    a.audit_bq(bq_name, user, 1)
    a.id+=1
    a.audit_bq(bq_name, user, 2)
    # ---------------------------
    b = Bq(user)
    # 登录提交人账号查看该标签
    b.get_bq(bq_name)

