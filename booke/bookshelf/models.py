from django.db import models
from django.utils import timezone
from accounts.models import Profile


class Author(models.Model):
    name=models.CharField(max_length=20, blank=False,null=True)
    count=models.IntegerField(default=0)
    def __str__(self):
        return self.name

#회원들이 저장한 전체 책 관리 
class Book(models.Model):
    title=models.CharField(max_length=20,blank=False,null=True)
    author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name="book")
    count=models.IntegerField(default=0) #몇 명의 회원들이 해당 책을 저장했는지

    def __str__(self):
        return self.title

class UserBook(models.Model):
    userid=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='books')
    bookid=models.ForeignKey(Book, on_delete=models.CASCADE, related_name="users")
    whole_page=models.IntegerField()
    color=models.CharField(max_length=20,blank=False,null=True)

class Memo(models.Model):
    book=models.ForeignKey(UserBook, on_delete=models.CASCADE)
    content=models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    page = models.IntegerField(blank=True, null=True)

#링크를 걸어서 친구 책장에 가는 것은 지금 url 설계상 불가능
#유저 id가 url에 들어있게 하는 방법으로 구분하면 가능할 수도 있지만 가능하진지는 확인 필요
#불가능하다면 userbook object 전체 중 userid가 친구 id에 해당하는 것을 골라 페이지를 만들어보여줘야 할 듯
#https://github.com/yeonnseok/django-study/wiki/Django-%EB%B3%B5%EC%8A%B5-%EB%B0%8F-%EC%98%88%EC%A0%9C