from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')

driver = webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe",options=chrome_options)
driver.get("file:///C:/Users/hadas/Python/First%20Lesson/html/1%20(3).html")
# txts = driver.find_elements_by_tag_name("input")
# txts = [txt for txt in txts if txt.location["x"] > 0]
# txts = [item for item in txts if item.location["x"] > 0 and item.size["width"]>200]
# txt = driver.find_elements_by_xpath("//input[@title='חיפוש' or @title='search']")
txt = driver.find_elements_by_xpath("//input[@type='color']")
txt[0].send_keys("search text.")
txt[0].send_keys(Keys.ENTER)

driver.implicitly_wait(20) 
txt = driver.find_elements_by_xpath("//input[@title='hgjgh' or @title='ghjghjg']")
    
        
         
