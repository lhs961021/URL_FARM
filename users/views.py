from django.shortcuts import render
from analyze.models import URLAnalyze
# Create your views here.

def mypage(request):
    urls=URLAnalyze.objects.filter(writer=request.user)
    return render(request,'mypage.html',{'urls':urls})