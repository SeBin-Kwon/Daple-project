from django.shortcuts import render, redirect
from .models import Review, Comment
from .forms import ReviewForm, CommentForm
# Create your views here.

def index(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews' : reviews
    }
    return render(request, 'reviews/index.html', context)

def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('reviews:index')
    else:
        form = ReviewForm()
    context = {
        'form' : form
    }
    return render(request, 'reviews/form.html', context)

def delete(request, pk):
    Review.objects.get(pk=pk).delete()
    return redirect('reviews:index')

def update(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            reviews = form.save(commit=False)
            reviews.user = request.user
            reviews.save()
            return redirect('reviews:index')
    else:
        form = ReviewForm(instance=review)
    context = {
        'form' : form
    }
    return render(request, 'reviews/form.html', context)

def comment_create(request, pk):
    if request.user.is_authenticated:
        reviews = get_object_or_404(Review, pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.review = reviews
            comment.user = request.user
            comment.save()
        return redirect('reviews:index')
    return redirect('accounts:login')

def comment_update(request, comment_pk):
    if request.user.is_authenticated:
        comment = Comment.objects.get(pk=comment_pk)
        comment_form = CommentForm(request.POST, instance=comment)

        if request.method == "POST":
            if request.user == comment.user:
                if comment_form.is_valid():
                    comment_form.save()


        return redirect('reviews:index')
    return redirect('accounts:login')

def comment_delete(request, comment_pk):
    if request.user.is_authenticated:
        comment = Comment.objects.get(pk=comment_pk)
        comment.delete()
        return redirect('reviews:index')
    return redirect('accounts:login')

