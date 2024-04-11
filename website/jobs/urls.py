from django.urls import path
from . import views
from .views import JobListView, JobDescriptionView, JobApplyView, JobCreateView, JobDeleteView, JobUpdateView

app_name = 'jobs'

urlpatterns = [
    path('jobs/', JobListView.as_view(), name='job_list'),
    path('jobs/<int:pk>/', JobDescriptionView.as_view(), name='job_description'),
    path('jobs/<int:pk>/apply/', JobApplyView.as_view(), name='job_apply'),
    path('new/', JobCreateView.as_view(), name='job_create'),
    path('recruteur/', views.post_job, name='post_job'),
    path('<int:pk>/update/', JobUpdateView.as_view(), name='job_update'),
    path('<int:pk>/delete/', JobDeleteView.as_view(), name='job_delete'),
]
