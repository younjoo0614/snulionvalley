from django.urls import path
from map import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('red/', views.red, name='red'),
    path('orange/', views.orange, name='orange'),
    path('yellow/', views.yellow, name='yellow'),
    path('green/', views.green, name='green'),
]