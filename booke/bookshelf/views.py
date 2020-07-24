from django.shortcuts import render, redirect
from django.contrib import auth
from .models import Author, Book, UserBook, Memo
from accounts.models import Profile

# Create your views here.
def index(request):
    return render(request, 'bookshelf/index.html')

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
        UserBook.objects.create(userid=member.id,bookid=book.id)
        
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
    memos=Memo.objects.filter(book=id)
    return render(request, 'bookshelf/show.html',{'userbook':userbook,'memos':memos})

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