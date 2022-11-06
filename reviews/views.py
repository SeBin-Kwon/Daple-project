from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Review, Comment
from stores.models import Store
from accounts.models import User
from .forms import ReviewForm, CommentForm
from django.http import JsonResponse
import json
import datetime
# Create your views here.

def index(request):
    reviews = Review.objects.order_by('-pk')
    comments = Comment.objects.all().order_by('-pk')
    comment_form = CommentForm()
    context = {
        'reviews' : reviews,
        'comment_form' : comment_form,
        'comments':comments,
    }
    return render(request, 'reviews/index.html', context)

def create(request, pk):
    store = Store.objects.get(pk=pk)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST,request.FILES)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.store = store
            review_form.save()
            return redirect('stores:detail', pk)
    else:
        review_form = ReviewForm()
    context = {
        'review_form' : review_form,
    }
    return render(request, 'reviews/form.html', context)

def update(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, request.FILES, instance=review)
        if review_form.is_valid():
            reviews = review_form.save(commit=False)
            reviews.user = request.user
            reviews.save()

            return redirect(request.GET.get('next'))
            # return redirect('reviews:index')
    else:
        review_form = ReviewForm(instance=review)
    context = {
        'review_form' : review_form
    }
    return render(request, 'reviews/form.html', context)

def delete(request, pk):
    Review.objects.get(pk=pk).delete()

    return redirect(request.GET.get('next'))
    # return redirect('reviews:index')


def comment_create(request, pk):
    review = get_object_or_404(Review, pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment.save()
        
        comments = Comment.objects.filter(review_id=pk).order_by('-pk')
        comments_data = []
        for co in comments:
            co.created_at = co.created_at.strftime('%Y-%m-%d %H:%M')
            comments_data.append(
                {
                    'request_user_pk': request.user.pk,
                    'comment_pk': co.pk,
                    'user_pk': co.user.pk,
                    'username': co.user.username,
                    'content': co.comment_content,
                    'created_at': co.created_at,
                    'updated_at':co.updated_at,
                    'review_pk':co.review_id,
                })
        context = {
            'comments_data':comments_data
        }
        return JsonResponse(context)

def comment_update(request, pk, comment_pk):
    if request.user.is_authenticated:
        jsonObject = json.loads(request.body)

        comment = Comment.objects.get(pk=comment_pk)
        comment.comment_content = jsonObject.get('content')
        comment.save()

        comments = Comment.objects.filter(review_id=pk).order_by('-pk')
        comments_data = []
        for co in comments:
            co.created_at = co.created_at.strftime('%Y-%m-%d %H:%M')
            comments_data.append(
                {
                    'request_user_pk': request.user.pk,
                    'comment_pk': co.pk,
                    'user_pk': co.user.pk,
                    'username': co.user.username,
                    'content': co.comment_content,
                    'created_at': co.created_at,
                    'updated_at':co.updated_at,
                    'review_pk':co.review_id,
                })
        context = {
            'comments_data':comments_data
        }
        return JsonResponse(context)

def comment_delete(request, pk, comment_pk):
    if request.user.is_authenticated:
        comment = Comment.objects.get(pk=comment_pk)
        comment.delete()
        
        comments = Comment.objects.filter(review_id=pk).order_by('-pk')
        comments_data = []
        for co in comments:
            co.created_at = co.created_at.strftime('%Y-%m-%d %H:%M')
            comments_data.append(
                {   'request_user_pk': request.user.pk,
                    'comment_pk': co.pk,
                    'user_pk': co.user.pk,
                    'username': co.user.username,
                    'content': co.comment_content,
                    'created_at': co.created_at,
                    'updated_at':co.updated_at,
                    'review_pk':co.review_id,
                })
        context = {
            'comments_data':comments_data
        }
        return JsonResponse(context)

def like(request, pk):
    review = get_object_or_404(Review, pk=pk)
    
    if review.review_liked.filter(id=request.user.id).exists():
    # if request.user in review.review_liked.all(): 
        review.review_liked.remove(request.user)
        review.like_count -= 1
        review.save()
        user = User.objects.get(pk=review.user_id)
        user.like_count -= 1
        user.save()
        is_liked = False
    else:
        review.review_liked.add(request.user)
        review.like_count += 1
        review.save()
        user = User.objects.get(pk=review.user_id)
        user.like_count += 1
        user.save()
        is_liked = True

    context = {
        'isLiked': is_liked, 
        'likeCount': review.review_liked.count(), 
        'gonggam_cnt': review.user.like_count
    }
    return JsonResponse(context)