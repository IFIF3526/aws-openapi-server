import requests
from config import Config

# URL 은 config.py 파일에 있다.
# client_id 와 client_secret 도 config.py 파일에 있다.

# 데이터부분을 셋팅해야 하는데,
# GET으로 호출하기 때문에, requests.get()함수를 이용한다.

headers = {'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8', 'X-Naver-Client-Id' : Config.NAVER_CLINET_ID, 'X-Naver-Client-Secret' : Config.NAVER_CLINET_SECRET}

data = {'query' : '타잔'}

res = requests.get(Config.NAVER_MOVIE_SEARCH_URL, data, headers= headers)

res = res.json()

print(res)