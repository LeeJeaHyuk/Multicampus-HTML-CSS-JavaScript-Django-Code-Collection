from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup

tag = input("serch tags : ")
url = f"https://www.instagram.com/explore/tags/{tag}"

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get(url)

sleep(5)

soup = BeautifulSoup(driver.page_source, "html.parser")
divs = soup.find_all("div", class_="_aagv")
print(divs)
for img in divs:
    print(img.find('img')['src'])

driver.close()