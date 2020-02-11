from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///C:/Users/szymon.hubicki/Desktop/selenium/DoubleClick.html")
driver.maximize_window()

button = driver.find_element_by_id("bottom")
#webdriver.ActionChains(driver).double_click(button.)perform()

webdriver.ActionChains(driver).context_click(button).perform()
