from selenium import webdriver
from selenium.webdriver.common.by import By
import time

if __name__ == "__main__":
    
    n = input('How many times do you have to click?')

    driver = webdriver.Chrome(r"./chromedriver")
    #driver = webdriver.Edge(r"./msedgedriver") for MS Edge.
    #For Mozilla Firefox, check the documentation and also download the specific web driver for it. Chrome or Edge web drivers won't work for it.
    
    driver.get('https://shopmrbeast.com/slap-to-win')
    value = driver.find_element(By.CLASS_NAME,'slapper_normalImg__rE0TX')
    
    for i in range(int(n)):
        value.click()

    time.sleep(10)
    #driver.quit()
