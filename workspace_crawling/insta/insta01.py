import requests
from bs4 import BeautifulSoup

tag = input("serch tags : ")
url = f"https://www.instagram.com/explore/tags/{tag}"
soup = BeautifulSoup(requests.get(url).text, "html.parser")

print(soup)

# divs = soup.find("div", class_="_aagv")
# print(divs)