from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Define XPATH constants
EDIT_POST="/html/body/article/section/div[1]/table/tbody/tr[2]/td[1]/div/form/input[3]"
PRICE_FIELD="/html/body/article/section/form[1]/div/div[2]/label[2]/input"
CONTINUE_BUTTON="/html/body/article/section/form[1]/div/button"
PUBLISH_BUTTON="/html/body/article/section/div[1]/form/button"

driver = webdriver.Firefox()
driver.get("https://post.craigslist.org/INSERT_POST_ID_FROM_CRAIGSLIST_EMAIL")

# Click "Edit this Posting"
edit_post = driver.find_element_by_xpath(EDIT_POST)
edit_post.click()

# Capture the price field contents
# Clear original price and set new price
price_field = driver.find_element_by_xpath(PRICE_FIELD)
driver.find_element_by_xpath(PRICE_FIELD).clear()
price_field.send_keys("30")

# Continue to the "Publish" page
continue_button = driver.find_element_by_xpath(CONTINUE_BUTTON)
continue_button.click()

# Publish the update
publish_button = driver.find_element_by_xpath(PUBLISH_BUTTON)
publish_button.click()

driver.close()
