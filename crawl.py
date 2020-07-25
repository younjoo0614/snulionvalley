from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
import re

baseUrl = 'https://book.naver.com/search/search.nhn?sm=sta_hty.book&sug=&where=nexearch&query='

plusUrl=input ('책 제목을 입력하세요: ')

url = baseUrl + quote_plus(plusUrl) #네이버 책 홈에서 책 제목을 검색해서 나오는 url
html = urlopen(url)
bsObject = BeautifulSoup(html, "html.parser")

site_for_page = bsObject.select('li > dl > dt > a') # 책 제목을 검색해서 뜨는 a 태그들 결과들의 링크

for site in site_for_page:
    print(site.attrs['href']) # 책의 상세정보 페이지 url

deturl=site_for_page[0].attrs['href'] # 페이지 수가 써있는 url로 들어옴 index 0으로 한 건 편의를 위함, 추후 바뀔 수 있음

html=urlopen(deturl)
bs=BeautifulSoup(html, "html.parser")

whole_page= bs.select('.book_info_inner > div') #우리가 찾는 div에 class 이름이 없어서 그냥 div로 찾고 index로 특정
 
a= whole_page[3].text.split(" ") #띄어쓰기 기준 문자열 분할-> a[1]에 '122|ISBN'이 들어감

#첫 번째 방법: |이 나오기 전까지 문자열 분할
def get_page(str):
    b=""
    for i in a[1]:
        if i!='|':
            b+=i
        else:
            return int(b)

page=get_page(a[1])
print(page)

#두 번째 방법: 정규식 활용
m=re.search('\d+',a[1])
print(int(m.group())) #m.group()만 해도 페이지 수가 출력되지만 자료형이 str이므로 연산가능한 int형으로 변환
