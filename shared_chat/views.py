from django.shortcuts import redirect, render
from .models import Room
# Create your views here.

def roomlist(request):
    rooms=Room.objects.all()
    return render(request,'roomlist',{'rooms':rooms})

def openroom(request):
    return render(request,'openroom')

def saveroominfo(request):
    
    redirect('shared_chat:roomlist')
    
def chat(request):
    return render(request,'chat.html')