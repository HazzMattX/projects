import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# driver setup
driver = webdriver.Firefox()
driver.get("https://orteil.dashnet.org/cookieclicker/")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "langSelect-EN"))
    )
    element.click()
finally:
    baking = True
    while baking:
        # Locate and click the cookie
        wait = WebDriverWait(driver, 10)
        cookie = wait.until(EC.element_to_be_clickable((By.ID, "bigCookie")))
        cookie.click()