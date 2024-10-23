
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog_zona.urls', namespace='blog_zona')),
    path('api/',include('blog_zona_api.urls', namespace='blog_zona_api')),

]
