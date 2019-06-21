from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

delay = 5

capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"

driver = webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")#, desired_capabilities=capa)
# wait = WebDriverWait(driver, delay)
driver.get("https://buyme.co.il/")

try:
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#app-loading-img > div > div.bounce1')))
    driver.execute_script("window.stop();")
    print(driver.find_element_by_xpath('//*[@id="app-loading-img"]/div').size)
    print(driver.find_element_by_xpath('//*[@id="app-loading-img"]/div/div[1]').size)
    driver.quit()
except ValueError as err:
    print('the site is not good ' + str(err))
finally:
    driver.quit()