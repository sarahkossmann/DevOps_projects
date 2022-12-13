import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome("/Users/sarahkossmann/Downloads/chromedriver")
        self.browser.get("http://127.0.0.1:5000/")
    def test1(self):
        browser = self.browser
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "total-score")))
        total_score_flask = browser.find_element(By.ID, 'total-score').text
        total_score_flask = total_score_flask.split(": ")
        score = total_score_flask[1]
        score = int(score)
        self.assertGreaterEqual(score, 0)
        self.assertLessEqual(score, 1000)

    def tearDown(self):
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()
