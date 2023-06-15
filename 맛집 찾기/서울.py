import pandas as pd
import numpy as np
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import requests
import time
import warnings
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
warnings.simplefilter(action='ignore')

url = "https://www.mangoplate.com/top_lists/D12L0IS" # url만 바꾸면 됨<-- "https://www.mangoplate.com/top_lists/2963_gangwondo2022", "https://www.mangoplate.com/top_lists/2749_gyeongsangdo2021", "https://www.mangoplate.com/top_lists/I3IBPRC", "https://www.mangoplate.com/top_lists/KSWVV24", "https://www.mangoplate.com/top_lists/1259_daejeon","https://www.mangoplate.com/top_lists/2965_busan2022","https://www.mangoplate.com/top_lists/D12L0IS","https://www.mangoplate.com/top_lists/ABRDRL2","https://www.mangoplate.com/top_lists/2751_jeollado2021","https://www.mangoplate.com/top_lists/2964_jejudo2022","https://www.mangoplate.com/top_lists/2752_chungcheongdo2021"

req = Request(url, headers={'User-Agent': 'Chrome'})

html = urlopen(req)
mang = BeautifulSoup(html, 'html.parser')

name = []
point = []
address = []
imgurl = []

driver = webdriver.Chrome('../driver/chromedriver.exe')
driver.get(url)
time.sleep(3)

for i in range(3):
    some_tag = driver.find_element(By.CSS_SELECTOR, '#contents_list > div > button')
    action = ActionChains(driver)
    action.move_to_element(some_tag).perform()
    some_tag.click()
    time.sleep(2)
    html = driver.page_source  # 현재 페이지의 HTML 소스코드 가져오기
    mang = BeautifulSoup(html, 'html.parser')  # BeautifulSoup 객체로 파싱

    list_soup = mang.find_all('div', 'info')  # 수정: 새로운 페이지에서 list_soup 재설정
    for item in list_soup:
        address.append(item.find('p', 'etc').text.strip())
        point.append(item.find('strong', 'point').text.strip())
        title = item.find('span', 'title').text.strip()
        name.append(title[3:])
    html = driver.page_source  # 현재 페이지의 HTML 소스코드 가져오기
    mang = BeautifulSoup(html, 'html.parser')  # BeautifulSoup 객체로 파싱
    # 이미지 태그 찾기 (CSS 선택자 사용)
    images = driver.find_elements(By.CSS_SELECTOR, ".center-croping.lazy")
    for image in images:
        src = image.get_attribute('data-original')
        imgurl.append(src)

# print(imgurl)




driver.quit()  # WebDriver 종료

# print(name, point, address)

name = name[58:98] 
point = point[58 : 98]
address = address[58 : 98] 
imgurl = imgurl[58 : 98]

print(name, point, address)

# 데이터 프레임 만들기
data = {
    "foods":name,
    'Point' : point,
    'Address' : address,
    "imgurl": imgurl
}
df = pd.DataFrame(data)
print(df)

# 저장
df.to_csv(
    '맛집 찾기/맛집서울.csv', header= None, index = False, sep=',', encoding='utf-8'
)

