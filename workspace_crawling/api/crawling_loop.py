import requests
from bs4 import BeautifulSoup

url = "https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword=%EA%B5%90%EC%9C%A1&detailKeyword=&publicDataPk=&recmSe=N&detailText=&relatedKeyword=&commaNotInData=&commaAndData=&commaOrData=&must_not=&tabId=&dataSetCoreTf=&coreDataNm=&sort=_score&relRadio=&orgFullName=&orgFilter=&org=&orgSearch=&currentPage=1&perPage=10&brm=&instt=&svcType=&kwrdArray=&extsn=&coreDataNmArray=&pblonsipScopeCode="
resp = requests.get(url)
# print(resp.text)
soup =  BeautifulSoup(resp.text, "html.parser")
# print(soup)
paging = soup.find("nav", class_="pagination")
# print(paging)

"""
nums=list()
for page in paging:
    # print(page.text)
    if page.text.isdigit():
        # 숫자만 가져옮
        # print(page.text)
        nums.append(page.text)
"""

nums = list(filter(None, map(lambda x:x.text if x.text.isdigit() else None, paging  )))
# print(nums)

for i in nums:
    sub_url=f"https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword=%EA%B5%90%EC%9C%A1&currentPage={i}"
    # print(sub_url)
    sub_soup = BeautifulSoup(requests.get(sub_url).text, "html.parser")
    titles = sub_soup.select("span[class=title]")
    for title in titles:
        #.strip()
        print(title.text.strip())


