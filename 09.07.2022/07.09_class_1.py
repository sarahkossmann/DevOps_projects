from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome("/Users/sarahkossmann/Desktop/chromedriver")

driver.get("file:/Users/sarahkossmann/PycharmProjects/Devops_projects/09.07.2022/tip_calc/index.html")
driver.find_element(By.ID, "billamt").send_keys("100")
driver.find_element(By.ID, "serviceQual").click()
sleep(3)
driver.find_element(By.ID, "good").click()
driver.find_element(By.ID, 'peopleamt').send_keys("4")
driver.find_element(By.ID, 'calculate').click()
tip = driver.find_element(By.ID, 'tip').text
assert tip == "5.00"
driver.close()