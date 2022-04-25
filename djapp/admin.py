from django.contrib import admin
from .models import Student, Track

#for customization
#admin home == tuble contain lists == panels .. (['panel_title', {'fields': ['field_name', '', '', '']}], [])

#inheret from admin == customization on a model registered on admin site
class CustomStudent(admin.ModelAdmin):                  
    #fieldsets, fields are predefined vars in admin app .. edit it
    fieldsets = (
        ['Student Information', {'fields': ['fname', 'lname','age']}],
        ['Scholarship information', {'fields': ['student_track']}]
    )

    list_display = ('fname', 'lname', 'age', 'student_track', 'is_adult')

#custom track == not to add track without students 
#need to inject student form to track form
#make student form to be injectable ... inline and use it in track form

class InlineStudent(admin.StackedInline):
    #override to vals .. models (model name) ..ext (how many time inject this model)
    model = Student
    extra = 1

class CustomTrack(admin.ModelAdmin):
    inlines = [InlineStudent]

# Register your models here.  (in admin site)

admin.site.register(Student, CustomStudent)
admin.site.register(Track, CustomTrack)




