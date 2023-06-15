import pandas as pd
import numpy as np
import re	# regular expression (정규표현식)사용을 위해
from bs4 import BeautifulSoup 	# 오늘의 핵심
from urllib.request import urlopen, Request  #오늘의 핵심 2
url = 'https://www.mangoplate.com/top_lists/2966_gyeonggido2022'
req = Request(url, headers={'User-Agent': 'Chrome'})  
# 그냥 불러오면 500 error가 납니다. 
# 그래도 다행히 headers넣어주니까 잘 불러와졌습니다(안도의 한숨)

html = urlopen(req)
mang = BeautifulSoup(html, 'html.parser')
# print(mang.prettify())
# prettify()는 들여쓰기를 실행해서 가독성을 높여줍니다.

# 빈 리스트들을 준비해둡니다.
name = []
point = []
address = []

# 세 가지 정보를 모두 포함하는 상위 태그로 선택하였습니다.
list_soup = mang.find_all('div', 'info') 

# 각 리스트에 append()로 추가해줍니다.
for item in list_soup:
    address.append(item.find('p', 'etc').text)
    point.append(item.find('strong', 'point').text.strip())
    title = item.find('span', 'title').text.strip()
    name.append(title[3:])

name = name[:10]
point = point[:10]
address = address[:10]

print(name, point, address)

# 데이터 프레임 만들기
data = {
    "foods":name,
    'Point' : point,
    'Address' : address
}
df = pd.DataFrame(data)
print(df)

# 저장
df.to_csv(
    '맛집 찾기/맛집경기.csv', header=None, index=False, sep=',', encoding='utf-8'
)