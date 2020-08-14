# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 18:30:16 2020

@author: noelp
"""


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = "http://url.com/"
driver = webdriver.Chrome()
#driver.minimize_window()
driver.get(url)

### log in
u = driver.find_element_by_name('username') ### you can also find element by xpath
u.send_keys('your username')
p = driver.find_element_by_name('Password')
p.send_keys('xxxxxxxx')
p.send_keys(Keys.RETURN)

##wait until it loads
driver.implicitly_wait(10)

##click a buttom
driver.find_element_by_xpath('xpath').click()

### fill form
new_bill_paths = {'Name': 'xpath_name', 'Age': 'xpath_age'}

data = {'Name': 'Vera', 'Age': '33'}

for k in new_bill_paths.keys():
    l = driver.find_element_by_xpath(new_bill_paths[k])
    l.send_keys(data[k])
    
### add attachements
k = driver.find_element_by_name('#fuUploader')
k.send_keys("path_to_file/filename.pdf")
driver.find_element_by_id("submit").click()
