from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):

    section = request.path.strip('/')  # تحديد القسم بناءً على URL
    home = Home.objects.last()
    about = AboutMe.objects.last()
    skills = Skill.objects.all()


    return render(request, 'index.html')