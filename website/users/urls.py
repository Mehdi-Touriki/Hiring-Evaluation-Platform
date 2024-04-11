from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.home, name='logged_out_home'),
    path('candidat/', include("jobs.urls"), name='candidat_home'),
    path('recruteur/', views.home_rec, name='recruiter_home'),
]

