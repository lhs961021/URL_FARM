from datetime import time
from django.shortcuts import get_object_or_404, redirect, render
from .models import Room
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
import json
from django.http import HttpResponse
from users.models import Profile
from django.db.models import Q
from .models import Chat
from analyze.models import URLAnalyze
from django.contrib.auth.models import User


# Create your views here.

def roomlist(request):
    rooms=Room.objects.all().order_by('-updated_at')
    mynick={}
    mynick['mynick']=request.user.profile.nickname
    
    return render(request,'roomlist.html',{'rooms':rooms,'mynick':mynick})

@login_required
def openroom(request):
    return render(request,'open.html')

def saveroominfo(request): 
    newroom=Room()
    newroom.name=request.POST['name']
    newroom.description=request.POST['description']
    newroom.writer=request.user
    newroom.created_at=timezone.now()
    newroom.updated_at=timezone.now()
    newroom.save()
    
    parti=json.loads(request.POST['participants'])
    parti[f'{newroom.writer.id}']=newroom.writer.profile.nickname
    #여기서 id값으로 add
    participant=list(parti.keys())
    join=User.objects.filter(id__in=participant)
    for person in join:
        newroom.participants.add(person)
    
    return redirect('shared_chat:chatroom',newroom.id)

@login_required
def fixroom(request, id):
    fixroom=Room.objects.get(id=id)
    already={}
    for i in fixroom.participants.all():
        if i !=request.user:
            already[i.id]=i.profile.nickname
    # print(already)
    return render(request,'fix.html',{"room":fixroom,"already":already})

def updateroominfo(request,id): 
    
    thisroom=Room.objects.get(id=id)
    thisroom.name=request.POST['name']
    thisroom.description=request.POST['description']
    thisroom.updated_at=timezone.now()
    thisroom.save()
    
    parti=json.loads(request.POST['participants'])
    parti[f'{thisroom.writer.id}']=thisroom.writer.profile.nickname
    participant=list(parti.keys())
    join=User.objects.filter(id__in=participant)
    thisroom.participants.clear()
    for person in join:
        thisroom.participants.add(person)
    
    return redirect('shared_chat:chatroom', thisroom.id)
    
def deleteroom(request, id):
    deleteroom=get_object_or_404(Room,id=id)
    deleteroom.delete()
    return redirect ('shared_chat:roomlist')

@require_POST
def nick_check(request):
    
    nickname=json.loads(request.body)
    
    nickname=nickname['nick']
    
    if nickname == '': # 닉네임이 쳤다가 다지워서 빈게 contains인 경우 제외
        list=''
    else:
        list=Profile.objects.filter(nickname__contains=nickname).exclude(Q(nickname='')|Q(nickname=request.user.profile.nickname))
    # print(list)
    
    nicklist={}
    for i in list:
        nicklist[i.id]=i.nickname
    # print(nicklist)
    
    return HttpResponse(json.dumps(nicklist),content_type="application/json")


def chatroom(request,room_id): #detail
    room = get_object_or_404(Room,pk=room_id)
    chats = Chat.objects.filter(room=room).order_by('updated_at')
    myurls = URLAnalyze.objects.filter(writer=request.user)
    return render(request,'chat.html',{'chats':chats,'room':room,'myurls':myurls})


def create_chat(request,room_id):
    room = get_object_or_404(Room,pk=room_id)
    chat = Chat()
    chat.writer = request.user
    chat.body = request.POST['body']
    chat.room = room
    chat.created_at=timezone.now()
    chat.updated_at=timezone.now()
    if(request.POST['urlid']):
        urlid=request.POST['urlid']
        urlid=int(urlid)
        # print(urlid)
        # print(type(urlid))
        url=get_object_or_404(URLAnalyze,pk=urlid)
        chat.url=url
    chat.save()
    
    return redirect('shared_chat:chatroom',room_id)


    
def fixchat(request,room_id,chat_id): 
    room = get_object_or_404(Room,pk=room_id)
    chats = Chat.objects.filter(room=room).order_by('updated_at')
    pick = get_object_or_404(Chat,pk=chat_id) 
    return render(request,'update.html',{'chats':chats,'room':room,"pick":pick})


def update_chat(request,room_id,chat_id):
    # room = get_object_or_404(Room,pk=room_id)
    chat = get_object_or_404(Chat,pk=chat_id)  
    chat.body = request.POST['body']
    chat.updated_at=timezone.now()
    chat.save()
    
    return redirect('shared_chat:chatroom',room_id)

def delete_chat(request,room_id,chat_id):
    # room = get_object_or_404(Room,pk=room_id)
    chat = get_object_or_404(Chat,pk=chat_id)
    chat.delete()
    
    return redirect('shared_chat:chatroom',room_id)

