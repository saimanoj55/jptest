from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Add this line to handle the root URL
    path('jobs/', views.job_list, name='job_list'),
    path('jobs/<int:job_id>/', views.job_detail, name='job_detail'),
    path('register/', views.register, name='register'),
    # other URL patterns...
]
