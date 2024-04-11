from django.urls import path, include
from . import views

app_name = "users"

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    # path('recruteur/', include('job.urls'), name='post_job'),
    # path('candidat/', include('jobs.urls'), name='jobs'),
    path('recruteur/signup/', views.register_recruter, name='register_recruter'),
    path('candidat/signup/', views.register_candidat, name='register_candidat'),
    # path('recruteur/formulaire', views.post_job),
]
