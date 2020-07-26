from django.shortcuts import render, redirect
from django.contrib import auth
from .models import Author, Book, UserBook, Memo
from accounts.models import Profile
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
import re

# Create your views here.
def index(request):
    member=request.user.profile
    ratio=member.already_read/member.goal
    return render(request, 'bookshelf/index.html',{"ratio":ratio})

def get_page(title,select):
    baseUrl = 'https://book.naver.com/search/search.nhn?sm=sta_hty.book&sug=&where=nexearch&query='

    plusUrl=input ('책 제목을 입력하세요: ')

    url = baseUrl + quote_plus(plusUrl) #네이버 책 홈에서 책 제목을 검색해서 나오는 url
    html = urlopen(url)
    bsObject = BeautifulSoup(html, "html.parser")

    site_for_page = bsObject.select('li > dl > dt > a') # 책 제목을 검색해서 뜨는 a 태그들 결과들의 링크

    deturl=site_for_page[select].attrs['href'] # 페이지 수가 써있는 url로 들어옴 index 0으로 한 건 편의를 위함, 추후 바뀔 수 있음

    html=urlopen(deturl)
    bs=BeautifulSoup(html, "html.parser")

    whole_page= bs.select('.book_info_inner') 

    m=re.search('페이지.\d+',whole_page[0].text)
    b=m.group()
    page=re.search('\d+',b)
    
    return int(page.group())

def create_book(resquest):
    # queryset 잘 몰라서 참고하려고 둔 사이트https://docs.djangoproject.com/en/3.0/topics/db/queries/
    if request.method=='POST':
        member=request.user.profile
        #아직 외부 api 신청 안 한 상태라 직접 입력하는 방식으로 함
        title=request.POST['title']
        author=request.POST['author']

        #Author에 지금 유저가 추가하려고 하는 책이 이미 있는지 확인하고 없으면 추가
        try:
            is_author_in_list=Author.objects.get(author=author)

        except Author.DoesnotExist:
            Author.objects.create(name=author)
        
        bookauthor=Author.objects.get(name__iexact=author)
        #Book에 지금 유저가 추가하려고 하는 책이 이미 있는지 확인하고 없으면 추가
        try:
            is_in_list=Book.objects.get(title__iexact=title, author=bookauthor.id)

        except Book.DoesNotExist:
            Book.objects.create(title=title, author=bookauthor.id)
        
        book= Book.objects.get(titl__iexact=title, author=bookauthor.id)
        # 저장된 횟수 추가
        book.count+=1
        bookauthor.count+=1
        book.save()
        bookauthor.save()

        whole_page=get_page(title,0)
        member.already_read+=whole_page
        UserBook.objects.create(userid=member.id,bookid=book.id,whole_page=whole_page)
        
        return redirect ('/')
    
    UserBook=Book.objects.all()
    authors=Author.objects.all()
    return render(request,'bookshelf/index.html',{"books":books,"authors":authors})

def delete_book(request,id):
    userbook=UserBook.objects.get(id=id)
    userbook.delete()
    return redirect('/bookshelf')

def show_memo(request,id):
    userbook=UserBook.objects.get(id=id)
    book_for_title=Book.objects.get(id=userbook.bookid)
    author_id=book_in_list.author
    author=Author.objects.get(id=autor_id)
    memos=Memo.objects.filter(book=id)
    return render(request, 'bookshelf/show.html',{'userbook':userbook,'memos':memos,'book_for_title':book_for_title,'author':author})

def recommend_book(request):
    by_book=Book.objects.all().order_by('-count')
    best_author=Author.objects.all().order_by('-count').first()
    by_author=Book.objects.filter(author=best_author.id)#.exclude로 자기가 읽은 책 제외해야 함
    return render(request,'bookshelf/recommend.html',{"by_books":by_book,'by_author':by_author})

def create_memo(request,id):
    page=request.POST['page']
    content=request.POST['content']    
    Memo.objects.create(content=content, page=page)

    return redirect('bookself/show.html')

def delete_memo(request,id,mid):
    m=Memo.objects.get(id=mid)
    m.delete()

    return redirect('bookshelf/show.html')