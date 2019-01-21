from selenium import webdriver
import time
Ch_driver = webdriver.Chrome()
Ch_driver.get("https://www.baidu.com")
time.sleep(5)           
print("网站的名称：",Ch_driver.title)      
for line in open("keyword.txt").readlines():  
  Ch_driver.find_element('id','kw').send_keys(line)  
    Ch_driver.find_element('id','su').click()  
    time.sleep(5)  
    Ch_driver.find_element('id','kw').clear()  



