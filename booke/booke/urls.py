"""booke URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import bookshelf.views
import accounts.views
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bookshelf.views.index, name='index'),
    path('bookshelf/', include('bookshelf.urls')),
    path('accounts/', include('allauth.urls')), #allauth 쓰면 templates 안에 이름 account로 해야 하는 건지 확인 필요
    # path('accounts/', include('django.contrib.auth.urls'))
    # path('accounts/signup/', accounts.views.signup, name='account_signup'),
    path('accounts/result/', accounts.views.result, name='search_friend'),
    path('accounts/result/<int:fid>/follow', accounts.views.follow_manager,name='follow_manager'),
    # path('accounts/', include('allauth.urls')), #allauth 쓰면 templates 안에 이름 account로 해야 하는 건지 확인 필요
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

