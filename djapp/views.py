from xml.parsers.expat import model
from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, Track

# Create your views here.

def home(request):
    all_students = Student.objects.all()
    #3rd param is context var ... {'key = anything' : 'val = all_students'}
    context = { 'student_list': all_students }
    return render(request, 'djapp/home.html', context )

def show(request):
    st = Student.objects.all()[0].fname
    return HttpResponse(st)