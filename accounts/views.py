from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from stores.models import Thematag, Foodtag
# Create your views here.
def index(request):
    Thematag.objects.create(thematag_name='가성비좋은')
    Thematag.objects.create(thematag_name='분위기좋은')
    Thematag.objects.create(thematag_name='푸짐한')
    Thematag.objects.create(thematag_name='격식있는')
    Thematag.objects.create(thematag_name='고급스러운')
    Thematag.objects.create(thematag_name='서민적인')
    Thematag.objects.create(thematag_name='시끌벅적한')
    Thematag.objects.create(thematag_name='조용한')
    Thematag.objects.create(thematag_name='깔끔한')
    Thematag.objects.create(thematag_name='이색적인')
    Thematag.objects.create(thematag_name='뷰가좋은')
    Thematag.objects.create(thematag_name='예쁜')
    Thematag.objects.create(thematag_name='지역주민이찾는')

    Foodtag.objects.create(foodtag_name='한식')
    Foodtag.objects.create(foodtag_name='중식')
    Foodtag.objects.create(foodtag_name='양식')
    Foodtag.objects.create(foodtag_name='일식')
    Foodtag.objects.create(foodtag_name='아시안')
    Foodtag.objects.create(foodtag_name='패스트푸드')

    return render(request, 'accounts/index.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('accounts:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('accounts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

def callback(request):
    return render(request, 'accounts/callback.html')

def logout(request):
    auth_logout(request)
    return redirect('accounts:index')

def mypage(request, pk):
    user = User.objects.get(pk=pk)
    context = {
        'user': user
    }
    return render(request, 'accounts/mypage.html', context)

@login_required
def mypage_update(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('accounts:mypage', user.pk)
    else:
        form = CustomUserChangeForm(instance=user)
    context = {
        'form': form
    }
    return render(request, 'accounts/mypage-update.html', context)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('accounts:mypage', request.user.pk)
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)

def mypage_delete(request, pk):
    user = User.objects.get(pk=pk)
    user.delete()
    return redirect('accounts:index')

def temp(request, pk):
    print(pk)
    return render('accounts:index')

def database(request):
    jsonObject = json.loads(request.body)
    username = jsonObject.get('username')
    users = User.objects.filter(username=username)
    print(users)
    if users:
        user = User.objects.get(username=username)
        auth_login(request, user)
    else:
        user = User()
        user.username = jsonObject.get('username')
        user.email = jsonObject.get('email')
        user.save()
        user = User.objects.get(username=username)
        auth_login(request, user)
    return JsonResponse({'username': user.username, 'email': user.email})

def database_naver(request):
    jsonObject = json.loads(request.body)
    username = jsonObject.get('id')
    print(username)
    users = User.objects.filter(username=username)
    if users:
        user = User.objects.get(username=username)
        auth_login(request, user)
        print('complete!')
    else:
        user = User()
        user.username = jsonObject.get('id')
        print(jsonObject.get('id'))
        user.nickname = jsonObject.get('name')
        user.email = jsonObject.get('email')
        # user.phone = jsonObject.get('mobile')
        user.save()
        user = User.objects.get(username=username)
        auth_login(request, user)
    return JsonResponse({'username': user.username, 'email': user.email})

# @csrf_exempt
# def kakaoLogin(request):
#     form = AuthenticationForm(request, data=request.POST)
#     if form.is_valid():
#         auth_login(request, form.get_user())
#         return redirect('accounts:index')

# '{"username":2508796199,"email":"dayeong5479@hanmail.net"}'