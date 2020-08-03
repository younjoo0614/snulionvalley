from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect
from django.contrib.auth import login as django_login
from django.contrib.auth import authenticate as django_authenticate
from django.http import JsonResponse
from .models import Profile,Follow


def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password1"]
        goal = request.POST["goal"]
        taste = request.POST["taste"]

        user = User.objects.create_user(username=username, password=password)
        user.profile.nickname = username
        user.profile.goal = goal
        user.profile.taste = taste
        user.save()

        login_user = django_authenticate(username=username, password=password)
        django_login(request, login_user)
        return JsonResponse({"response": "signup success"})

# 모달 전 기존 회원가입 함수.. 기록용! 무시해도 됨
# def signup(request):
#     if request.method  == 'POST':
#         if request.POST['password1'] == request.POST['password2']:
#             user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
#             auth.login(request, user)
#             return redirect('/bookshelf')
#     return render(request, 'accounts/signup.html')

#def login(request):
    # return render(request, 'accounts/login.html')

def logout(request):
    return render(request, 'accounts/logout.html')

def follow_manager(request, fid):
    followed_by = Profile.objects.get(user_id = request.user.id)
    follow = Profile.objects.get(user_id = fid)

    try:
        following_already = Follow.objects.get(followed_by=followed_by, follow=follow)
    except Follow.DoesNotExist:
        following_already = None

    if following_already:
        following_already.delete()
    else:
        f = Follow()
        f.followed_by, f.follow = followed_by, follow
        f.save()
    print('follow_manager')
    return redirect('/bookshelf')

def result(request):
    fs = Profile.objects.all()
    f = request.GET['friend-value']
    if f:
        fs = Profile.objects.filter(nickname__startswith=f)
    return render(request, 'bookshelf/index.html', {'f_result':fs})