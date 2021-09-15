# encoding:utf-8
from time import sleep
from selenium import webdriver

class Bq():
    def __init__(self,user):
        # 登录地址和密码固定
        self.driver = webdriver.Firefox()
        self.driver.get('url')
        self.driver.maximize_window()
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div[3]/div/input').send_keys(user)
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div[4]/div/input').send_keys('xx')
        # 验证码为任意值可登录
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div[5]/div/input').send_keys('a')
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div[6]').click()
    def quit(self):
        self.driver.quit()
    #     添加属性标签
    def add_bq_sx(self, name):
        sleep(1)
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/section/aside/div/div[14]/div/img').click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/section/aside/div/div[13]/div/img').click()
        self.driver.implicitly_wait(2)
        # 新增按钮
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/div').click()
        self.driver.implicitly_wait(2)
        # 分类
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[4]/div/div/section/div[1]/form/div[1]/div/div/div/input').click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div[1]/ul/li[2]/label/span[1]/span').click()
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[4]/div/div/section/div[1]/form/div[1]/div/div/div/input').click()
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[4]/div/div/section/div[1]/form/div[2]/div/div/input').send_keys(name)
        self.driver.implicitly_wait(2)
        # 字段名 属性标签
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[4]/div/div/section/div[1]/form/div[5]/div/div[1]/div[1]/input').click()
        self.driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[1]/div[1]/ul/li[1]/span').click()
        self.driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[2]/div[1]/ul/li[1]/span').click()
        self.driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[3]/div[1]/ul/li[1]/label/span[1]/span').click()
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[4]/div/div/section/div[1]/form/div[5]/div/div[1]/div[1]/input').click()

        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[4]/div/div/section/div[1]/form/div[5]/div/div[2]/div/input').click()
        self.driver.find_element_by_xpath('/html/body/div[7]/div[1]/div[1]/ul/li[1]/span').click()

        self.driver.implicitly_wait(2)
        # 标签值类型
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[4]/div/div/section/div[1]/form/div[6]/div/div/div[1]/input').click()
        self.driver.find_element_by_xpath('/html/body/div[8]/div[1]/div[1]/ul/li[1]').click()
        # 禁用
        self.driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[4]/div/div/section/div[1]/form/div[9]/div/div/label[2]/span[1]/span').click()
        sleep(1)
        # 保存
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[4]/div/div/section/div[2]/div/div[1]/div').click()

    # 添加统计标签
    def add_bq_tj(self, name):
        sleep(1)
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/section/aside/div/div[14]/div/img').click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/section/aside/div/div[13]/div/img').click()

        self.driver.implicitly_wait(2)
        # 新增按钮
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[1]/div[2]/div').click()
        self.driver.implicitly_wait(2)
        # 分类
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[4]/div/div/section/div[1]/form/div[1]/div/div/div/input').click()
        self.driver.implicitly_wait(2)
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div[1]/ul/li[2]/label/span[1]/span').click()
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[4]/div/div/section/div[1]/form/div[1]/div/div/div/input').click()

        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[4]/div/div/section/div[1]/form/div[2]/div/div/input').send_keys(name)

        self.driver.implicitly_wait(2)
        # 统计标签
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[4]/div/div/section/div[1]/form/div[3]/div/div/div/input').click()
        self.driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[1]/ul/li[2]').click()

        # 脚本 统计标签
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[4]/div/div/section/div[1]/form/div[5]/div/div/textarea').send_keys(
            "select * from a")
        # 溯源脚本
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[4]/div/div/section/div[1]/form/div[6]/div/div[1]/textarea').send_keys(
            "select * from a")

        self.driver.implicitly_wait(2)
        # 标签值类型
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[4]/div/div/section/div[1]/form/div[7]/div/div/div/input').click()
        self.driver.find_element_by_xpath('/html/body/div[7]/div[1]/div[1]/ul/li[1]/span').click()
        # 禁用
        self.driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[4]/div/div/section/div[1]/form/div[10]/div/div/label[2]/span[2]').click()
        sleep(1)
        # 保存
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[4]/div/div/section/div[2]/div/div[1]/div').click()
    # 打开指定标签页面
    def get_bq(self,name):
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/section/aside/div/div[13]/div/img').click()
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div/div[1]/ul/li[2]/div/a').click()
        self.driver.implicitly_wait(1)
        # 搜索
        self.driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[1]/div[1]/div/div/input').send_keys(name)
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[1]/div[1]/div/p').click()
if __name__ == '__main__':
    bq = Bq('1000328')
    for i in range(1,5):
        name='测试统计标签0819-'+str(i)
        bq.add_bq_tj(name)
        name = '测试属性标签0819-' + str(i)
        bq.add_bq_sx(name)
    bq.quit()

