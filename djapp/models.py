from django.db import models

# Create your models here.   

'''
class is a table
object is a row
attributes ia a column
'''

class Track(models.Model):
    track_name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.track_name


class Student(models.Model):
    fname = models.CharField(max_length=20, null=True)
    lname = models.CharField(max_length=20, default='NoName')
    age = models.IntegerField()
    student_track = models.ForeignKey(Track, on_delete=models.CASCADE)

    #change string representation of the object
    #for any func under class
    #self obj ref
    def __str__(self):
        #override __str__()
        return self.fname + " " + self.lname
    
    #for derived col   ... then add name func (model class attr) to the display list in adim.py
    def is_adult(self):
        if self.age > 15:
            return True
        else:
            return False
              
    #to display it with another name
    is_adult.short_description = 'Graduated Student'

        