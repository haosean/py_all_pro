# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from time import sleep
import sys
from conf import equipment_para, base_url
reload(sys)
sys.setdefaultencoding("utf-8")


def addterminal(
        click_classroom, equipment_name, equipmentModel, ipAddr, locAddr, equipmentLogName, equipmentLogPwd):
    driver = webdriver.Chrome()
    driver.implicitly_wait(40)
    driver.get(base_url + "/middleclient/index.do")
    Select(driver.find_element_by_id("platform")).select_by_visible_text(
        u"河南教育局")
    # Select(driver.find_element_by_id("platform")).select_by_visible_text(
    #     u"河南教育局哦")
    driver.find_element_by_id('s_username').clear()
    driver.find_element_by_id('s_username').send_keys('hnsadmin')
    driver.find_element_by_id('s_password').clear()
    driver.find_element_by_id('s_password').send_keys('111111')
    driver.find_element_by_name('submit').click()
    driver.maximize_window()

    driver.find_element_by_css_selector(
        "#div_menu > ul.nav.nav-list > li > a.dropdown-toggle > span.menu-text").click()
    driver.find_element_by_link_text(u"学校管理").click()
    driver.find_element_by_link_text(u"教室列表").click()
    driver.find_element_by_link_text(click_classroom).click()
    driver.find_element_by_xpath(u"//a[contains(text(),'设备管理')]").click()
    sleep(1)
    driver.find_element_by_id("addterminal").click()
    sleep(1)
    driver.find_element_by_css_selector(
        "div.modal-body > div > #name > div.col-sm-9 > input.form-control").clear()
    driver.find_element_by_css_selector(
        "div.modal-body > div > #name > div.col-sm-9 > input.form-control").send_keys(equipment_name)
    Select(driver.find_element_by_css_selector(
        "div.modal-body > div > #equipmentModel > div.col-sm-9 > select")).select_by_visible_text(equipmentModel)
    driver.find_element_by_css_selector(
        "div.modal-body > div > #ipAddr > div.col-sm-9 > input.form-control").clear()
    driver.find_element_by_css_selector(
        "div.modal-body > div > #ipAddr > div.col-sm-9 > input.form-control").send_keys(ipAddr)
    driver.find_element_by_css_selector(
        "div.modal-body > div > #locAddr > div.col-sm-9 > input.form-control").clear()
    driver.find_element_by_css_selector(
        "div.modal-body > div > #locAddr > div.col-sm-9 > input.form-control").send_keys(locAddr)
    driver.find_element_by_css_selector(
        "div.modal-body > div > #equipmentLogName > div.col-sm-9 > input.form-control").clear()
    driver.find_element_by_css_selector(
        "div.modal-body > div > #equipmentLogName > div.col-sm-9 > input.form-control").send_keys(equipmentLogName)
    driver.find_element_by_css_selector(
        "div.modal-body > div > #equipmentLogPwd > div.col-sm-9 > input.form-control").clear()
    driver.find_element_by_css_selector(
        "div.modal-body > div > #equipmentLogPwd > div.col-sm-9 > input.form-control").send_keys(equipmentLogPwd)
    driver.find_element_by_css_selector(
        "#terminal > div.modal-dialog > div.modal-content > #formrole > div.modal-body > div.text-center > #submit").click()
    # driver.find_element_by_xpath("(//input[@name='isgk'])[2]").click()
    sleep(3)
    driver.quit()

if __name__ == '__main__':
    for each_terminal in equipment_para:
        addterminal(each_terminal['click_classroom'],
                    each_terminal['equipment_name'],
                    each_terminal['equipmentModel'],
                    each_terminal['ipAddr'],
                    each_terminal['locAddr'],
                    each_terminal['equipmentLogName'],
                    each_terminal['equipmentLogPwd'])
        print "add >>", each_terminal['click_classroom'], "<< OK!"
