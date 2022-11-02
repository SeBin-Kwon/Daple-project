from .models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('profile_image', 'nickname', 'username', 'password1', 'password2', 'email', 'phone','Is_owner')
        labels = {
            'profile_image': '프로필사진',
            'nickname': '이름',
            'username': '아이디',
            'password1': '비밀번호',
            'password2': '비밀번호확인',
            'email': '이메일주소',
            'phone': '휴대폰번호',
            'Is_owner': '가게 주인이신가요?',
        }