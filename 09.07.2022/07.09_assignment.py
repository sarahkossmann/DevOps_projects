from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chrome_driver = webdriver.Chrome("/Users/sarahkossmann/Desktop/chromedriver")

#
# 1. Write a script which will open the following:
# a. Chrome – http://www.walla.co.il
# b. Firefox – http://www.ynet.co.il

# firefox_driver = webdriver.Firefox(executable_path="/Users/sarahkossmann/Desktop/geckodriver")

# chrome_driver.get("https://www.google.com/")
# chrome_driver.quit()
# firefox_driver.get("http://www.ynet.co.il")
# firefox_driver.quit()

# 2. In one of the browsers you have open, do the following:
# a. Create a variable with the website’s title
# b. Refresh website
# c. Get website name and compare it to the variable you created in clause 1
# google_title_assert = 'עסקים'
# google_title_path = chrome_driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[2]/div[1]/a[3]').text
# chrome_driver.refresh()
# sleep(3)
# assert google_title_assert == google_title_path
# chrome_driver.quit()

# 3. Open a few browsers, locate any element, does the element has the same locator in
# the other browser?
# Yes
# 4. Create a test with the following:
# a. Open Google Translate web page
# b. Write anything in Hebrew in the text area
chrome_driver.get("")

# 5. Open Youtube web page
# a. Type a name of a song
# b. Click on search.
# 6. Open Chrome browser on Google Translate website: https://translate.google.com/
# a. Find translation text field (the one you send keys to) with 3 different locators and
# print the WebElement you created.
# 7. Open Chrome browser on Facebook website https://www.facebook.com/
# a. Login into Facebook (No need to send me credentials).