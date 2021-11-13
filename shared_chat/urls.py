from django.urls import path, include
from .views import *

app_name="shared_chat"

urlpatterns = [
    
    path('roomlist',roomlist,name="roomlist"),
    path('openroom',openroom,name="openroom"),
    path('chat',chat,name="chat"),
    
    
]
