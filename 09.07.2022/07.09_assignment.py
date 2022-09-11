from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_driver = webdriver.Chrome("/Users/sarahkossmann/Desktop/chromedriver")

def find_elem(by, element):
    chrome_driver.find_element(by, element)

def send_text(by, element, text):
    chrome_driver.find_element(by, element).send_keys(text)

def click_on_elem(by, element):
    chrome_driver.find_element(by, element).click()

# 1. Write a script which will open the following:
# a. Chrome – http://www.walla.co.il
# b. Firefox – http://www.ynet.co.il
firefox_driver = webdriver.Firefox(executable_path="/Users/sarahkossmann/Desktop/geckodriver")

chrome_driver.get("http://www.walla.co.il")
chrome_driver.quit()
firefox_driver.get("http://www.ynet.co.il")
firefox_driver.quit()

# 2. In one of the browsers you have open, do the following:
# a. Create a variable with the website’s title
# b. Refresh website
# c. Get website name and compare it to the variable you created in clause 1
chrome_driver.get("https://www.google.com/")
google_title_assert = 'עסקים'
google_title_path = chrome_driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[2]/div[1]/a[3]').text
chrome_driver.refresh()
sleep(3)
assert google_title_assert == google_title_path
chrome_driver.quit()

# 3. Open a few browsers, locate any element, does the element has the same locator in
# the other browser?
# Yes
# 4. Create a test with the following:
# a. Open Google Translate web page
# b. Write anything in Hebrew in the text area
chrome_driver.get("https://translate.google.com/?hl=iw&tab=TT")
send_text(By.CLASS_NAME, "er8xn", "שלום")
chrome_driver.quit()

# 5. Open Youtube web page
# a. Type a name of a song
# b. Click on search.
chrome_driver.get("https://www.youtube.com/")

WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located((By.ID, 'search-input')))
click_on_elem(By.NAME, 'search_query')
send_text(By.NAME, 'search_query', "happy birthday to you")
send_text(By.NAME, 'search_query', Keys.RETURN)
chrome_driver.quit()

# 6. Open Chrome browser on Google Translate website: https://translate.google.com/
# a. Find translation text field (the one you send keys to) with 3 different locators and
# print the WebElement you created.
chrome_driver.get("https://translate.google.com/")
find_elem(By.CLASS_NAME, "er8xn")
print("this is class name")
find_elem(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea')
print("this is xpath")
find_elem(By.XPATH, "//textarea[@aria-label='Source text']")
print("this is xpath 2")
chrome_driver.quit()

# 7. Open Chrome browser on Facebook website https://www.facebook.com/
# a. Login into Facebook (No need to send me credentials).
chrome_driver.get("https://www.facebook.com/")
find_elem(By.ID, "email")
send_text(By.ID, "email", "devops_course@selenium_test.il")
click_on_elem(By.ID, "pass")
send_text(By.ID, "pass", "apassword")
click_on_elem(By.NAME, "login")
chrome_driver.quit()

# 8. Open Chrome browser on any webpage:
# a. Delete all cookies from browser.
# b. Make sure all cookies are deleted by printing all cookies stored in the browser.
chrome_driver.get("https://www.youtube.com/")

before_deletion = chrome_driver.get_cookies()
chrome_driver.delete_all_cookies()
after_deletion = chrome_driver.get_cookies()

if before_deletion == after_deletion:
    print("Cookies not deleted")
else:
    print("Cookies deleted")
cookie_names = ""
for cookie in before_deletion:
    cookie_names += cookie['name']+', '
cookie_names = cookie_names[:-2]
print(f"{cookie_names} have been deleted")

chrome_driver.quit()

# 9. Open any browser on "Github" website https://github.com/
# a. Enter “Selenium” keyword in search textfield
# b. Press Enter to search (through code - of course).
chrome_driver.get("https://github.com/")
send_text(By.XPATH, "//input[@data-test-selector='nav-search-input']", "selenium")
send_text(By.XPATH, "//input[@data-test-selector='nav-search-input']", Keys.RETURN)

# 10.Find a way to disable all extensions in
# a. Chrome
# b. Firefox
# c. Explorer.
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_driver_2 = webdriver.Chrome("/Users/sarahkossmann/Desktop/chromedriver", options=chrome_options)
chrome_driver_2.get("https://www.google.com/")
chrome_driver_2.quit()