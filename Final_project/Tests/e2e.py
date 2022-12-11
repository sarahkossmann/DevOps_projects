from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_driver = webdriver.Chrome("/Users/sarahkossmann/Downloads/chromedriver")

chrome_driver.get("http://127.0.0.1:5000/")

total_score = chrome_driver.find_element(By.ID, 'total-score').text
