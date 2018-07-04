from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

def demo(request):
    cards = Card.objects.all()
    return render(request, 'demo.html',{"cards":cards})

@login_required(login_url='/login')
def home(request):
	return render(request, 'home.html')