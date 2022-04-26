from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('details/<std_id>', views.show, name='show'),
    path('delete/<std_id>', views.delete, name='delete'),
    path('create/', views.createStudent, name='create'),
    path('edit/<std_id>', views.editStudent, name='edit'),



]
