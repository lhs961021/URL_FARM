from django.urls import path, include
from .views import *

app_name="users"

urlpatterns = [
    path('mypage',mypage,name='mypage'),
    path('pick_url/<int:id>',pick_url,name='pick_url'),
    
]
