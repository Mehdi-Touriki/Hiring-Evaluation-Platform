from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('login/', views.login),
    path('recruteur/', views.home_rec),
    path('candidat/', views.home_can),
    path('recruteur/signuprec/', views.signuprec),
    path('candidat/signupcan/', views.signupcan),
    path('recruteur/formulaire', views.post_job),
    # todo: modify this path for dynamic description mr.database
    path('candidat/description', views.description),
    path('login/',views.home)
]
