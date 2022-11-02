from django.shortcuts import render, redirect
import urllib
import json
from urllib import parse
from urllib import request
from .models import Store
from .forms import StoreForm
from django.contrib.auth.decorators import login_required
import requests
from django.conf import settings
from reviews.models import Review,Comment


def index(request):
    data = Store.objects.all()
    context = {
        'stores': data
    }

    return render(request,'stores/index.html', context)

def detail(request,pk):
    data = Store.objects.get(pk=pk)
    reviews = data.reviews.get(pk=pk)
    comment = data.comment.all()
    context ={
        'store_data':data,
        'reviews':reviews,
        'comment':comment
    }
    return render(request,'stores/detail.html',context)

@login_required
def create(request):
    if request.method == 'POST':
        form = StoreForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('stores:index')
    else:
        form = StoreForm()
    context = {
        'form':form
    }
    return render(request, 'stores/create.html',context)

@login_required
def edit(request,pk):
    data = Store.objects.get(pk=pk)
    if (request.user == data.user) and (data.Is_owner == True) :
        if request.method == 'POST':
            store_form = StoreForm(request.POST, request.FILES, instance=data)
            if store_form.is_valid():
                store_form.save()
                return redirect('stores:detail',data.pk)
        else:
            store_form = StoreForm(instance=data)

        context = {
           'store_form':store_form
        }

        return render(request,'stores/edit.html',context)
    else:

        return redirect("stores:detail",data.pk)

@login_required
def delete(request,pk):
    data = Store.objects.get(pk=pk)
    if (request.user == data.user) and (data.Is_owner == True) :
        data.delete()
        return redirect('stores:index')




def kakao_search():
    searching = '합정 스타벅스'
    url = 'https://dapi.kakao.com/v2/local/search/keyword.json?query={}'.format(searching)
    headers = {
        "Authorization": "KakaoAK 0f23477b2b3262f820c688ff81fdf916"
    }
    places = requests.get(url, headers=headers).json()['documents']
    print(places)
