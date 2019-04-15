from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model() # 현재 쓰고있는 모델의 class를 가져오는 method
        fields = ['username', 'email', 'first_name', 'last_name',]
    