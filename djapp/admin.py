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

# Register your models here.  (in admin site)

admin.site.register(Student, CustomStudent)
admin.site.register(Track)




