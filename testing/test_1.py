from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import asyncio

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support.ui import Select
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"  #  interactive

driver = webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe",options=chrome_options)
driver.implicitly_wait(5)

driver.get("https://buyme.co.il/") 


# element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "app-loading-img"))
sel = driver.find_elements_by_id("app-loading-img")
print(sel)

item = driver.find_elements_by_partial_link_text("סעדות שף")
item[0].click()

item = driver.find_elements_by_partial_link_text("בוצת מחניודה")
item[0].click()


# print(sel)
# sel = driver.find_element_by_partial_link_text("סכום")
# sel.click() 

# sel = driver.find_element_by_xpath("//li[@data-option-array-index='2']")
# sel.click() 

# driver.get("https://buyme.co.il/supplier/20620")
# elem = driver.find_elements_by_class_name("input-cash")
# elem[0].send_keys("100")
# btn = driver.find_element_by_xpath("//button[text()='לבחירה']")
# btn.click()


print(driver.title)
      
         
