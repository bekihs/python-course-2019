from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\chromedriver_win32\chromedriver.exe")
driver.get("file:///C:/Users/hadas/Python/First%20Lesson/html/1%20(3).html")  
txts = driver.find_elements_by_tag_name("input")


for txt in txts:
    print(txt.get_attribute("type"))
txts = [txt for txt in txts if txt.get_attribute("type") == "text"]
txtUserName = txts[0]
txtUserName.send_keys("user name")
print(txts)
