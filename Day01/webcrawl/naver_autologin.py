from selenium import webdriver
from bs4 import BeautifulSoup

ctx = '../crawler/chromedriver'
driver = webdriver.Chrome(ctx)
driver.implicitly.wait(3)
driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')
driver.find_elenemt_by_name('id').send.keys('holywood')
driver.find_elenemt_by_name('pw').send.keys('1234')
driver.implicitly_wait(3)
driver.find_elenemt_by_xpath('//*[@id="frmNIDLogin"]/fieldest/input').click()
driver.implicitly_wait(3)
