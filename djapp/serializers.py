from dataclasses import field
from rest_framework import serializers
from .models import Student, Track


#to serialize (sent into rest api 'json' response) data of model create obj from its serializer 
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields = ('fname', 'lname', 'age', 'student_track')  
        #or 
        fields = '__all__'

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'