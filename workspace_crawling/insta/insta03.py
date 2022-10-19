from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


input_id = input('id 입력 :')
input_pw = input('pw 입력 :')

service = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get("https://www.instagram.com/")

# 아이디 비밀번호 만드는 창이 바로 만들어지지 않으므로 sleep을 주어서 조금 이따 id를 입력하도록 한다
sleep(3)

id = driver.find_element(By.NAME, 'username')
id.send_keys(input_id)

pw = driver.find_element(By.NAME, 'password')
pw.send_keys(input_pw)

#loginForm클래스의 자식요소의 자식요소를
sleep(3)
# driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(3)").click()
driver.find_element(By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]").click()
