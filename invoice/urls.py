
from django.urls import path,include

from . import views

urlpatterns = [
    path('search',views.search,name="search"),
    path('upload',views.upload,name="upload"),
    path('result',views.result,name="result"),
    
]


from django.conf import settings
from django.conf.urls.static import static
 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)