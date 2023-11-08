import requests # poetry add requests -> 서버에 요청을 보낼 수 있도록 도와주는 library
import json

def dust_level(data):
    word = ""
    if 0<= data < 10: word="매우 좋음"
    elif 10<= data < 20: word="나쁨"
    elif 20<= data < 30: word="매우 나쁨"
    return word

def get_dust_data():
    endpoint_url = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc"
    service_path = "/getMsrstnAcctoRltmMesureDnsty" # 미세먼지

    API_KEY="B8Ywe1IIAAFMcXT/GhMDm7rgpAQKKZsR9YkL/5HljYgt/fIZ5H+d3G7I1SKCQ8TZWRS+7Y9R8bSzAyak0vu1VQ=="
    
    STATION_NAME = input('궁금한 지역을 입력하세요 : ')
    
    params = {
        'serviceKey' : API_KEY,
        'returnType' : 'json',
        'numOfRows' : 10,
        'pageNo' : 1,
        'stationName' : STATION_NAME,
        'dataTerm' : 'DAILY',
        'ver' : '1.0'
    }

    res = requests.get(f"{endpoint_url}{service_path}", params=params)

    if res.status_code == 200:
        print("Data get success")
        data = json.loads(res.text)
        items = data['response']['body']['items']
        print(items) # List

        for item in items:
            dust_level_val = dust_level(int(item['pm10Value']))
            microdust_level_val = dust_level(int(item['pm25Value']))
            print('미세먼지 : ' , dust_level_val)
            print('초미세먼지 : ' , microdust_level_val)

    else:
        print("Request failed error: {}".format(res.status_code))

get_dust_data()