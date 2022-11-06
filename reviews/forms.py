from django import forms
from .models import Review, Comment
class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['review_image', 'review_content', 'review_taste', 'review_price', 'review_service', 'review_rating',]
        labels = {
            'review_content': '리뷰 내용',
            'review_rating': '총 평점',
            'review_taste': '맛 평점',
            'review_price': '가격 평점',
            'review_service': '서비스 평점',
            'review_image': '첨부 이미지',
        }
        widgets = {
            'review_content': forms.Textarea(attrs={'placeholder': '리뷰 내용을 작성해주세요.'}),
            'review_rating': forms.TextInput(attrs={'placeholder': '1~5', 'style': 'width:55px;'}),
            'review_taste': forms.TextInput(attrs={'placeholder': '1~5', 'style': 'width:55px;'}),
            'review_price': forms.TextInput(attrs={'placeholder': '1~5', 'style': 'width:55px;'}),
            'review_service': forms.TextInput(attrs={'placeholder': '1~5', 'style': 'width:55px;'}),
        }
        help_texts = {
            'review_rating': '1~5점 사이로 입력해주세요',
            'review_taste': '1~5점 사이로 입력해주세요',
            'review_price': '1~5점 사이로 입력해주세요',
            'review_service': '1~5점 사이로 입력해주세요',
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