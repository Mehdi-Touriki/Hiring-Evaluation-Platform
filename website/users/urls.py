from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    # path('recruteur/', include('job.urls'), name='post_job'),
    path('candidat/', include('jobs.urls'), name='jobs'),
    path('recruteur/signuprec/', views.register_recruter, name='register_recruter'),
    path('candidat/signupcan/', views.register_candidat, name='register_candidat'),
    # path('recruteur/formulaire', views.post_job),
]
