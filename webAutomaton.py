# najpierw trzeba ściągnąc program pomocniczy z http://chromedriver.chromium.org/downloads
import time
from selenium import webdriver

driver = webdriver.Chrome(r".\browserDrivers\chromedriver.exe")  # Optional argument, if not specified will search path.
driver.get('http://www.google.com')
time.sleep(1) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('python automation is fun')
search_box.submit()
time.sleep(5) # Let the user actually see something!
#driver.quit()
