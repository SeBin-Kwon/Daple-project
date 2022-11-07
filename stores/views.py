from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
import urllib
import json
from urllib import parse
from urllib import request
from .models import Store
from .forms import StoreForm
from reviews.models import Review, Comment
from reviews.forms import ReviewForm, CommentForm
from django.http import JsonResponse
import datetime
from django.contrib.auth.decorators import login_required
import requests
import json
from django.db.models import Q
from django.core.paginator import Paginator

from accounts.models import User


def index(request):

    if request.method == 'POST':
        jsonObject = json.loads(request.body)
        for i in range(len(jsonObject)):
            if not Store.objects.filter(kakao_id=jsonObject[i]['id']).exists():
                db = Store.objects.create(
                    store_address=jsonObject[i]['address_name'],
                    store_tel=jsonObject[i]['phone'],
                    store_name=jsonObject[i]['place_name'],
                    store_url=jsonObject[i]['place_url'],
                    store_x=jsonObject[i]['x'],
                    store_y=jsonObject[i]['y'],
                    kakao_id=jsonObject[i]['id'])
                db.save()
        return render(request, 'stores/index.html',)
    else:
        data = Store.objects.all()

        page = request.GET.get("page")
        data_all = Store.objects.all()
        paginator = Paginator(data_all, 6)
        posts = paginator.get_page(page)
        context = {
            'stores': data,
            'posts': posts
        }

    return render(request, 'stores/index.html', context)


def detail(request, pk):
    data = Store.objects.get(pk=pk)

    reviews = Review.objects.filter(store_id=pk).order_by('-pk')
    sum_rating = 0
    for review in reviews:
        sum_rating += review.review_rating
    people_num = len(reviews)
    if sum_rating:
        avg_rating = round(sum_rating / people_num,1)
    else:
        avg_rating = 0

    comments = Comment.objects.all().order_by('-pk')
    comment_form = CommentForm()
    
    
    if Review.objects.filter(store_id=pk).filter(user_id=request.user.pk):
        is_write = True
    else:
        is_write = False

    context = {
        'store_data': data,
        'reviews': reviews,
        'comment_form': comment_form,
        'comments': comments,
        'avg_rating': avg_rating,
        'people_num': people_num,
        'is_write': is_write
    }

    return render(request, 'stores/detail.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = StoreForm(request.POST, request.FILES)
        if form.is_valid():
            new = form.save(commit=False)
            new.user = request.user
            new.save()
            return redirect('stores:index')
    else:
        form = StoreForm()
    context = {
        'form': form
    }
    return render(request, 'stores/create.html', context)


@login_required
def edit(request, pk):
    data = Store.objects.get(pk=pk)
    if (request.user == data.user) and (data.Is_owner == True):
        if request.method == 'POST':
            store_form = StoreForm(request.POST, request.FILES, instance=data)
            if store_form.is_valid():
                store_form.save()
                return redirect('stores:detail', data.pk)
        else:
            store_form = StoreForm(instance=data)

        context = {
            'store_form': store_form
        }

        return render(request, 'stores/edit.html', context)
    else:

        return redirect("stores:detail", data.pk)


@login_required
def delete(request, pk):
    data = Store.objects.get(pk=pk)
    if (request.user == data.user) and (data.Is_owner == True):
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


def store_like(request, pk):
    store = get_object_or_404(Store, pk=pk)

    if store.store_liked.filter(id=request.user.id).exists():
        # if request.user in store.store_liked.all():
        store.store_liked.remove(request.user)
        is_liked = False
    else:
        store.store_liked.add(request.user)
        is_liked = True
    context = {'isLiked': is_liked, 'likeCount': store.store_liked.count()}
    return JsonResponse(context)


def db_save(request):
    return redirect('stores:index')


def search(request):
    if request.method == 'POST':
        store_search = request.POST['store_search']
        for i in range(1, 46):
            searching = store_search

            num = i
            url = 'https://dapi.kakao.com/v2/local/search/keyword.json?page={}&query={}'.format(num, searching)
            headers = {
                "Authorization": "KakaoAK 0f23477b2b3262f820c688ff81fdf916"
            }
            places = requests.get(url, headers=headers).json()
            page = places['meta']['is_end']
            places = places['documents']
            if page == True:
                break
            elif (page == False and (
                    places[i]['category_group_code'] == "FD6" or places[i]['category_group_code'] == 'CE7')
            and Store.objects.filter(kakao_id=places[i]['id']).exists() == False):
                for i in range(len(places) ):
                    db_save = Store(store_name=places[i]["place_name"], store_address=places[i]["address_name"],
                                    store_x=places[i]["x"],
                                    store_y=places[i]["y"],
                                    store_url=places[i]['place_url'],
                                    store_tel=places[i]['phone'],
                                    kakao_id=places[i]["id"])
                    db_save.save()
        results = Store.objects.filter(Q(store_name__contains=store_search)|Q(store_address__contains=store_search))
        context = {
            'search': store_search,
            'results': results
        }
        return render(request, 'stores/search.html', context)

def name_sort(request):
    jsonObject = json.loads(request.body)
    search = jsonObject.get('search')
    
    temp_results = Store.objects.all().filter(Q(store_name__contains=search)).order_by('store_name')
    results = []
    for result in temp_results:
        results.append({'store_pk': result.pk, 'store_name': result.store_name, 'store_address': result.store_address})
    print(results)

    return JsonResponse({'results': results})

# def like_sort(request):
#     jsonObject = json.loads(request.body)
#     search = jsonObject.get('search')
    
#     temp_results = Store.objects.all().filter(Q(store_name__contains=search)).order_by('store_liked')
#     results = []
#     for result in temp_results:
#         results.append({'store_pk': result.pk, 'store_name': result.store_name, 'store_address': result.store_address})
#     print(results)

#     return JsonResponse({'results': results})

def like_sort(request):
    jsonObject = json.loads(request.body)
    search = jsonObject.get('search')
    
    temp_results = Store.objects.all().filter(Q(store_name__contains=search)).order_by('store_liked')
    results = []
    for result in temp_results:
        results.append({'store_pk': result.pk, 'store_name': result.store_name, 'store_address': result.store_address})
    print(results)

    return JsonResponse({'results': results})

def score_sort(request):
    jsonObject = json.loads(request.body)
    search = jsonObject.get('search')
    
    temp_results = Store.objects.all().filter(Q(store_name__contains=search)).order_by('store_grade')
    results = []
    for result in temp_results:
        results.append({'store_pk': result.pk, 'store_name': result.store_name, 'store_address': result.store_address})
    print(results)

    return JsonResponse({'results': results})