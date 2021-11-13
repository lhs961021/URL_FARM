from django.urls import path, include
from .views import *

app_name="analyze"

urlpatterns = [
    path('crawl',crawl,name="crawl"),
    path('analyze',analyze,name="analyze"),
    path('modify',modify,name="modify"),
    
]
