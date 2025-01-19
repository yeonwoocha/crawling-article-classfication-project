from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import pandas as pd
import os
import yaml
import time
import requests
from bs4 import BeautifulSoup
import nltk
from textblob import TextBlob

'''
selector
html
    head 
    body


-- 전체 x-path
/html
    /html/head
    /html/body
'''



url = 'https://www.naver.com/'



options = webdriver.ChromeOptions()
options.add_argument('--disable-gpu')   # GPU 가속 비활성화
options.add_argument('--no-sandbox')
options.add_argument('--disable-webgl') # WebGL 문제 무시
options.add_argument('--disable-software-rasterizer')  # 소프트웨어 렌더링 비활성화
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get(url)

time.sleep(2)

# body 태그 가져오기
body = driver.find_element(By.CSS_SELECTOR, 'body')
# elements = body.find_element(By.ID, value='query')

# 검색어 검색
body.find_element(By.ID, value='query').click()
search_element = driver.find_element(By.ID, value='query')
search_element.send_keys("유니티소프트웨어")

# 검색 버튼 실행
a = driver.find_element(By.ID, 'search-btn').click()

a
time.sleep(4)

# 검색 후 페이지 body 태그 가져오기기
body1 = driver.find_element(By.CSS_SELECTOR, 'body')

body1.find_element(By.CLASS_NAME, value='mod_more_wrap').click()
time.sleep(4)

'''
# 페이지 끝까지 스크롤하여 콘텐츠 로드
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # 콘텐츠 로드 대기 (웹사이트에 따라 조정)

    # 새로운 높이 계산
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break  # 더 이상 로드할 콘텐츠가 없으면 종료
    last_height = new_height
'''

html = driver.page_source

# BeautifulSoup으로 분석
soup = BeautifulSoup(html, 'html.parser')
'''
with open('C:/Users/USER/YU/YU_python/crawling-data/crawling_article/crawler_news/drivers/train_data.txt', 'w', encoding='utf-8') as writer:
    writer.write(soup.prettify())
'''
news_title_elements = soup.find_all('a', class_='news_tit')
news_media_elements = soup.find_all('a', class_='info press')




for idx, (title_elm,  media_elm) in enumerate(zip(news_title_elements, news_media_elements), start=1):
    link = title_elm.get('href')
    print(f'{idx}번째 뉴스 제목 : {title_elm.text}, 뉴스 링크 : {link}, 뉴스 매체 : {media_elm.text}')
    with open('C:/Users/USER/YU/YU_python/crawling-data/crawling_article/crawler_news/drivers/main_train_data.txt', '+a', encoding='utf-8') as writer:
        writer.write(f'{idx}번째 뉴스 제목 : {title_elm.text}, 뉴스 링크 : {link}, 뉴스 매체 : {media_elm.text}\n' )
   
driver.quit()