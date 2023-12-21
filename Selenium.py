from selenium import webdriver
from selenium.webdriver.common.keys import Keys

webdriver_path = '/path/to/your/webdriver'
driver = webdriver.Chrome(executable_path=webdriver_path)
driver.get("https://www.google.com")

# Find the search input element using its name attribute value
search_input = driver.find_element("name", "q")

# Input the search query (replace "Your search query" with your actual search query)
search_input.send_keys("Your search query")

# Press Enter to perform the search
search_input.send_keys(Keys.RETURN)

# Wait for a few seconds to see the results (you can use WebDriverWait for more precise waiting)
driver.implicitly_wait(5)

# Close the browser window
driver.quit()
