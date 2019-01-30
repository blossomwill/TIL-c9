from django.urls import path
from . import views

# 앞에 /는 없고 뒤에 /는 작성한다
urlpatterns = [
    path('',views.index, name='list'), 
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:question_id>/', views.detail, name='detail'),
    ]