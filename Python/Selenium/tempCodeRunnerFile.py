from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import warnings
import time

warnings.filterwarnings("ignore", category=DeprecationWarning)
driver = webdriver.Edge(EdgeChromiumDriverManager().install())
driver.get("https://japanplacements.com/")

driver.maximize_window()

driver.find_element_by_link_text("Login").click()  # send_keys(Keys.RETURN)

driver.find_element_by_name('pt_user_login').send_keys('Ankrp')
driver.find_element_by_name('pt_user_pass').send_keys('!primeHP')

driver.find_element_by_class_name('jobsearch-login-submit-btn').click()


time.sleep(5)
driver.quit()