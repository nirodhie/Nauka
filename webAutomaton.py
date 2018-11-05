# najpierw trzeba ściągnąc program pomocniczy z http://chromedriver.chromium.org/downloads
import time
from selenium import webdriver
import os

os.environ.update({"__COMPAT_LAYER": "RUnAsInvoker"}) #pomija UAC !!!
driver = webdriver.Ie(r".\browserDrivers\IEDriverServer.exe")  # Optional argument, if not specified will search path.
driver.maximize_window()
driver.get('https://mystatus.hemmersbach.com/index.php?token=A9yb4Rf5gN8zDMKOGh17AhfQhu6HGoYFckGb9NM2')
#time.sleep(1) # Let the user actually see something!
'''
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
'''

submitButton = driver.find_element_by_id('sumbit-login')
submitButton.submit() # submit bo przycisk jest czescia wiekszej form
time.sleep(1)
driver.quit()