from django.shortcuts import render, redirect
from django.contrib import auth
from .models import Author, Book, UserBook, Memo
from accounts.models import Profile
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
import re
from django.http import JsonResponse

# Create your views here.

def get_page_author(title,select):
    baseUrl = 'https://book.naver.com/search/search.nhn?sm=sta_hty.book&sug=&where=nexearch&query='

    url = baseUrl + quote_plus(title) #네이버 책 홈에서 책 제목을 검색해서 나오는 url
    html = urlopen(url)
    bsObject = BeautifulSoup(html, "html.parser")

    site_for_page = bsObject.select('li > dl > dt > a') # 책 제목을 검색해서 뜨는 a 태그들 결과들의 링크

    deturl=site_for_page[select].attrs['href'] # 페이지 수가 써있는 url로 들어옴 index 0으로 한 건 편의를 위함, 추후 바뀔 수 있음

    html=urlopen(deturl)
    bs=BeautifulSoup(html, "html.parser")

    whole_page= bs.select('.book_info_inner') 

    m=re.search('페이지.\d+',whole_page[0].text)
    n=re.search('저자.(\w+|\s|\.)+',whole_page[0].text)

    page=re.search('\d+',m.group())
    author=re.search('(?!저)(?!자)(?!\s)(\w+|\s|\.)+',n.group()) #정규식 앞에 '저자 ' 제거하는 방법이 있을 거 같은데...
    
    page_author=[page.group(),author.group()]
    return page_author

def index(request):
    # queryset 잘 몰라서 참고하려고 둔 사이트https://docs.djangoproject.com/en/3.0/topics/db/queries/
    if request.method=='POST':
        member=request.user.profile
        #아직 외부 api 신청 안 한 상태라 직접 입력하는 방식으로 함
        book_title=request.POST['title']
        book_author=get_page_author(book_title,0)[1]

        #Author에 지금 유저가 추가하려고 하는 책이 이미 있는지 확인하고 없으면 추가
        
        try:
            is_author_in_list=Author.objects.get(name=book_author)

        except Author.DoesNotExist:
            Author.objects.create(name=book_author)
        
        bookauthor=Author.objects.get(name__iexact=book_author)
        #Book에 지금 유저가 추가하려고 하는 책이 이미 있는지 확인하고 없으면 추가
        try:
            is_in_list=Book.objects.get(title__iexact=book_title, author=bookauthor)

        except Book.DoesNotExist:
            Book.objects.create(title=book_title, author=bookauthor)
        
        book= Book.objects.get(title__iexact=book_title, author=bookauthor)
        # 저장된 횟수 추가
        book.count+=1
        bookauthor.count+=1
        book.save()
        bookauthor.save()

        whole_page=int(get_page_author(book_title,0)[0])
        member.already_read+=whole_page
        UserBook.objects.create(userid=member,bookid=book,whole_page=whole_page)
        
        return JsonResponse({"message":"created"},status=201)
    else: 
        books=UserBook.objects.all()
        authors=Author.objects.all()
        return render(request,'bookshelf/index.html',{"books":books,"authors":authors})
    

def create_book(request):
    return render(request,'bookshelf/new.html')

def list_friends(request):
    followers=request.user.profile.follows
    return request(request,'index.html',{"follows":follows})

def delete_book(request,id):
    userbook=UserBook.objects.get(id=id)
    userbook.delete()
    return redirect('/bookshelf')

def show_memo(request,id):
    userbook=UserBook.objects.get(id=id)
    memos=Memo.objects.filter(book=userbook)
    return render(request, 'bookshelf/show.html',{'userbook':userbook,'memos':memos})

def recommend_book(request):
    by_book=Book.objects.all().order_by('-count')
    best_author=Author.objects.all().order_by('-count').first()
    by_author=Book.objects.filter(author=best_author)#.exclude로 자기가 읽은 책 제외해야 함
    return render(request,'bookshelf/recommend.html',{"by_books":by_book,'by_author':by_author})

def create_memo(request,id):
    page=request.POST['page']

    content=request.POST['content']
    Memo.objects.create(content=content, page=page,book_id=id )

    new_memo = Memo.objects.latest('id')

    context = {
        # memo의 id도 필요할까?
        # memo 자체에 접근하려면 필요한데 삭제 말고 접근할 일이 없으니 일단 두기
        'page': new_memo.page,
        'content': new_memo.content,
    }

    # return redirect('bookself/show.html')
    return JsonResponse(context)

def delete_memo(request,id,mid):
    m=Memo.objects.get(id=mid)
    m.delete()
    
    return redirect('bookshelf/show.html')
