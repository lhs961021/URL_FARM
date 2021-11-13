from datetime import time
from django.shortcuts import redirect, render
from .models import Room
from django.utils import timezone
from django.views.decorators.http import require_POST
import json
from django.http import HttpResponse
from users.models import Profile
# Create your views here.

def roomlist(request):
    rooms=Room.objects.all()
    
    return render(request,'roomlist.html',{'rooms':rooms})

def openroom(request): #맨처음 빈거만들어서 함
    newroom=Room()
    newroom.name=''
    newroom.description=''
    newroom.participants=''
    newroom.created_at=timezone.now()
    newroom.updated_at=timezone.now()
    newroom.save()
    
    return render(request,'open&fix.html',{'room':newroom})

def saveroominfo(request,id): #맨처음 빈거 생성하고 바로수정변경때도 쓰고, 그냥 수정때도씀
    
    thisroom=Room.objects.get(id=id)
    thisroom.name=request.POST['name']
    thisroom.description=request.POST['description']
    thisroom.participants=request.POST['participants']
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
        list=Profile.objects.filter(nickname__contains=nickname).exclude(nickname='')
    # print(list)
    
    nicklist={}
    for i in list:
        nicklist[i.id]=i.nickname
    # print(nicklist)
    
    return HttpResponse(json.dumps(nicklist),content_type="application/json")