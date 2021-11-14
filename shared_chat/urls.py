from django.urls import path, include
from .views import *

app_name="shared_chat"

urlpatterns = [
    
    path('roomlist',roomlist,name="roomlist"),
    path('openroom',openroom,name="openroom"),
    path('saveroominfo/<int:id>',saveroominfo,name="saveroominfo"),
    path('chatroom/<int:id>',chatroom,name="chatroom"),
    path('nick_check',nick_check,name="nick_check"),
    
]
