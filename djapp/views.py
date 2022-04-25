from xml.parsers.expat import model
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student, Track

# Create your views here.

def home(request):
    all_students = Student.objects.all()
    #3rd param is context var ... {'key = anything' : 'val = all_students'}
    context = { 'student_list': all_students }
    return render(request, 'djapp/home.html', context )

def show(request, std_id):
    student = Student.objects.get(id = std_id)
    context = {'student': student}
    return render(request, 'djapp/show.html', context)

def delete(request, std_id):
    Student.objects.get(id = std_id).delete()
    return redirect('home')

    