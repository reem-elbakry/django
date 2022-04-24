from django.db import models

# Create your models here.   

'''
class is a table
object is a row
attributes ia a column
'''

class Track(models.Model):
    track_name = models.CharField(max_length=20)


class Student(models.Model):
    fname = models.CharField(max_length=20, null=True)
    lname = models.CharField(max_length=20, default='NoName')
    age = models.IntegerField()
    student_track = models.ForeignKey(Track, on_delete=models.CASCADE)