from django.urls import path, include
from .views import *

app_name="analyze"

urlpatterns = [
    path('crawl',crawl,name="crawl"),
    path('analyze',analyze,name="analyze"),
    path('modify',modify,name="modify"),
    path('URL_detail/<int:id>',URL_detail,name="URL_detail"),
    path('URL_delete/<int:id>',URL_delete,name="URL_delete"),
    path('taken_url/<int:id>',taken_url,name="taken_url"),
    path('makememo/<int:url_id>',makememo,name="makememo"),
    path('updatememo/<int:id>',updatememo,name="updatememo"),
    path('deletememo',deletememo,name="deletememo"),
]
