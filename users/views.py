from django.shortcuts import redirect, render,get_object_or_404
from analyze.models import URLAnalyze
from django.db.models import Q
from django.contrib.auth.models import User
# Create your views here.

def mypage(request):
    urls=URLAnalyze.objects.filter(Q(writer=request.user)&Q(check=-1)).order_by('-updated_at')
    return render(request,'mypage.html',{'urls':urls})

def pick_url(request, id):
    
    picked=get_object_or_404(URLAnalyze,pk=id)
    me=get_object_or_404(User,pk=request.user.id)
    
    if picked in me.profile.pick.all():
        me.profile.pick.remove(picked)
    else:
        me.profile.pick.add(picked)
    
    # for i in picked.user_pick_url_set.values():
    #     print(i['time'])
    # print(me.profile.pick.count())
    return redirect('users:mypage')
    