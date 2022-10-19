import requests
from xml.etree import ElementTree
import re


def today():
    service_key="wlDJ%2F9iedzCniA3yJopx238L05ZHBtuK%2BTGcIaXOLYn4aJzq48Yqih%2FoSmwykMmUZX204XOAdWd79FbkhilJWQ%3D%3D"
    url = f"http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?ServiceKey={service_key}"
    resp = requests.get(url)
    # print(resp.text)
    tree = ElementTree.fromstring(resp.text)
    '''
    xml.etree.ElementTree.fromstring(text, parser=None)
    Parses an XML section from a string constant. Same as XML(). 
    text is a string containing XML data. 
    parser is an optional parser instance. 
    If not given, the standard XMLParser parser is used. 
    **Returns an Element instance.**
    '''
    print(tree)
    print(tree.tag) # 엘리먼트 객체의 태그를 가져옴
    print(tree[0])
    print(tree[1])
    print(tree[1][0])
    print(tree[1][3].tag)
    print(tree[1][3].text)
    # http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?ServiceKey=wlDJ%2F9iedzCniA3yJopx238L05ZHBtuK%2BTGcIaXOLYn4aJzq48Yqih%2FoSmwykMmUZX204XOAdWd79FbkhilJWQ%3D%3D

    for items in tree [1][0]:
        if items.find('gubun').text =='합계':
            #gubun의 텍스트가 합계인 tree를에서 텍스트 가져오기
            incDec = items.find('incDec').text
            localOccCnt = items.find('localOccCnt').text
            overFlowCnt = items.find('overFlowCnt').text
            print(f"items.find('stdDay').text={items.find('stdDay').text}")
            stdDay = re.sub(r'(\D)+', '', items.find('stdDay').text)[2:8]
            # 숫자가 아닌 애들을 찾아서 공백으로 바꾸기
            print(stdDay)
            stdDay = stdDay[:2] + "/" + stdDay[2:4] + "/" + stdDay[4:]
            print(f'[{stdDay}]\n일일합계:{incDec}\n국내발생:{localOccCnt}\n해외발생:{overFlowCnt}')



if __name__ == '__main__':
    today()