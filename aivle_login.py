from time import sleep
import conf
import os
import execute_util as exe
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def run():
    exe.execute(conf.run_cmd, conf.chrome_path)

    opt = Options()
    opt.add_experimental_option('debuggerAddress', '127.0.0.1:9222')
    driver = webdriver.Chrome(conf.chromedriver_path, options=opt)
    driver.implicitly_wait(5)

    driver.get(conf.url_aivle)

    element_id = driver.find_element(By.CSS_SELECTOR, conf.id_path)
    element_id.clear()
    element_id.send_keys(conf.id)

    element_pw = driver.find_element(By.CSS_SELECTOR, conf.pw_path)
    element_pw.clear()
    element_pw.send_keys(conf.pw)

    element_btn = driver.find_element(By.CSS_SELECTOR, conf.btn_path)
    element_btn.click()

    sleep(1.5)
    driver.switch_to.alert.accept()
    driver.switch_to.default_content()

    element_otp = driver.find_element(By.CSS_SELECTOR, conf.otp_path)
    element_otp.click()
