from django.urls import path
from django.views.generic import TemplateView


app_name = 'blog_zona'

urlpatterns = [
    path('',TemplateView.as_view(template_name='zona_blog/index.html')),
]