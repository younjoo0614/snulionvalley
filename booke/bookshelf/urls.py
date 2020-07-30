from django.urls import path
from bookshelf import views


urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.create_book,name='create_book'),
    path('recommend/',views.recommend_book,name='recommend_book'),
    path('<int:id>/', views.show_memo, name='show_memo'),
    path('<int:id>/delete/', views.delete_book, name='delete_book'),# 삭제 버튼이 책장에서 가능할지 아니면 메모보려 들어갔을 때 있을지 정해야 함
    path('<int:id>/memos/', views.create_memo, name='create_memo'),
    path('<int:id>/memos/<int:mid>/delete/', views.delete_memo, name='delete_memo'),    
]