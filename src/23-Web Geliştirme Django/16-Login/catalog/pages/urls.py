from django.urls import path
from . import views

# http://127.0.0.1:8000/

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
]