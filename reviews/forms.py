from django import forms
from .models import Review, Comment

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['review_content', 'review_rating', 'review_taste', 'review_price', 'review_service', 'created_at', 'updated_at', 'review_image',]


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment_content',]