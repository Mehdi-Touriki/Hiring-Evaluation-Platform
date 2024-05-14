from django.urls import path
from . import views
from .views import (
    JobListView,
    saved_post,
    JobDescriptionView,
    JobDeleteView,
    JobUpdateView,
    AllApplicants,
    Myrequest,
    MyJobListView,
    MysaveJobListView)

app_name = 'jobs'

urlpatterns = [
    path('jobs/', JobListView.as_view(), name='job_list'),
    path('jobs/<int:pk>/', JobDescriptionView.as_view(), name='job_description'),
    path('jobs/<int:pk>/apply/', views.job_apply_view, name='job_apply'),
    path('jobs/profil/', views.profil, name='profil'),  # Updated URL pattern here
    path('jobs/saved/', saved_post.as_view(), name='saved'),  # Updated URL pattern here hta hada

    path('recruteur/new/', views.job_create_view, name='job_create'),
    path('jobs/my_saves/', MysaveJobListView.as_view(), name='my_saves'),  # o hada
    path('recruteur/myjobs/', MyJobListView.as_view(), name='my_jobs'),
    path('candidat/myjobs/', Myrequest.as_view(), name='requests'),
    path('recruteur/', views.post_job, name='post_job'),
    path('recruteur/<int:pk>/update/', JobUpdateView.as_view(), name='job_update'),
    path('recruteur/<int:pk>/delete/', JobDeleteView.as_view(), name='job_delete'),
    path('recruteur/<int:pk>/applicantsposted/', AllApplicants.as_view(), name='applicant_posted'),
    
    # Nouvelles URLs pour les catégories
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:pk>/', views.category_detail, name='category_detail'),


# Nouvelles URLs pour les offres d'emploi
#     path('post/new/', views.post_create_view, name='post_create'),
#     path('post/<int:pk>/', views.post_detail_view, name='post_detail'),
#     path('post/<int:pk>/update/', views.post_update_view, name='post_update'),
#     path('post/<int:pk>/delete/', views.post_delete_view, name='post_delete'),
]

