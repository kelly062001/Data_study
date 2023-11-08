import googlemaps #poetry andd googlemaps, pip install googlemaps



#(1) 위, 경도 데이터
def get_geo_info():
    API_KEY='AIzaSyC1sMpAAm-Zf6dMlQgrXj0hfFu0GtTjN9M'
    gmaps = googlemaps.Client(key=API_KEY)
    
    address = '서울시 강남구'
    res = gmaps.geocode(address, language='ko')
    
    lat = res[0]['geometry']['location']['lat']
    lng = res[0]['geometry']['location']['lng']
    
    return [lat, lng]
    
    
import requests
#(2) 위, 경도 데이터 -> 날씨 API로 호출
def get_weather_info():
    lat, lng = get_geo_info()
    final_url =f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lng}&daily=temperature_2m_max,temperature_2m_min&timezone=Asia%2FTokyo'
    
    
    res = requests.get(final_url)
    data = json.loads(res.text)
    print(data)

get_weather_info()