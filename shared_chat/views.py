from datetime import time
from django.shortcuts import redirect, render
from .models import Room
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
import json
from django.http import HttpResponse
from users.models import Profile
from django.db.models import Q

# Create your views here.

def roomlist(request):
    rooms=Room.objects.all().order_by('-updated_at')
    mynick={}
    mynick['mynick']=request.user.profile.nickname
    
    return render(request,'roomlist.html',{'rooms':rooms,'mynick':mynick})

@login_required
def openroom(request): #맨처음 빈거만들어서 함
    newroom=Room()
    newroom.name=''
    newroom.description=''
    newroom.participants=''
    newroom.created_at=timezone.now()
    newroom.updated_at=timezone.now()
    newroom.writer=request.user
    newroom.save()
    
    return render(request,'open&fix.html',{'room':newroom})

def saveroominfo(request,id): #맨처음 빈거 생성하고 바로수정변경때도 쓰고, 그냥 수정때도씀
    
    thisroom=Room.objects.get(id=id)
    thisroom.name=request.POST['name']
    thisroom.description=request.POST['description']
    parti=json.loads(request.POST['participants'])
    parti[f'{thisroom.writer.id}']=thisroom.writer.profile.nickname
    thisroom.participants=parti
    thisroom.updated_at=timezone.now()
    thisroom.save()
    return redirect('shared_chat:roomlist')
    
def chatroom(request,id):
    return render(request,'chat.html')

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