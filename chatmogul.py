import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait 


path = "C:/Program Files (x86)/chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(path, options=options)
driver.get("https://thechatmogul.com/chatmogul-login/")

username = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='log']")))
password = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pwd']")))

username.clear()
password.clear()

username.send_keys("emmyonwukwe2021")
password.send_keys("09121061435")


driver.find_element_by_xpath("//input[@value='forever']").click()

login_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='Submit']"))).click()

driver.get("https://thechatmogul.com/category/general/")

driver.find_element_by_link_text("Top 6 Popular Foreign Exchange Currencies In Nigeria").click()


WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "You can also read about"))).click()
time.sleep(30)
driver.switch_to.window(driver.window_handles[1])

WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "You can also read about"))).click()
time.sleep(30)
driver.switch_to.window(driver.window_handles[2])

WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "You can also read about"))).click()
time.sleep(30)
driver.switch_to.window(driver.window_handles[3])

WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "You can also read about"))).click()
time.sleep(30)
driver.switch_to.window(driver.window_handles[4])

WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "You can also read about"))).click()
time.sleep(30)
driver.switch_to.window(driver.window_handles[5])

WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "You can also read about"))).click()
time.sleep(30)
driver.switch_to.window(driver.window_handles[6])

WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "You can also read about"))).click()
time.sleep(30)
driver.switch_to.window(driver.window_handles[7])

WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "You can also read about"))).click()
time.sleep(30)
driver.switch_to.window(driver.window_handles[8])

WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "You can also read about"))).click()
time.sleep(30)
driver.switch_to.window(driver.window_handles[9])

WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "You can also read about"))).click()
time.sleep(30)
driver.switch_to.window(driver.window_handles[10])

