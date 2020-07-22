from django.urls import path
from bookshelf import views


urlpatterns = [
    path('', views.index, name='index'),
   
    
]