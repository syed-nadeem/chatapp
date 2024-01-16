from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('auth/', include('allauth.urls')),
    path('chat/', include('chat.urls'))
]
