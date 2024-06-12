from selenium import webdriver
import requests
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import requests
driver = webdriver.Chrome()

driver.maximize_window()
driver.get('https://www.instagram.com')
sleep(2)
username="__iwritesometimes__"
password="hi"

# Login to the instagram page 
driver.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input").send_keys(username)


driver.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input").send_keys(password)

driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button").click()
driver.implicitly_wait(10)
sleep(3)
print(driver.current_url)
# driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button").click()
# driver.implicitly_wait(10)
# 
# driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
# driver.implicitly_wait(10)



# driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[2]/a").click()
# driver.implicitly_wait(10)



# driver.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[3]/a").click()
# driver.implicitly_wait(10)

# priyank="8/10 nahi 10/10 ho aap! ❤️❤️"

# button=driver.find_element_by_xpath("///*[@id=react-root']/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]")

# button.send_keys(priyank)
# driver.implicitly_wait(10)

# button.send_keys(Keys.RETURN)
