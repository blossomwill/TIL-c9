from django.urls import path
from . import views
app_name = 'pages'

urlpatterns = [
    path('', views.index, name='list'),
    path('hello/<str:name>/', views.hello, name='hello'),
    path('create/', views.create, name='create'),
    path('new/', views.new, name='new'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('<int:post_id>/delete/', views.delete, name='delete')
    ]
    