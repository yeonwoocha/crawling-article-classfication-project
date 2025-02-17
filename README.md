# crawling-article-classfication

이 프로젝트는 Selenium과 BeautifulSoup을 활용하여 네이버 검색 페이지에서 뉴스 데이터를 수집하는 방법을 시도합니다. 기존의 XPath 기반 개별 요소 접근 방식과 달리, 전체 HTML 페이지를 긁어와서 BeautifulSoup으로 파싱하는 방식으로 진행하여 다양한 뉴스 데이터를 추출합니다.

### 주요 기능
Selenium 기반 브라우저 자동화

네이버 메인 페이지 접속 및 검색창 자동 입력
검색 버튼 클릭 및 결과 페이지 로드
추가적인 페이지 요소(예: '더보기' 버튼) 클릭을 통해 뉴스 결과를 확장


### HTML 파싱 및 데이터 추출

Selenium으로 가져온 전체 HTML 소스를 BeautifulSoup을 이용해 파싱
뉴스 제목(news_tit)과 뉴스 매체 정보(info press) 추출
추출한 뉴스 데이터(제목, 링크, 매체)를 콘솔 출력 및 파일에 저장


### 데이터 저장

추출한 뉴스 데이터를 지정된 텍스트 파일에 추가 기록하여 보존
