from django.urls import path
from . import views
from .views import JobListView, JobDescriptionView, JobApplyView, JobCreateView, JobDeleteView, JobUpdateView

app_name = 'jobs'

urlpatterns = [
    path('', JobListView.as_view(), name='job_list'),
    path('<int:pk>/', JobDescriptionView.as_view(), name='job_description'),
    path('<int:pk>/apply/', views.apply, name='job_apply'),
    path('new/', JobCreateView.as_view(), name='job_create'),
    path('<int:pk>/update/', JobUpdateView.as_view(), name='job_update'),
    path('<int:pk>/delete/', JobDeleteView.as_view(), name='job_delete'),
]
