from multiprocessing import context
from xml.parsers.expat import model
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student, Track
from .forms import StudentForm

#rest_framework imports here.

from .serializers import StudentSerializer

#Response take oj return in api response
from rest_framework.response import Response
#determine view func hit by get or post method
from rest_framework.decorators import api_view




#rest_framework views here.

@api_view(['GET'])
def api_all_student(request):
    all_st = Student.objects.all()
    #serialize data  #many == list of objs of model ..loop 
    st_ser = StudentSerializer(all_st, many=True)
    return Response(st_ser.data)


@api_view(['GET'])
def api_one_student(request, std_id):
    student = Student.objects.get(id=std_id)
    st_ser = StudentSerializer(student, many=False)
    return Response(st_ser.data)


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

def createStudent(request):
    #create empty student obj form 
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')


    context = {'form' : form}
    return render(request, 'djapp/create.html', context)

def editStudent(request, std_id):
    student = Student.objects.get(id=std_id)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')

            
    context = {'form': form}
    return render(request, 'djapp/create.html', context)








    