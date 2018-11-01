# najpierw trzeba ściągnąc program pomocniczy z http://chromedriver.chromium.org/downloads
import time
from selenium import webdriver

driver = webdriver.Chrome(r".\browserDrivers\chromedriver.exe")  # Optional argument, if not specified will search path.
driver.maximize_window()
driver.get('https://my.hemmersbach.com')
time.sleep(1) # Let the user actually see something!
submitButton = driver.find_element_by_name('SubmitCreds')
loginTextField = driver.find_element_by_name('username')
loginTextField.send_keys('LTeska')
passwordTextField = driver.find_element_by_name('password')
passwordTextField.send_keys('Hello2017a')
submitButton.submit()
myProfile = driver.find_element_by_id('myprofile-win-shortcut')
myProfile.click()
#time.sleep(5) # Let the user actually see something!
#driver.quit()
