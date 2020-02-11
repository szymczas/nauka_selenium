from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///C:/Users/szymon.hubicki/Desktop/selenium/Test.html")
driver.maximize_window()

username_imput = driver.find_element_by_name("username")
username_imput.clear()
username_imput.send_keys("PonuryAdam")