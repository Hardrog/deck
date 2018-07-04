from django.urls import path, include

from .views import *
from django.contrib.auth import views

urlpatterns = [
    path('demo', demo, name="demo"),
    path('auth/', include('social_django.urls', namespace='social')),
    path('login/', views.login, name='login'),
    path('',  home, name='home')
]