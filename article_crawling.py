from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import pandas as pd
import os
import time
import requests
from bs4 import BeautifulSoup
# import nltk
# from textblob import TextBlob
import json


options = webdriver.ChromeOptions()
options.add_argument('--disable-gpu')   # GPU 가속 비활성화
options.add_argument('--no-sandbox')
options.add_argument('--disable-webgl') # WebGL 문제 무시
options.add_argument('--disable-software-rasterizer')  # 소프트웨어 렌더링 비활성화
driver = webdriver.Chrome(options=options)
driver.maximize_window()

url = 'https://www.naver.com/'
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

html = driver.page_source

# BeautifulSoup으로 분석
soup = BeautifulSoup(html, 'html.parser')

with open('./train_data.txt', 'w', encoding='utf-8') as writer:
    writer.write(soup.prettify())

news_title_elements = soup.find_all('a', class_='news_tit')
news_media_elements = soup.find_all('a', class_='info press')

news_data = []

for idx, (title_elm,  media_elm) in enumerate(zip(news_title_elements, news_media_elements), start=1):
    link = title_elm.get('href')
    print(f'{idx}번째 뉴스 제목 : {title_elm.text}, 뉴스 링크 : {link}, 뉴스 매체 : {media_elm.text}')
    json_data = {
        "index" : idx,
        "title" : title_elm.text,
        "link"  : link,
        "media" : media_elm.text
    }
    news_data.append(json_data)

with open('./main_train_data.json', 'w', encoding='utf-8') as writer:
    # json_data = json.load(writer)
    # writer.write(f'{idx}번째 뉴스 제목 : {title_elm.text}, 뉴스 링크 : {link}, 뉴스 매체 : {media_elm.text}\n' )
    json.dump(news_data, writer, ensure_ascii=False, indent=4)

def extract_article_body(html):
    soup = BeautifulSoup(html, 'html.parser')
    article_text = []
    
    try:
        # 각 기사 본문 태그
        content = soup.select_one('div.news_cnt_detail_wrap, div.articleView, div#news-contents')
        if content:
            article_text = [p.get_text(strip=True) for p in content.find_all('p')]
    except Exception as e:
        print(f"Error with primary pattern: {e}")

    if not article_text:
        try:
            article_text = [p.get_text(strip=True) for p in soup.find_all('p') if p.get_text(strip=True)]
        except Exception as e:
            print(f"Error with fallback pattern: {e}")
    
    return '\n'.join(article_text)

with open('./main_train_data.json', 'r', encoding='utf-8') as reader:
    data = json.load(reader)

for i in range(len(data)):
    link = data[i]['link']
    driver.get(link)
    time.sleep(4)
    html = driver.page_source
    # BeautifulSoup으로 분석
    soup = BeautifulSoup(html, 'html.parser')
    with open(f'./link_body_{i}.txt', 'w', encoding='utf-8') as writer:
        writer.write(soup.prettify())
    
    # 기사 본문만 스크랩랩
    text = soup.find_all('p')
    with open(f'./test_{i}.txt', 'w', encoding='utf-8') as writer:
        for i in text:
            writer.write(i.text)
            

driver.quit()