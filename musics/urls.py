from django import views
from musics.views import addMusic, homePage,main,physical,mental
from django.urls import path

app_name='musics'

urlpatterns = [
    path('',main,name="main"),
    path('physical/',physical,name='physical'),
    path('mental/',mental,name='mental'),
    path('home/',homePage,name='home_page'), 
    path('add/',addMusic,name='add_music'),  

]
