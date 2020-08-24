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
    image=models.CharField(max_length=255, blank=True,null=True)

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
    isopen=models.BooleanField(default=True)

#https://github.com/yeonnseok/django-study/wiki/Django-%EB%B3%B5%EC%8A%B5-%EB%B0%8F-%EC%98%88%EC%A0%9C