from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\\Users\\satven\\chromedriver\\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://tinder.com/")
sleep(3)
login_button = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span")
login_button.click()

sleep(3)
try:
    login_with_fb = driver.find_element(By.XPATH, '//*[@id="q36386411"]/div/div/div[1]/div/div[3]/span/div[2]/button')
    login_with_fb.click()

except:
    driver.find_element(By.XPATH, '//*[@id="q36386411"]/div/div/div[1]/div/div[3]/span/button').click()
    sleep(2)
    login_with_fb = driver.find_element(By.XPATH,'//*[@id="q36386411"]/div/div/div[1]/div/div[3]/span/div[2]/button')
    login_with_fb.click()

base_window = driver.window_handles[0]
login_fb_window = driver.window_handles[1]
driver.switch_to.window(login_fb_window)

sleep(3)
driver.find_element(By.ID,"email").send_keys("kishorekumar007@hotmail.com")
driver.find_element(By.ID,"pass").send_keys("32017648")
driver.find_element(By.XPATH,'/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]/input').click()
driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div/div/div[1]/div[3]/div[2]/div[1]/div/div/div/div[1]/div/span/span').click()