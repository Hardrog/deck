from django.urls import path

from .views import *

urlpatterns = [
    path('demo', demo, name="demo")
]