from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_driver = webdriver.Chrome("/Users/sarahkossmann/Desktop/chromedriver", options=chrome_options)

def find_elem(by, element):
    chrome_driver.find_element(by, element)

def send_text(by, element, text):
    chrome_driver.find_element(by, element).send_keys(text)

def click_on_elem(by, element):
    chrome_driver.find_element(by, element).click()


chrome_driver.get("https://www.youtube.com/")

WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located((By.ID, 'search-input')))
click_on_elem(By.NAME, 'search_query')
send_text(By.NAME, 'search_query', "happy birthday to you")
send_text(By.NAME, 'search_query', Keys.RETURN)
chrome_driver.quit()
