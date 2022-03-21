
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from SleepApp.views import index,sleep
from FoodApp.views import calorie, food,fruit,vegetables,nuts,dairy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('musics.urls', namespace='music')),
    path('sleep/',sleep,name='sleep'),
    path('chart/',index,name='index'),
    path('food/',food,name='food'),
    path('fruits/',fruit,name='fruits'),
    path('calorie/',calorie,name='calorie'),
    path('vegetables/',vegetables,name='vegetables'),
    path('nuts/',nuts,name='nuts'),
    path('dairy/',dairy,name='dairy')
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
