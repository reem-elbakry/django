from django import forms
from .models import Student, Track

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('fname', 'lname', 'age', 'student_track')


class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ('track_name', )  # , for tuble ... not grouping
