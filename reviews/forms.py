from django import forms
from .models import Review, Comment

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['review_content', 'review_rating', 'review_taste', 'review_price', 'review_service', 'review_image',]


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment_content',]