# encoding:utf-8
from time import sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

class Gz():
    def __init__(self,user):
        self.driver = webdriver.Firefox()
        self.driver.get('url')
        self.driver.maximize_window()
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div[3]/div/input').send_keys(user)
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div[4]/div/input').send_keys('xxx')
        # 任意可登录
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div[5]/div/input').send_keys('a')
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div[6]').click()

    # 添加规则
    def add_gz(self,name):
        sleep(1)
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/section/aside/div/div[13]/div/img').click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/section/aside/div/div[14]/div/img').click()
        self.driver.implicitly_wait(2)
        # 新增按钮
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[2]/div/div[1]/div[2]').click()
        self.driver.implicitly_wait(2)
        # 分类
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[2]/div/div[3]/div/div/section/div[1]/form/div[1]/div/div/div/input').click()
        self.driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div[1]/ul/li[4]/label/span[1]/span').click()
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[2]/div/div[3]/div/div/section/div[1]/form/div[1]/div/div/div/input').click()

        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[2]/div/div[3]/div/div/section/div[1]/form/div[2]/div/div/input').send_keys(name)
        # 类型
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[2]/div/div[3]/div/div/section/div[1]/form/div[3]/div/div/div[1]/input').click()
        self.driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[1]/ul/li[1]/span').click()
        # 适用对象
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[2]/div/div[3]/div/div/section/div[1]/form/div[4]/div/div/div/input').click()
        self.driver.find_element_by_xpath('/html/body/div[7]/div[1]/div[1]/ul/li[1]').click()
        # 禁用
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[2]/div/div[3]/div/div/section/div[1]/form/div[5]/div/div/label[2]/span[1]/span').click()
        # 启用
        # self.driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[2]/div/div[3]/div/div/section/div[1]/form/div[5]/div/div/label[1]/span[1]/span').click()
        # 表达式
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[2]/div/div[3]/div/div/section/div[1]/form/div[6]/div/div/div[2]/div').click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_xpath('/html/body/div[7]/div/div[2]/div[2]/div[2]/div[2]/div/span[1]').click()
        self.driver.find_element_by_xpath('/html/body/div[7]/div/div[2]/div[3]').click()
        sleep(1)
        # 规则描述
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[2]/div/div[3]/div/div/section/div[1]/form/div[9]/div/div/input').send_keys('1')
        sleep(1)
        # 保存
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[2]/div/div[3]/div/div/section/div[2]/div/div[1]/div').click()

    #     查找指定规则页面
    def get_gz(self,name):
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/section/aside/div/div[13]/div').click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/section/aside/div/div[14]/div').click()

        self.driver.implicitly_wait(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[1]/ul/li[2]/div/a').click()
        # 搜索
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[2]/div/div[1]/div/div/input').send_keys(name)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[2]/div/div[1]/div/p').click()

    # 添加规则结果
    def add_gz_res(self,fenlei,name):
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/section/aside/div/div[13]/div').click()
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/section/aside/div/div[14]/div').click()
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div/div[1]/ul/li[2]/a').click()
        self.driver.implicitly_wait(1)
        # 新增结果
        self.driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div/div[2]/div[2]/div/div[1]/div[2]').click()
        self.driver.implicitly_wait(1)
        # 分类
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div/div[3]/div/div/section/div[1]/div[1]/form/div/div/div/input').send_keys(fenlei)
        self.driver.implicitly_wait(1)
        # 新增
        self.driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div/div[2]/div[2]/div/div[3]/div/div/section/div[1]/div[2]/span').click()
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div/div[2]/div[2]/div/div[3]/div/div/section/div[1]/div[3]/div[4]/div[2]/table/tbody/tr/td[1]/div/div/input').send_keys(name)
        sleep(1)
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div/div[2]/div[2]/div/div[3]/div/div/section/div[2]/div/div[1]/div').click()
        sleep(2)

    #     查找规则结果页面
    def get_gz_res(self,name):
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/section/aside/div/div[13]/div').click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/section/aside/div/div[14]/div').click()

        self.driver.implicitly_wait(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div/div[1]/ul/li[2]/a').click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/section/main/div/div[2]/div[1]/div/ul/li[2]/div/a').click()
        # 搜索
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div/div[1]/div/div/input').send_keys(name)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div/div[2]/div[2]/div/div[1]/div/p').click()

    # 测试未填写数据提交时是否有弹出框
    def test_alert(self):
        self.driver.find_element_by_xpath('/html/body/div[1]/div/section/aside/div/div[6]/div/img').click()
        self.driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div/div/div[2]/div[1]/div[2]').click()
        self.driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div/div/div[2]/div[5]/div/div/section/div[2]/div/div[1]/div').click()
        # 判断弹出框是否存在
        res=EC.alert_is_present()(self.driver)
        print(res)
        if res:
            print(res.text)
            res.accept()
        else:
            print('no alert')

    def quit(self):
        self.driver.quit()

if __name__ == '__main__':
    gz = Gz('1000294')
    for i in range(1,5):
        name='测试规则0819-'+str(i)
        gz.add_gz(name)
        name1='测试规则结果0819-'+str(i)
        gz.add_gz_res('测试分类',name1)
    # 添加完成后 查看某一规则页面
    gz.get_gz('测试规则0819-1')
    #退出
    # gz.quit()

