from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = "users"

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="logout.html"), name='logout'),
    # path('recruteur/', include('job.urls'), name='post_job'),
    # path('candidat/', include('jobs.urls'), name='jobs'),
    path('recruteur/signup/', views.register_recruter, name='register_recruter'),
    path('candidat/signup/', views.register_candidat, name='register_candidat'),
    # path('recruteur/formulaire', views.post_job),
]
