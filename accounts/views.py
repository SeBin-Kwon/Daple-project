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

# Create your views here.
def index(request):
    return render(request, 'accounts/index.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
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
    # user = User()
    user = User.objects.get(username=jsonObject.get('username'))
    # user.username = jsonObject.get('username')
    # user.email = jsonObject.get('email')
    # user.save()
    print(user.username)
    print(request.session)
    auth_login(request, user)
    print('1')
    return JsonResponse({'username': user.username, 'email': user.email})

# @csrf_exempt
# def kakaoLogin(request):
#     form = AuthenticationForm(request, data=request.POST)
#     if form.is_valid():
#         auth_login(request, form.get_user())
#         return redirect('accounts:index')

# '{"username":2508796199,"email":"dayeong5479@hanmail.net"}'