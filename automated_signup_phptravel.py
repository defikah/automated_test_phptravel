from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.phptravels.net/home")
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/header/div[1]/div/div/div[2]/div/ul/li[3]/div/a").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/header/div[1]/div/div/div[2]/div/ul/li[3]/div/div/div/a[2]").click()
time.sleep(2)
driver.find_element_by_name("firstname").send_keys("Marry")
time.sleep(1)
driver.find_element_by_name("lastname").send_keys("Oliv")
time.sleep(1)
driver.find_element_by_name("phone").send_keys("1123461")
time.sleep(1)
driver.find_element_by_name("email").send_keys("@gmail.com")
time.sleep(1)
driver.find_element_by_name("password").send_keys("pass")
time.sleep(1)
driver.find_element_by_name("confirmpassword").send_keys("pass")
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div[1]/section/div/div/div[2]/div/form/div[8]/button").click()
time.sleep(5)
driver.close()
print ("success running robot program")
