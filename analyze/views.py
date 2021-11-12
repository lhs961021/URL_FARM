from django.shortcuts import render,HttpResponse
import requests
from bs4 import BeautifulSoup
from .models import *
# Create your views here.

def crawl(request):
    url=request.POST['url']
    title,content=beautifulcrawl(url)
    
    post=URLAnalyze()
    post.url=url
    post.title=title
    post.content=content
    post.level+=1
    post.save()
    
    return HttpResponse("여기서 크롤링해야함")
    
def beautifulcrawl(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    webpage = requests.get(f"{url}",headers=headers)
    soup = BeautifulSoup(webpage.content,"html.parser")
    title=soup.title.string
    content=soup.find('div',attrs={'id':'articleBodyContents'})
    content=content.get_text().replace("\n","").replace("// flash 오류를 우회하기 위한 함수 추가function _flash_removeCallback() {}","").replace("\t","")
    return title,content