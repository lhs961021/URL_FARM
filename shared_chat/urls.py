from django.urls import path, include
from .views import *

app_name="shared_chat"

urlpatterns = [
    
    path('roomlist',roomlist,name="roomlist"),
    path('openroom',openroom,name="openroom"),
    path('saveroominfo',saveroominfo,name="saveroominfo"),
    path('fixroom/<int:id>',fixroom,name="fixroom"),
    path('updateroominfo/<int:id>',updateroominfo,name="updateroominfo"),
    path('deleteroom/<int:id>',deleteroom,name="deleteroom"),
    path('nick_check',nick_check,name="nick_check"),
    path('chatroom/<int:room_id>',chatroom,name="chatroom"),
    path('fixchat/<int:room_id>/<int:chat_id>',fixchat,name="fixchat"),
    path('create_chat/<int:room_id>',create_chat,name="create_chat"),
    path('update_chat/<int:room_id>/<int:chat_id>',update_chat,name="update_chat"),
    path('delete_chat/<int:room_id>/<int:chat_id>',delete_chat,name="delete_chat"),
    
    
    
]
