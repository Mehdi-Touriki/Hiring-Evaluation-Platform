from django.urls import path
from . import views
from .views import(
    JobListView,
    JobDescriptionView,
    JobDeleteView,
    JobUpdateView,
    MyJobListView)

app_name = 'jobs'

urlpatterns = [
    path('jobs/', JobListView.as_view(), name='job_list'),
    path('jobs/<int:pk>/', JobDescriptionView.as_view(), name='job_description'),
    path('jobs/<int:pk>/apply/', views.job_apply_view, name='job_apply'),
    path('recruteur/new/', views.job_create_view, name='job_create'),
    path('recruteur/myjobs/', MyJobListView.as_view(), name='my_jobs'),
    path('recruteur/', views.post_job, name='post_job'),
    path('recruteur/<int:pk>/update/', JobUpdateView.as_view(), name='job_update'),
    path('recruteur/<int:pk>/delete/', JobDeleteView.as_view(), name='job_delete'),
]
