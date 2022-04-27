from multiprocessing import context
from xml.parsers.expat import model
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student, Track
from .forms import StudentForm, UserForm

#rest_framework imports here.

from .serializers import StudentSerializer
#Response take oj return in api response
from rest_framework.response import Response
#determine view func hit by get or post method
from rest_framework.decorators import api_view

#auth imports
#login ..logout .. sessions 
#authenticate .. database .. return if exists .. null if not exists 
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

#auth views

def signupPg(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
        signup_form = UserForm()
        if request.method == 'POST':
            signup_form = UserForm(request.POST)
            if signup_form.is_valid():
                signup_form.save()
                msg = 'User account created for username' + signup_form.cleaned_data.get('username')
                messages.info(request, msg)
                return redirect('login')
        context = {'signup_form': signup_form}
        return render(request, 'djapp/signup.html', context)




def loginPg(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')
            user = authenticate(username= name, password= passwd)
            if user is not None:
                login(request, user)
                if request.GET.get('next') is not None:
                    return redirect(request.GET.get('next'))
                else:
                    return redirect('home')
            else:
                messages.info(request, 'Username or password is incorrect')
        return render(request, 'djapp/login.html')


def signoutPg(request):
    logout(request)
    return redirect('login')
        




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


@api_view(['POST'])
def api_add_student(request):
    st_ser = StudentSerializer(data=request.data)
    if st_ser.is_valid():
        st_ser.save()
        return redirect('api-all')

@api_view(['POST', 'GET'])
def api_edit_student(request, std_id):
    student = Student.objects.get(id=std_id)
    if request.method == 'GET':
        st_ser = StudentSerializer(student, many=False)
        return Response(st_ser.data)
    else:
        st_ser = StudentSerializer(data=request.data, instance=student)
        if st_ser.is_valid():
            st_ser.save()
            return redirect('api-all')

@api_view(['DELETE'])
def api_del_student(request, std_id):
    student = Student.objects.get(id=std_id)
    student.delete()
    return Response('Student deleted!')







# Create your views here.
@login_required(login_url='login')
def home(request):
    all_students = Student.objects.all()
    #3rd param is context var ... {'key = anything' : 'val = all_students'}
    context = { 'student_list': all_students }
    return render(request, 'djapp/home.html', context )

@login_required(login_url='login')
def show(request, std_id):
    student = Student.objects.get(id = std_id)
    context = {'student': student}
    return render(request, 'djapp/show.html', context)

@login_required(login_url='login')
def delete(request, std_id):
    Student.objects.get(id = std_id).delete()
    return redirect('home')

@login_required(login_url='login')
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

@login_required(login_url='login')
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








    














    ##permissions ... self study