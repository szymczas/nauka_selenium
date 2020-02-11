from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///C:/Users/szymon.hubicki/Desktop/selenium/Test.html")
driver.maximize_window()
driver.execute_script("arguments[0].click();",driver.find_element_by_id("newPage"))

wartosc = 'Bartek'
driver.execute_script("arguments[0].setAttribute('value', '"+ wartosc +"')",driver.find_element_by_id("fname"))

#mi to nie działa
