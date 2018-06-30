from django.shortcuts import render
from .models import *
# Create your views here.
def demo(request):
    cards = Card.objects.all()
    return render(request, 'demo.html',{"cards":cards})