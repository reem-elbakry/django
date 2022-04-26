from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('details/<std_id>', views.show, name='show'),
    path('delete/<std_id>', views.delete, name='delete'),
    path('create/', views.createStudent, name='create'),
    path('edit/<std_id>', views.editStudent, name='edit'),



    #rest_framework path

    path('api-all/', views.api_all_student, name='api-all'),
    path('api-one/<std_id>', views.api_one_student, name='api-one'),
    path('api-add/', views.api_add_student, name='api-add'),
    path('api-edit/<std_id>', views.api_edit_student, name='api-edit'),
    path('api-del/<std_id>', views.api_del_student, name='api-del'),







]
