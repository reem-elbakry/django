from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('details/<std_id>', views.show, name='show'),

]
