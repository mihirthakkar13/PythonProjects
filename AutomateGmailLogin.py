from selenium import webdriver

import time

from selenium.webdriver.common.keys import Keys


#open google chrome browser

driver = webdriver.Chrome()

# maximize the window size

driver.maximize_window()

#delete cookies

driver.delete_all_cookies()

# navigate to url

driver.get("https://www.gmail.com")

# identify the user name text box and enter the value

driver.find_element("identifierId").send_keys("mihirthakkar1113@gmail.com")

time.sleep(2)

#click on the next button

driver.find_element('//*[@id=".identifyifierNext"]/div/button/div [2 ]').click()

time.sleep(3)

#identify the password checkbox and enter value

driver.find_element("password").send_keys("M!hir1113")
time.sleep(3)

#click on the next button

driver.find_element('//*[@id="passwordNext"]/div/button/div [2] ').click()
time.sleep(3)

# close the browser

driver.close()

print("gmail login successfull")