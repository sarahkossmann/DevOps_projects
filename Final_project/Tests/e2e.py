import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# opts = Options()
# opts.add_experimental_option("detach", False)
chrome_driver = webdriver.Chrome("/Users/sarahkossmann/Downloads/chromedriver")

def test_scores_service():
    chrome_driver.get("http://127.0.0.1:5000/")
    WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located((By.ID, "total-score")))
    total_score_flask = chrome_driver.find_element(By.ID, 'total-score').text
    total_score_flask = total_score_flask.split(": ")
    score = total_score_flask[1]
    score = int(score)
    if score in range(0, 1000):
        return True
    else:
        return False

def main_function():
    test_scores_service()
    if test_scores_service():
        exit(0)
    else:
        exit(1)

def tear_down():
    chrome_driver.quit()

main_function()

