import requests
import json

def getSiDo():
    url="https://www.starbucks.co.kr/store/getSidoList.do"
    resp = requests.post(url)

    # .json()으로 불러도 dict 타입으로 들어온다
    # print(type(resp.json()))

    sido_json = resp.json()['list']
    # print(sido_json[1].keys())
    sido_cd = list(map(lambda x: x['sido_cd'], sido_json))
    sido_nm = list(map(lambda x: x['sido_nm'], sido_json))
    # print(sido_cd)
    # print(sido_nm)
    sido_dict = dict(zip(sido_cd, sido_nm))
    return (sido_dict)


def getGugun(sido_cd):
    # sido_cd : 값을 전달
    # gugun_cd: "0101", gugun_nm: "강남구"
    url = "https://www.starbucks.co.kr/store/getGugunList.do"
    resp = requests.post(url, data={"sido_cd": sido_cd})
    # print(resp.text)

    gugun_json=resp.json()['list']
    gugun_dict=dict(zip(list(map(lambda x:x['gugun_cd'], gugun_json)), list(map(lambda x:x['gugun_nm'],gugun_json))))
    return(gugun_dict)

def getStore(sido_cd="", gugun_cd=""):
    url = "https://www.starbucks.co.kr/store/getStore.do"
    resp = requests.post(url, data={"ins_lat":"37.5128064",
                                    "ins_lng":"127.5128064",
                                    "p_sido_cd": sido_cd,
                                    "p_gugun_cd": gugun_cd,
                                    "in_biz_cd": "",
                                    "set_date":""})
    print(resp.text)


    store_json =resp.json()['list']

    store_list = list()
    for store in store_json:
        store_dict = dict()
        store_dict['s_name'] = store['s_name']
        store_dict['doro_address'] = store['doro_address']
        store_dict['lat'] = store['lat']
        store_dict['lot'] = store['lot']

        store_list.append(store_dict)

    # result = dict()
    # result['store_list']=store_list
    # return result
    return store_list

if __name__ == '__main__':

    # 전국 매장 요청
    list_all = list()

    sido_all = getSiDo()
    for sido in sido_all:
        # 구군코드를 가져오지 않고 서울시 전체를 가져와서 더 간단하게 할 수 있음
        if sido == '17':
            result = getStore(sido_cd=sido)
            print(result)
            list_all.extend(result)
        else:
            gugun_all = getGugun(sido)
            for gugun in gugun_all:
                result = getStore(gugun_cd=gugun)
                print(result)
                list_all.extend(result)

    # print(len(list_all))

    #json으로 만들기
        # dict로 만들기
    result_dict = dict()
    result_dict['list'] = list_all

        #json으로 만들기
    result_json = json.dumps(result_dict, ensure_ascii=False)

    with open('starbucks.json','w',encoding='utf-8')as file:
        file.write(result_json)






    # getSiDo()
    # sido = input("도시 코드를 입력해 주세요 : ")
    # # print(getGugun(sido))
    # #세종시는 구군이 없어 바로 검색한다.
    # if sido =='17':
    #     print(getStore(sido_cd=sido))
    # else:
    #     print(getStore(sido))
    #     gugun = input("구군 코드를 입력해 주세요 :")
    #     print(getStore(sido_cd=sido, gugun_cd=gugun))

