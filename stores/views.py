from django.shortcuts import render, redirect
import urllib
import json
from urllib import parse
from urllib import request
from .models import Store
from .forms import StoreForm
from django.contrib.auth.decorators import login_required


def index(request):
    data = Store.objects.all()
    context = {
        'stores': data
    }

    return render(request,'stores/index.html', context)

def detail(request,pk):
    data = Store.objects.get(pk=pk)
    context ={
        'store_data':data
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
    if request.user == data.user:
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
    if request.method == 'POST':
        data = Store.objects.get(pk=pk)
        data.delete()
        return redirect('stores:index')


def test():
    client_id = "uCCiykUMH5IF4JADGgWL"
    client_secret = "mD53NEgVgg"
    encText = urllib.parse.quote("우동")
    url = "https://openapi.naver.com/v1/search/local?query=" + encText + "&display=10&start=1&sort=random"  # JSON 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if rescode == 200:
        response_body = response.read()
        response_body = response_body.decode('utf-8')
        response_body = json.loads(response_body)
        temp = response_body["items"]
        for i in range(len(temp)):
            db_save = Store(store_name=temp[i]["title"], store_address=temp[i]["address"], store_x=temp[i]["mapx"],
                            store_y=temp[i]["mapy"])
            db_save.save()
        print(temp[0]["address"])
        result = []
        for i in range(len(temp)):
            result.append(temp[i]["address"])
        print(result)
    else:
        print("Error Code:" + rescode)

    return render(request, "stores/index.html", )


