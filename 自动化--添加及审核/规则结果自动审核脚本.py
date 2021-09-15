from selenium import webdriver
from time import sleep
from add_gz_gzRes import Gz
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

    def audit_gz_res(self,res_name,user,key):
        # 获取待复核人
        self.get_fh_people(res_name,user)
        print('----------')
        print('第', self.id, '级审核')
        print(self.t1)
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
                    self.people_fh(sh_code,res_name,key)
                    print(sh_name,' 审核结束')
                    break

    # 获取标签的当前待审核人 需要登录创建标签的账号上查看待复核人，之后退出
    def get_fh_people(self,res_name,user):
        self.login(user)
        # 定位到规则结果页面
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/section/aside/div/div[14]/div').click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div/div[1]/ul/li[2]/a').click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div/div[2]/div[1]/div/ul/li[2]/div/a').click()
        # 搜索结果名
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div/div[1]/div/div/input').send_keys(res_name)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div/div[2]/div[2]/div/div[1]/div/p').click()
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div/div[2]/div[1]/div[5]/div[2]/table/tbody/tr/td[12]/div/div/span').click()
        # 获取一级复核人时和获取二三级复核人的元素定位不同
        # t是复核状态，t1是复核人信息
        # 格式： 待复核（xx行/xx部门/姓名）
        if self.id==1:
            self.t1 = self.driver.find_element_by_xpath(
                '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div/div[6]/div/div/section/div[1]/form[3]/div[8]/ul/li[1]/div[3]/div[1]').text
            self.t = self.driver.find_element_by_xpath(
                '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div/div[6]/div/div/section/div[1]/form[3]/div[8]/ul/li[1]/div[3]/div[1]/span').text
        else:
            self.t1 = self.driver.find_element_by_xpath(
                '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div/div[7]/div/div/section/div[1]/form[4]/div[8]/ul/li[1]/div[3]/div[1]').text
            self.t = self.driver.find_element_by_xpath(
                '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div/div[7]/div/div/section/div[1]/form[4]/div[8]/ul/li[1]/div[3]/div[1]/span').text
        self.quit()

    #  审核人审核方法,登录进行审核
    def people_fh(self,sh_code,res_name,key):
        #  登录页面
        self.login(sh_code)

        # 待复核结果列表页
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/section/aside/div/div[5]/div/img').click()
        self.driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div/div/div[1]/ul/li[2]/a').click()
        # 搜索，点开审核
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/section/main/div/div/div[2]/div[2]/div[1]/div/div/input').send_keys(res_name)
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/section/main/div/div/div[2]/div[2]/div[1]/div/p').click()
        self.driver.find_element_by_xpath(
            '/html/body/div/div/section/main/div/div/div[2]/div[2]/div[2]/div[1]/div[5]/div[2]/table/tbody/tr/td[11]/div/span/div').click()

        self.driver.implicitly_wait(1)
        # 如果为stop则停止自动审核，否则继续审核
        if key == 0:
            exit()
        # 点击通过
        if key==1:
            self.driver.find_element_by_xpath(
                '/html/body/div[1]/div/section/main/div/div/div[2]/div[2]/div[7]/div/div/section/div[2]/div[1]/div').click()
        # 退回修改
        elif key==2:
            self.driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div/div/div[2]/div[2]/div[7]/div/div/section/div[2]/div[2]/div').click()
            self.driver.implicitly_wait(1)
            self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div[1]/input').send_keys(res_name+'退回')
            self.driver.implicitly_wait(1)
            self.driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/button[2]/span').click()
        # 不予通过
        elif key==3:
            self.driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div/div/div[2]/div[2]/div[7]/div/div/section/div[2]/div[3]/div').click()
        sleep(1)
        self.driver.quit()

    #  查看结果的一级审核页面，key为0，即停止自动审核
    def get_yiji_page(self,res_name,user):
        self.get_fh_people(res_name, user)
        if self.t == '待复核':
            for i in self.audit_people:
                if i==name_sh(self.t1):
                    sh_name = i
                    sh_code = self.audit_people[i]
                    self.quit()
                    #  登录一级审核人账号,0代表不进行后续操作，手动去审核
                    self.people_fh(sh_code, res_name, 0)
                    break

    # 编辑已发布的标签，标签审核通过后为已发布状态，编辑已发布标签即进入第二次审核
    def edit_fabu_gz_res(self,res_name,user):
        self.login(user)
        self.driver.implicitly_wait(1)
        # 定位规则结果列表页面
        self.driver.find_element_by_xpath('/html/body/div[1]/div/section/aside/div/div[14]/div').click()
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div/div[1]/ul/li[2]/a').click()
        # 搜索结果名称
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div/div[2]/div[2]/div/div[1]/div[1]/div/input').send_keys(res_name)
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div/div[2]/div[2]/div/div[1]/div[1]/p').click()
        self.driver.implicitly_wait(1)
        sleep(1)
        # 点编辑
        self.driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div/div[2]/div[2]/div/div[2]/div[1]/div[5]/div[2]/table/tbody/tr/td[12]/div/span[2]').click()
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div/div[3]/div/div/section/div[1]/form/div[2]/div/div/input').clear()
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div/div[3]/div/div/section/div[1]/form/div[2]/div/div/input').send_keys(res_name + '二次')
        sleep(1)
        self.driver.implicitly_wait(1)
        # 提交
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div/div[3]/div/div/section/div[3]/div/div[1]/div').click()

    # 结果的一级退回
    def gz_res_tuihui(self,fenlei,res_name,user):
        # 添加规则结果
        g=Gz(user)
        g.add_gz_res(fenlei,res_name)
        g.quit()
        # 审核 -- 一级退回
        a=Audit()
        a.id=1
        print(res_name)
        a.audit_gz_res(res_name,user,2)
        # 查看结果
        g=Gz(user)
        g.get_gz_res(res_name)

    # 结果的一级不通过
    def gz_res_no(self,fenlei,res_name,user):
        # 添加规则结果
        g = Gz(user)
        g.add_gz_res(fenlei, res_name)
        g.quit()
        # 审核 -- 一级不通过
        a = Audit()
        a.id = 1
        print(res_name)
        a.audit_gz_res(res_name, user, 3)
        # 查看结果
        g = Gz(user)
        g.get_gz_res(res_name)

    # 将方法组合起来，添加规则--审核均通过--查看
    def add_audit_show(self,fenlei,res_name,user):
        # 添加结果
        g = Gz(user)
        g.add_gz_res(fenlei,res_name)
        g.quit()
        print(res_name)
        # 三级审核都通过
        a = Audit()
        a.id = 1
        while a.id <= 3:
            # 等级小于等于3级，就一直调用审核方法（获取待复核人，登录复核人账号审核），1代表选择审核通过
            a.audit_gz_res(res_name,user,1)
            a.id += 1
        # 查看规则
        g = Gz(user)
        g.get_gz_res(res_name)

    # 组合后的方法，编辑已发布规则--审核通过--查看
    def edit_audit_two_show(self,res_name,user):
        # 编辑已发布结果
        a=Audit()
        a.edit_fabu_gz_res(res_name,user)
        a.quit()
        # 三级都审核通过， 1通过
        a=Audit()
        a.id=1
        res_name=res_name+'二次'
        print(res_name)
        while a.id<=3:
            a.audit_gz_res(res_name,user,1)
            a.id+=1
        # 查看该结果
        g = Gz(user)
        g.get_gz_res(res_name)

    def quit(self):
        self.driver.quit()
if __name__ == '__main__':
    a=Audit()
    res_name='测试规则结果-1'
    fenlei='测试'

    # 一级退回
    # a.gz_res_tuihui(fenlei,res_name,'1000302')
    # 一级不予通过
    # a.gz_res_no(fenlei, res_name, '1000302')

    # 添加结果 三级审核通过并查看
    # a.add_audit_show(fenlei,name,'1000302', 'YANshi2021')

    #  已发布结果编辑后，审核通过
    a.edit_audit_two_show(res_name,'1000302')

    # 根据结果名称和提交人账号，调用方法查看一级审核页面
    gz_name = '已创建但未审核的结果名'
    a.get_yiji_page(res_name, '提交人账号')

    # 组合方法进行一级通过 二级退回或一二级通过，三级退回，一级通过，二级不通过等
    # 如一级通过 二级退回
    # 添加
    user = '提交人账号'
    res_name = '测试结果--1'
    g=Gz(user)
    g.add_gz_res(res_name)
    g.quit()
    print(res_name)
    #审核
    # ---------------------------
    a=Audit()
    a.id=1
    # 1通过 2退回修改 3不通过
    # 一级通过 二级退回
    a.audit_gz_res(res_name,user,1)
    a.id+=1
    a.audit_gz_res(res_name, user, 2)
    # ---------------------------
    # 登录提交人账号查看该结果
    g = Gz(user)
    g.get_gz_res(res_name)
