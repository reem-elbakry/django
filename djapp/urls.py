from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('show/<std_id>', views.show),

]
