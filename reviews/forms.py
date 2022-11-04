from django import forms
from .models import Review, Comment

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['review_content', 'review_rating', 'review_taste', 'review_price', 'review_service', 'review_image',]
        labels = {
            'review_content': '리뷰 내용',
            'review_rating': '전체 평점',
            'review_taste': '맛',
            'review_price': '가격',
            'review_service': '서비스',
            'review_image': '첨부 이미지',
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment_content',]
        labels = {
            'comment_content': '',
        }
        widgets = {
            'comment_content': forms.TextInput(attrs={'placeholder': '댓글작성', 'style': 'width:400px;'}),
        }