import urllib.request 
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
import re
'''

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

whole_page= bs.select('.book_info_inner') #우리가 찾는 div에 class 이름이 없어서 그냥 div로 찾고 index로 특정

#첫번째 방법은 문자열 분할로 하는 거였는데 책마다 상세페이지 구조가 달라서 정규식 사용해야 하넹...

#두 번째 방법: 정규식 활용
m=re.search('페이지.\d+',whole_page[0].text)
print(m.group()) #m.group()만 해도 페이지 수가 출력되지만 자료형이 str이므로 연산가능한 int형으로 변환

b=m.group()
page=re.search('\d+',b)
print(int(page.group()))
'''
title=input('제목을 입력하세요: ')
baseUrl = 'https://book.naver.com/search/search.nhn?sm=sta_hty.book&sug=&where=nexearch&query='

url = baseUrl + quote_plus(title) #네이버 책 홈에서 책 제목을 검색해서 나오는 url
html = urllib.request.urlopen(url)
bsObject = BeautifulSoup(html, "html.parser")

site_for_page = bsObject.select('li > dl > dt > a') # 책 제목을 검색해서 뜨는 a 태그들 결과들의 링크

deturl=site_for_page[0].attrs['href'] # 페이지 수가 써있는 url로 들어옴 index 0으로 한 건 편의를 위함, 추후 바뀔 수 있음

html= urllib.request.urlopen(deturl)
bs=BeautifulSoup(html, "html.parser")

title_div=bs.select('.book_info > h2 > a')

whole_page= bs.select('.book_info_inner') 

for i in title_div:
    print(i.text)

m=re.search('페이지.\d+',whole_page[0].text)
n=re.search('저자.(\w+|\s|\.)+',whole_page[0].text)
o=re.search('(\w+|\s|,)+',title_div[0].text)

page=re.search('\d+',m.group())
author=re.search('(?!저자\s)(\w+|\s|\.)+',n.group())
title=re.search('(\w+|\s|,)+',o.group())

page_author=[page.group(),author.group()]

print (title.group())
print (page.group())
print (author.group())