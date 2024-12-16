from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.google.com") 
driver.find_element(By.CSS_SELECTOR, "div.class-name[data-test-id='value']")
driver.find_element(By.CSS_SELECTOR, "[data-test-id='unique-value']")
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://example.com")

# Locate element by ID
element_by_id = driver.find_element(By.ID, "unique-id")

# Locate element by CSS Selector
element_by_css = driver.find_element(By.CSS_SELECTOR, "div.class-name[data-test-id='value']")

# Locate element by XPath
element_by_xpath = driver.find_element(By.XPATH, "//div[@data-test-id='value']")

# Locate element by Link Text
element_by_link_text = driver.find_element(By.LINK_TEXT, "Click Here")
