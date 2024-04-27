from django.urls import path
from . import views
from .views import (
    JobListView,
    ToggleSavedPost,
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
    path('jobs/saved/', ToggleSavedPost.as_view(), name='toggle_saved'),  # Updated URL pattern here hta hada

    path('recruteur/new/', views.job_create_view, name='job_create'),
    path('jobs/my_saves/', MysaveJobListView.as_view(), name='my_saves'),  # o hada
    path('recruteur/myjobs/', MyJobListView.as_view(), name='my_jobs'),
    path('candidat/myjobs/', Myrequest.as_view(), name='requests'),
    path('recruteur/', views.post_job, name='post_job'),
    path('recruteur/<int:pk>/update/', JobUpdateView.as_view(), name='job_update'),
    path('recruteur/<int:pk>/delete/', JobDeleteView.as_view(), name='job_delete'),
    path('recruteur/<int:pk>/applicantsposted/', AllApplicants.as_view(), name='applicant_posted'),
]
