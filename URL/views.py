from django.shortcuts import render
from analyze.models import URLAnalyze
def index(request):
    if request.user.is_authenticated:
        return render(request,'main.html')
    else:
        
        return render(request,'index.html')