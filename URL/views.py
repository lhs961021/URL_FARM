from django.shortcuts import redirect, render
from analyze.models import URLAnalyze
def index(request):
    if request.user.is_authenticated:
        if request.user.profile.level==1:
            info=URLAnalyze.objects.get(check=request.user.id)
            return render(request,'main.html',{"info":info})
        else: # 맨처음, 확인후 추가입력 해야 할 경우
            print(request.user.profile.level)
            return render(request,'main.html')
    else:
        return render(request,'index.html')
        
        
def diff(request): #크롤링 한 값이랑 내가 생각한 부분이 다를때 다음 단계로
    request.user.profile.level+=1
    request.user.profile.save()
    return redirect('index')