from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///C:/Users/szymon.hubicki/Desktop/selenium/Test.html")
driver.maximize_window()
driver.find_element_by_id('newPage').click()
print(driver.title)
current_window_name = driver.current_window_handle
window_names = driver.window_handles

for window in window_names:
    if window != current_window_name:
        driver.switch_to.window(window)

print(driver.title)

driver.switch_to.window(current_window_name)
print(driver.title)





# driver.find_element_by_id("clickOnMe").click()
# driver.switch_to.alert.accept()
# driver.find_element_by_id("clickOnMe").click()
# driver.switch_to.alert.dismiss()
# driver.find_element_by_id("fname").send_keys("Bartek")
# print("Element text " + driver.find_element_by_id("fname").get_attribute("value"))
# #driver.find_element_by_name("password").send_keys(Keys.ENTER)
# auto_select = Select(driver.find_element_by_tag_name("select"))
# auto_select.select_by_visible_text("Volvo")
# auto_select.select_by_value("saab")
# auto_select.select_by_index(0)
# driver.find_element_by_xpath("//input[@type='checkbox']").click()
# driver.find_element_by_xpath("//input[@value='male']").click()
# print(driver.find_element_by_tag_name("h1").text)
# print(driver.find_element_by_id("clickOnMe").text)
# print(driver.find_element_by_tag_name("p").get_attribute('textContent'))
#
# print(driver.find_element_by_id("smileImage").size.get("height"))
# print(driver.find_element_by_id("smileImage").get_attribute("naturalHeight"))


#driver.quit()
