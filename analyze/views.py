from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
import requests
from bs4 import BeautifulSoup
from gensim.summarization.summarizer import summarize
from .models import *
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from ml.predict import predict_category,tfidfwordcloud


# Create your views here.

def beautifulcrawl(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    webpage = requests.get(f"{url}",headers=headers)
    soup = BeautifulSoup(webpage.content,"html.parser")
    title=soup.title.string
    content=soup.find('div',attrs={'id':'articleBodyContents'})
    content=content.get_text().replace("\n","").replace("// flash 오류를 우회하기 위한 함수 추가function _flash_removeCallback() {}","").replace("\t","").replace(".",". ")

    return title,content

@login_required
def crawl(request):
    url=request.POST['url']
    title,content=beautifulcrawl(url)
    
    post=URLAnalyze()
    post.url=url
    post.title=title
    post.content=content
    post.check=request.user.id
    post.writer=request.user
    post.created_at=timezone.now()
    post.updated_at=timezone.now()
    post.save()
    request.user.profile.level+=1
    request.user.profile.save()
    return redirect('index')
    
def modify(request): #크롤링 내용이랑 달라서 내용 변경해야할때    

    info=URLAnalyze.objects.get(check=request.user.id)
    info.url=request.POST['url']
    info.title=request.POST['title']
    info.content=request.POST['content']
    info.check=-1 #변경완료 check
    info.updated_at=timezone.now()
    info.category=predict_category(info.content) #고치기
    tfidfwordcloud(info.content,info.id) #워드클라우드
    info.content=summarize(info.content,word_count=70) #본문요약
    info.save()

    request.user.profile.level=0#url 내용 입력받아 저장하고 다시 첫단계로
    request.user.profile.save()
    # print(request.user.profile.level)
    return redirect('index')

def analyze(request): #맞나요? 해서 맞다하면 여기로옴
    
    request.user.profile.level=0#url 크롤링 잘된거 확인하고 다시 첫단계로
    request.user.profile.save()
    
    # 분석시작해야함 그런데 여기서 불러올때는 내 urlanalyze모델에 check칼럼에 내 id값이 저장되어있는걸로 불러오고
    # 전처리하고 check값 -1로 바꿔주기(이 url 전처리 다했다 인증임)
    info=URLAnalyze.objects.get(check=request.user.id)
    info.category=predict_category(info.content) #카테고리도 여기서
    tfidfwordcloud(info.content,info.id) #워드클라우드
    info.content=summarize(info.content,word_count=70) #본문요약
    info.check=-1
    info.save()
    return redirect('analyze:URL_detail',info.id)

def URL_detail(request,id):
    urlinfo=get_object_or_404(URLAnalyze,pk=id)
    
    return render(request,'detail.html',{'urlinfo':urlinfo})

def URL_delete(request,id):
    urlinfo=get_object_or_404(URLAnalyze,pk=id)
    urlinfo.delete()
    return redirect('users:mypage')

def taken_url(request, id):
    
    url=get_object_or_404(URLAnalyze,pk=id)
    me=get_object_or_404(User,pk=request.user.id)
    
    if me in url.taken.all():
        url.taken.remove(me)
    else:
        url.taken.add(me)
    
    return redirect('users:mypage')