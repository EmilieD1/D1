from selenium import webdriver
from selenium.webdriver.common.keys import Keys

webdriver_path = '/path/to/your/webdriver'
driver = webdriver.Chrome(executable_path=webdriver_path)
driver.get("https://www.google.com")

# Find the search input element using its name attribute value
search_input = driver.find_element("name", "q")
search_input.send_keys("Your search query")
search_input.send_keys(Keys.RETURN)
driver.implicitly_wait(5)
driver.quit()
