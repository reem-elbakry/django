from pyexpat import model
from django import forms
from .models import Student, Track

#auth import 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('fname', 'lname', 'age', 'student_track')
        Widgets = {
            'fname' : forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Enter your first name'}),
            'lname' : forms.TextInput(attrs={ 'class': 'form-control'}),
            'age' : forms.NumberInput(attrs={ 'class': 'form-control'}),
            'student_track' : forms.Select(attrs={ 'class': 'form-control'}),
        }


class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ('track_name', )  # , for tuble ... not grouping







#form validation (cleaned_data)
