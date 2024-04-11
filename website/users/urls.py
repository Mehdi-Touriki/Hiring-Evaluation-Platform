from django.urls import path
from . import views
urlpatterns =[
    path('', views.home,name='home'),
    path('login/', views.login),
    path('recruteur/', views.home_rec,name='post_job'),
    path('candidat/', views.home_can,name='jobs'),
    path('recruteur/signuprec/', views.register_recruter,name='register_recruter'),
    path('candidat/signupcan/', views.register_candidat,name='register_candidat'),
    path('recruteur/formulaire', views.post_job),
    # todo: modify this path for dynamic description mr.database
    path('candidat/description', views.description)
]
