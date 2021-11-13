from django.shortcuts import redirect, render

# Create your views here.

def roomlist(request):
    
    return render(request,'roomlist')

def openroom(request):
    return render(request,'openroom')

def saveroominfo(request):
    
    redirect('shared_chat:roomlist')