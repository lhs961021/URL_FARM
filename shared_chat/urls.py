from django.urls import path, include
from .views import *

app_name="shared_chat"

urlpatterns = [
    
    path('roomlist',roomlist,name="roomlist"),
    path('openroom',openroom,name="openroom"),
    path('saveroominfo',saveroominfo,name="saveroominfo"),
    path('fixroom/<int:id>',fixroom,name="fixroom"),
    path('updateroominfo/<int:id>',updateroominfo,name="updateroominfo"),
    path('chatroom/<int:id>',chatroom,name="chatroom"),
    path('deleteroom/<int:id>',deleteroom,name="deleteroom"),
    path('nick_check',nick_check,name="nick_check"),
    
]
