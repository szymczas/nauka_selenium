from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///C:/Users/szymon.hubicki/Desktop/selenium/FileUpload.html")
driver.maximize_window()

upload_input = driver.find_element_by_id("myFile")
path = os.path.abspath("upload.txt")

driver.save_screenshot("screenshots/before_upload.png")
upload_input.send_keys(path)
driver.save_screenshot("screenshots/after_upload.png")

