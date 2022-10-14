import requests
from bs4 import BeautifulSoup
import json


# 웹툰의 이름과 평점 가져오기
url = "https://comic.naver.com/webtoon/weekdayList?week=fri"
resp = requests.get(url)
# print(resp)
# print(resp.text)
soup = BeautifulSoup(resp.text, "html.parser")
# print(soup)

# [별점] 제목
img_list = soup.find("ul", {"class":"img_list"})
# img_list는 1개
# select에 css선택자
# select one

webtoon_list = list()
webtoons = img_list.select("dl")
for webtoon in webtoons:
    # 가장 먼저 있는 a태그를 가져옴
    # a태그가 여러개 있으면 findall사용
    title = webtoon.find("a")['title']
    star = webtoon.find('strong').text
    # print(f'{title} [{star}]')

    # json파일로 변환
    tmp = dict()
    tmp['title'] = title
    tmp['star'] = star

    webtoon_list.append(tmp)
# 배열 형태
# print(webtoon_list)
# json형태로
res = dict()
res['webtoons'] = webtoon_list
# value가 array형태인 object,...,object형태
# print(res)

res_json = json.dumps(res, ensure_ascii=False)
# print(res_json)
# ""로 뜨면 json객체임을 확인 가능

with open("webtoons.json", "w", encoding="utf-8") as f:
    f.write(res_json)
